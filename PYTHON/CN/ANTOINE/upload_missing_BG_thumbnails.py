hcjfd8kffrom gumball import shotgun, browser, gui, imagetools as img
from pprint import pprint
import os
import re
import difflib

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


def bg_is_reused( epname, bgname ):
    ''' returns True or False '''
    
    m = re.match(
        'GB(\d{2,3})([a-z]*).*SC(\d{3}[a-z]?)',
        bgname,
        re.IGNORECASE
        )
    
    if m and m.groups()[1].upper() == epname.upper():
        del m
        return False
    else:
        del m
        return True

ep = gui.episode_prompt()
epname = ep.name


# find layout shot folders and match them with sg database
loscenes = ep.get_scenes('loapp')
loscenes = shotgun.ShotList(loscenes)


# list all bgs for these shots
backgrounds = []

for shot in loscenes:
    bgs = shot.get('sg_background_asset_1')
    if bgs:
        for bg in bgs:
            if not bg_is_reused( epname, bg['name'] ) and bg not in backgrounds:
                bg['code'] = bg['name']
                del bg['id']
                backgrounds.append(bg)
        

# match backgrounds on shotgun
backgrounds = shotgun.AssetList( backgrounds )

for bg in backgrounds:
    
    # skip this bg if it has a thumbnail or version
    if bg.get('image'):
        continue
        
    # get main shot folder for the backgrounds
    m = re.match( '.*_Sc(\d+[a-z]?)_.*', bg['code'], re.IGNORECASE )
    if m:
        scene = m.groups()[0]
    else:
        raise Exception, 'could not parse asset name ' + bg['code']
    
    scenefolder = ep.directory('loapp').scene( scene )
    
    # look for bg in this directory
    f = find( scenefolder, bg['code'], weak=True, subdirs=True )
    if f:
        f = [i for i in f if i['el_path'][-3:].upper() in ['JPG','MOV','MP4','AVI','MPG']]
    
    if f:
        preview = f[0]['el_path']
    else:
        continue
    
    
    # create a new shotgun version for this shot
    data = {
        'project': {'type':'Project','id': shotgun.projectId},
        'code' : bg['code'],
        'description':'uploaded by the gumball python API',
        'entity':{'type':'Asset', 'id':bg['id']}        
        }
    version = shotgun.sg.create( 'Version', data )
    
    
    # upload preview file to version
    if version:
        
        # re-encode videos it first (to avoid uploading massive playblasts...)
        if img.is_video( preview ):
            print 'Re-encoding ' + os.path.split(preview)[1] + ' ...'
            encoded = img.encode_720p( preview )
            while not os.path.isfile( encoded ):
                pass
            preview = encoded
        
        print 'Uploading   ' + os.path.split(preview)[1] + ' ...'
        result = shotgun.sg.upload(
            'Version',
            version['id'],
            preview,
            'sg_uploaded_movie'
            )