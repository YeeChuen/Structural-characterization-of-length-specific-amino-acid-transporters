# Author/s: Yee Chuen Teoh          (Author that contribute to the script)
# Title: TODO:                      (the name of the script)
# Project: TODO: project title      (the main project name, what project this script is apart of?)
# Description: TODO: Description    (summary of what the script does)
# Reference:
'''
TODO: write your reference here
Usage:

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
    '''
    get parser argument.
    '''
    # create a directory to store.
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, required=True) # fas path file to do CD-HIT on.

    args = parser.parse_args() 
    return args

def main():
    # TODO: write your main here
    work_dir = "/work/ratul/chuen/sequence_structure_delineation"
    os.chdir(work_dir)
    # always start the python to by bringing it to the main directory.

    args = parser()
    
    pass

#____________________________________________________________________________________________________
# main 
if __name__ == "__main__":
    # TODO: change your python script title
    print("\n-------------------- START of \"<python_script.py>\" script --------------------")
    main()
    print("-------------------- END of \"<python_script.py>\" script --------------------\n")