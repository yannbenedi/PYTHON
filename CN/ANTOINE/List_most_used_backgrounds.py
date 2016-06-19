from gumball import shotgun, gui, paths
import os


####################################################################


def output( plist ):
    ''' Compiles the master problem list into a markdown file,
    return its location '''
               
    # create new file
    tempmd = os.path.join(os.environ['TMP'], 'rlptemp.md')
    while os.path.isfile(tempmd):
        os.remove(tempmd)
    
    # write the file
    with open(tempmd,'w') as f:
        f.write( '\n\n'.join( plist ) )
    
    return tempmd

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


##############################################################################


filters = [['sg_asset_type','is','Background']]
fields = ['shot_sg_background_asset_1_shots','code']
backgrounds = shotgun.sg.find('Asset',filters,fields)

for bg in backgrounds:
    bg['count'] = len(bg['shot_sg_background_asset_1_shots'])
    
sorted_bgs = sorted(backgrounds, key=lambda k: k['count'], reverse = True)[:100]

fileoutput = output( [assetlink(i) for i in sorted_bgs] )
rtf = pandoc( fileoutput, 'rtf' )
os.system('start wordpad "' + rtf + '"')

