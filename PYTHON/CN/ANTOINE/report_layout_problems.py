# to run this script you need to have the gumball module installed
# see in ressources/pipeline/gumball for the latest version (stable)
# see in developement/python/gumball for the latest WIP version (unstable)

from gumball import shotgun, browser, gui, paths, asset_management as am
from sys import exit
from pprint import pprint

import difflib
import time
import re
import os


def prompt():
    ''' recursively prompt for episode name until valid or cancelled '''
    
    # gui
    input = gui.mbox(
        'Enter an episode name:',
        b1='Ok',
        b2='Cancel',
        entry=True)
    if not input:
        exit()
    
    # find the episode on shotgun
    episode = shotgun.sg.find_one(
        'Sequence',
        [['code','contains',input]],
        ['code'],
        [{'field_name':'created_at','direction':'desc'}])
    if not episode:
        episode = prompt()
    return episode


def parse_ep( inputstr ):
    ''' parse string to find episode name '''
    m = re.match(
        'GB\d{3}_(?:The)?([a-z]*)',
        inputstr,
        re.IGNORECASE
        )
    return m.groups()[0] if m else None


def get_shots( epname, path ):
    ''' find all shots folders at a given location
    and format them into a shotgun-style dict '''
    shots = []
    for root,dirs,files in os.walk( path ):
        for dir in dirs:
            if re.match('Sc\d{3}', dir):
                shotcode = epname.upper() + '_' + dir[2:]
                shots.append( 
                    {
                        'code': shotcode,
                        'lopath': os.path.join( root, dir )
                    })
        return shots


def find( path, *args, **kwargs ):
    ''' Attempts to find a filename in a directory tree
    use weak = True to allow for spelling mistakes
    use subdirs = False to only search root directory
    '''
    results = []
    for root,dirs,files in os.walk( path ):
        for file in files:
            fname = os.path.splitext(file)[0]
            for arg in args:
                if kwargs.get('weak') == True:
                    condition = same_asset( arg, fname )
                else:
                    condition = arg.upper() == fname.upper()
                if condition:
                    results.append( os.path.join(root,file) )
        if 'subdirs' in kwargs and kwargs['subdirs'] is False:
            dirs[:] = []
    results = [
        {'code':os.path.splitext(os.path.split(i)[1])[0],
        'el_path':i} for i in results
        ]
    return sorted(results) if results else None


def bg_is_reused( epname, bgname ):
    ''' returns True or False '''
    m = am.parse(bgname)
    if m and m.groups()[1].upper() == epname.upper():
        del m
        return False
    else:
        del m
        return True


def similaritude( str1, str2 ):
    ''' compares the similaritude in two string, returns a ratio '''
    ratio = difflib.SequenceMatcher(None, str1, str2).ratio()
    return ratio


def same_header( str1, str2 ):
    ''' compares the first two tokens of provided strings '''
    header1 = '_'.join( str1.split('_')[0:2] )
    header2 = '_'.join( str2.split('_')[0:2] )
    if header1.upper() == header2.upper():
        return True
    else:
        return False


def same_asset( str1, str2 ):
    ''' compares if two strings might represent the same asset even
    if spelling mistakes are included '''
    if same_header(str1,str2) and similaritude(str1, str2) > 0.8:
        return True
    else:
        return False


def assetlink( asset ):
    ''' returns a formatted markdown link to the 
    provided shotgun asset entity detail page '''
    
    # fix a weird behavior in shotgun, sometimes it returns entities
    # with 'name' key instead of 'code', but they both represent
    # the same thing.
    try:
        asset['name']
    except KeyError:
        asset['name'] = asset['code']
    
    retval = ( '[' + asset['name'] + 
               '](https://turneruk.shotgunstudio.com/detail/Asset/' +
               str(asset['id']) + ')' )
    return retval


def shotlink( shot ):
    ''' returns a formatted markdown link to the provided
    shotgun shot entity detail page '''
    retval = ( '[' + shot['code'] + 
               '](https://turneruk.shotgunstudio.com/detail/Shot/' + 
               str(shot['id']) + ')' )
    return retval


def link( name, path ):
    ''' returns a formatted markdown link '''
    retval = '[' + name + '](' + path + ')'
    return retval


def pandoc( inputfile, filetype ):
    ''' Document conversion using Pandoc executable, doc types
    are guessed from the file extensions. filetype is the target
    file extension '''
    
    # check input file
    spath, sfile = os.path.split( inputfile )
    filename, ext = os.path.splitext( sfile )
    if not ext.upper() == '.MD':
        raise IOError, 'Input file is not a markdown file'
    if not os.path.isfile( inputfile ):
        raise IOError, 'Could not find the input file'
    
    # prepare output file
    outputfile = os.path.join( spath, filename + '.'+filetype )
    if os.path.isfile( outputfile ):
        os.remove( outputfile )
    
    # send command to system
    os.system( paths.PANDOC + 
               ' -s --data-dir="' + paths.PANDOC[0:-11] + '"' +
               ' -o "' + outputfile + '"' +
               ' -i "' + inputfile + '"' )
    
    if os.path.isfile( outputfile ):
        return outputfile
    else:
        return False


def output( plist ):
    ''' Compiles the master problem list into a markdown file,
    return its location '''
               
    # create new file
    tempmd = os.path.join(os.environ['TMP'], 'rlptemp.md')
    while os.path.isfile(tempmd):
        os.remove(tempmd)
    
    # write the file
    with open(tempmd,'w') as f:
        f.write( '\n'.join( plist ) )
    
    return tempmd



############################ EXECUTION ################################


### global variables

all_problems_list = []  # Will be compiled into output file
backgrounds = []  # BGs that are found while searching shots


