# Author/s: Yee Chuen Teoh          (Author that contribute to the script)
# Title: TODO:                      (the name of the script)
# Project: TODO: project title      (the main project name, what project this script is apart of?)
# Description: TODO: Description    (summary of what the script does)
# Reference:
'''
TODO: write your reference here
Usage:
    python pbd_CDHIT.py --f PoreDB_nonRNA/PoreDB_nonRNA_le1000.fas
'''
# Updates:  (date)
'''
TODO: write your updates here
mm/dd/yyyy
    - creation of the script
'''

#____________________________________________________________________________________________________
# imports 
    # TODO: write your imports here
import argparse
import os
import sys
import subprocess


#____________________________________________________________________________________________________
# functions/set ups 
    # TODO: write your functions here

def parser():
    '''
    get parser argument.
    '''
    # create a directory to store.
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, required=True) # fas path file to do CD-HIT on.

    args = parser.parse_args() 
    return args

def create_dir(addname, file_name):   
    '''
    addname: a string, to add to the title of the new directory
    file_name: some other dataset file_name, added to create the new directory.
    ''' 
    newdir = addname+file_name
    track = 0
    if os.path.exists(newdir):
        temp = newdir + "_{}".format(str(track))
        while os.path.exists(temp):
            track += 1        
            temp = newdir + "_{}".format(str(track))
        newdir = temp
    os.makedirs(newdir)
    print("new directory created with name: {}".format(newdir))
    print("in {}".format(os.getcwd()))
    return newdir

def main():
    # TODO: write your main here
    os.chdir("/work/ratul/chuen/sequence_structure_delineation")

    args = parser()

    # get file name
    fasfile_loc = args.f
    a_temp = fasfile_loc.split("/")
    directory_name = a_temp[0]
    file_name = a_temp[1]
    #remove .fas
    b_temp = file_name.split(".")
    file_name = b_temp[0]

    # create new directory
    newdir = create_dir("cluster_", file_name)

    # move to new directory, but save current path.
    currdir = os.getcwd()
    move_to_newdir = currdir +"/"newdir
    os.chdir(move_to_newdir)

    # do CD-HIT here.

    # Define the CD-HIT command with arguments
    cdhit_command = "cd-hit -i {} -o cd-hit_{} -c 0.9".format(fasfile_loc, file_name)

    # Run the CD-HIT command
    subprocess.run(cdhit_command)

    # always start the python to by bringing it to the main directory.
    pass

#____________________________________________________________________________________________________
# main 
if __name__ == "__main__":
    # TODO: change your python script title
    print("\n-------------------- START of \"<python_script.py>\" script --------------------")
    main()
    print("-------------------- END of \"<python_script.py>\" script --------------------\n")