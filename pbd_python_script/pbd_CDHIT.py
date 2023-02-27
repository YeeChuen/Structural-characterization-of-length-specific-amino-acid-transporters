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

#____________________________________________________________________________________________________
# functions/set ups 
    # TODO: write your functions here

def parser():
    # create a directory to store.
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, required=True) # fas path file to do CD-HIT on.

    args = parser.parse_args() 
    return args

def create_dir(addname, file_name):    
    newdir = addname+file_name
    track = 0
    if os.path.exists(newdir):
        temp = newdir + "_{}".format(str(track))
        while os.path.exists(temp):
            track += 1        
            temp = newdir + "_{}".format(str(track))
        newdir = temp
    return newdir

def main():
    # TODO: write your main here
    os.chdir("/work/ratul/chuen/sequence_structure_delineation")

    args = parser()

    fasfile = args.f
    a_temp = fasfile.split("/")
    directory_name = a_temp[0]
    file_name = a_temp[1]
    #remove .fas
    b_temp = file_name.split(".")
    file_name = b_temp[0]

    newdir = create_dir("cluster_", file_name)



    # always start the python to by bringing it to the main directory.
    pass

#____________________________________________________________________________________________________
# main 
if __name__ == "__main__":
    # TODO: change your python script title
    print("\n-------------------- START of \"<python_script.py>\" script --------------------")
    main()
    print("-------------------- END of \"<python_script.py>\" script --------------------\n")