import os
import shutil
import datetime
import sys
import time

clear = lambda: os.system('cls')

# ASK BEFORE CREATING FOLDER

print "\n--- 3D BG prop create template folder ---"

def auto_prop_folder():
    # Ask for prop name and create folder in library

    # Set Paths
    lib_folder_root = r'C:\YANNB\WORK\PYTHON\GB'    # update BG 3D prop root folder path
    template_folder = lib_folder_root + "\Template" # update BG 3D prop template folder name
    library_bg_folder = lib_folder_root + "\lib"    # update BG 3D prop folder name


    def get_prop_name():

        # using user input for now, may change that later
        msg = '\n Type the name of the BG3D prop you want to create. \n'
        prop_name = raw_input(msg)

        return prop_name


    def copytemplate( prop_name ):

        #check if props folder is already created

        prop_folder = os.path.join(library_bg_folder, prop_name)

        # Check if prop folder already exist
        if not os.path.exists( prop_folder ):
            clear()
            print "\n Create folder: \n" + prop_folder
            shutil.copytree( template_folder, prop_folder )
            return prop_folder
        else:
            clear()
            print "\n  " + prop_name + " already exists in 3D BG library , choose another name"
            print ""
            print "\n " + prop_folder
            time.sleep(4)
            sys.exit()


    def write_infotxt( prop_folder):

        # Template .txt file to update with user input

        filename= prop_folder + "\scenes\info.txt"
        namespace_search = 'namespace:' # update with namespace in txt, update the info.txt in template as well

        # List of folders to check if asset already exists
        list_folder = ["libRigging","libShading","libShadingSoi"] # update other folder check name


        # If already exist from the list, ask user which username to pick

        def extract_actual_namespace(library_folder):
            """
            :param library_bg_folder: root path of an asset
            :return: return the namespace of the indicated folder
            """
            with open(library_folder, 'r') as rofile:
                for line in rofile:
                    if line.strip() == namespace_search:
                        for _ in xrange(1):  # get the next line
                            namespace = rofile.next()
                            return namespace

        # Check existing namespace of the actual asset and display the list to choose

        existing_asset =[]
        existing_namespace =[]
        count = 0

        for check_folder in list_folder:
            library_folder = r'%s\%s\%s\scenes\info.txt' %(lib_folder_root,check_folder, prop_name)
            if os.path.exists( library_folder ):
                count +=1
                namespace_extract = extract_actual_namespace(library_folder)
                print ""
                print " -" + str(count)+ ": " + namespace_extract  + check_folder
                existing_asset.append(check_folder)
                existing_namespace.append(namespace_extract)

        # if asset doesn't exist in other directory, ask for namespace

        if len(existing_namespace) == 0:
            namespace = raw_input('\n Type prop namespace:')
        else:
            select_lib_folder = raw_input('\n Pick the namespace you want to use \n Type the number: ')
            user_pick = int(select_lib_folder) -1
            namespace = existing_namespace[user_pick]

        clear()
        description = raw_input('\n Type prop description you want to display in the asset loader:')
        user = os.getenv('username')
        creation_date = str(datetime.datetime.now())
        maya_scene = prop_name + '_v001.ma'

        # Replace content of .txt with user input
        with open(filename, 'r') as f:
          text = f.read()

        text = text.replace('maya_scene_tmp', maya_scene)
        text = text.replace('namespace_tmp', namespace)
        text = text.replace('description_tmp', description)
        text = text.replace('prop_creator_tmp', user)
        text = text.replace('date_tmp', creation_date)

        with open(filename, 'w') as f:
          f.write(text)

    # execution

    prop_name = get_prop_name()
    prop_folder = copytemplate( prop_name )
    write_infotxt( prop_folder )

    # Open newly created folder
    clear()
    print "\n -" + prop_name + "- 3D BG prop folder has been successfully created"
    time.sleep(2)
    os.startfile(prop_folder)

auto_prop_folder()