### initialization

episode = prompt()
epname = parse_ep(episode['code'])

loapp = browser.episode(epname).folder('loapp') # all layout shot folders
shots = shotgun.ShotList(get_shots(epname, loapp)) # retrieve sg info on shots

tasktemplates = [i['code'] for i in shotgun.sg.find('TaskTemplate',[],['code'])]



### check that the layout animatic is up-to-date

# find LO rushes and LO edits
lorushes = browser.episode(epname).folder('LOrushes')
loedits = browser.episode(epname).folder('LOedits')

# find most recent rush creaion date
for root,dirs,files in os.walk(lorushes):
    times = [ os.path.getmtime(os.path.join(root,i)) for i in files ]
    dirs[:] = [] # do not recurse
latest_rush = sorted(times)[-1]

# find most recent LO edit creation date
for root,dirs,files in os.walk(loedits):
    times = []
    for i in files:
        if i[-3:].upper() in ['MOV','MP4','AVI','MPG']:
            f = os.path.join(root,i)
            times.append( os.path.getmtime(f) )
    dirs[:] = [] # do not recurse
latest_edit = sorted(times)[-1]

# compare latest rush and edit dates
if latest_rush > latest_edit:
    all_problems_list.append(
        '**LAYOUT EDIT NOT UP-TO-DATE,'
        'NEWER RUSHES ARE AVAILABLE**\n'
        )



### cycle through layout shot folders to spot problems

for shot in shots:
    
    shot_problems = []
    sgbgs = shot.get('sg_background_asset_1')
    
    # Check that the shot is on shotgun
    if not shot.get('id'):
        shot_problems.append( 'Shot does not exist on Shotgun' )
        continue
    
    # Check for discrepencies between sg and lo background assignement
    if sgbgs:
        for sgbg in sgbgs:
            bgname = sgbg.get('name')
            if not find( shot['lopath'], bgname, weak = True ):
                msg = 'Shotgun BG not found in LO folder: '
                shot_problems.append(msg + assetlink(sgbg))
    
    # Look for undeclared background psd in lo 
    lobgs = find(shot['lopath'], '.psd', '.psb', subdirs=False)
    if lobgs:
        for lobg in lobgs:
            m = [True for i in sgbgs if i['name'].upper() == lobg['code'].upper()]
            if not m or not all(m):
                msg = 'PSD found but not declared on shotgun: '
                shot_problems.append(msg + link(lobg['code'], shot['lopath']))
    
    # Look for BGs imported in AE but not on SG:
    aebgpath = os.path.join( shot['lopath'], 'AE', '03_BG' )
    if os.path.exists( aebgpath ):
        aebgs = [os.path.splitext(i)[0] for i in os.listdir( aebgpath )]
        aebgs = [i for i in aebgs if i[:2].upper() == 'GB'] # filter out junk files
        if aebgs:
            for aebg in aebgs:
                m = [True for i in sgbgs if same_header(i['name'],aebg)]
                if not m or not all(m):
                    sglink = shotlink( {'code':'shotgun','id':shot['id']} )
                    msg = 'A BG was imported in AE but not declared on ' + sglink + ': '
                    shot_problems.append( msg + link(aebg,aebgpath))
    
    # check that the old script has not been used
    if find(shot['lopath'], 'exported', subdirs=False):
        shot_problems.append('layout has been exported with old script')
    
    # check if no background is assigned
    if not sgbgs:
        shot_problems.append('No BG assigned in shotgun: ' + shotlink(shot))
    
    # store all new bgs for later checking
    if sgbgs:
        for sgbg in sgbgs:
            if not bg_is_reused(epname, sgbg['name']):
                if sgbg not in backgrounds:
                    backgrounds.append(sgbg)
    
    if shot_problems:
        all_problems_list.append(
            '\n' +
            '**' + link(shot['code'],shot['lopath']) +':**\n\n' +
            '\n'.join( ['  * '+i for i in shot_problems] )
            )


### cycle through new shotgun backgrounds to spot problems

for sgbg in backgrounds:
    
    problems = [] 
    
    # retrieve additional info on SG
    x = shotgun.sg.find_one(
        'Asset',
        [['id','is',sgbg['id']]],
        ['code','sg_resolution','sg_background_type','description','tasks']
        )
    
    for i in x:
        if x[i] == None:
            x[i] = ''
    
    # check resolution information is there
    if (    x.get('sg_background_type', 'unset').upper() in ['BG3DMOVING','BG3DSTILL']
            and not x.get('sg_resolution')
            ):
        problems.append('Resolution info missing')

    # check bg type matches
    if (    x['sg_background_type'].upper() not in x['code'].upper()
            and sum([1 for i in shotgun.bgtypes if i.upper() in x['code'].upper()])
        ):
        problems.append('BG-type mismatch between name and field')
    
    # check if description is filled
    if  ( not ( x.get('description') and
                x['description'] in tasktemplates ) 
          and epname.upper() in x['code'].upper()
          and not x.get('tasks') ):
        problems.append('BG description (task template) not filled-in')
    
    if problems:
        all_problems_list.append(
            '\n' +
            '**' + assetlink( x ) +':**\n\n' +
            '\n'.join( ['  * '+i for i in problems] )
            )


if all_problems_list:
    
    # insert title on top
    title = epname + ' Layout Report'
    all_problems_list.insert(0, title + '\n' + '='*len(title) + '\n' )
    
    md = output( all_problems_list ) # write tmp markdown file
    rtf = pandoc( md, 'rtf' ) # convert to rtf doc
    os.system('start wordpad "' + rtf + '"') # open the doc
        
    # html = pandoc( md, 'html' )
    # os.system('start iexplore "' + html + '"')
    