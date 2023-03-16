# Author/s: Yee Chuen Teoh          (Author that contribute to the script)
# Title: pbd_CDHIT_compare.py                  (the name of the script)
# Project: Chowdhury Lab Sequence Structure Dealineation      (the main project name, what project this script is apart of?)
# Description: TODO: Description    (summary of what the script does)
# Reference:
'''
TODO: write your reference here
Script Idea:
    1. get true member and least member in the cluster, put them as ordered pair
        - index 0: true member
        - index 1: least member
    2. get all the protein in the dataset as a list,
        - even number index: protein description
        - odd number index: protein sequence
    3. 

Usage:
    python pbd_CDHIT_compare.py --cf cluster_PoreDB_nonRNA_le1000/cd-hit_PoreDB_nonRNA_le1000.clstr --df PoreDB_nonRNA/PoreDB_nonRNA_le1000.fas 
'''
# Updates:  (date)
'''
TODO: write your updates here
02/27/2023
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
    parser.add_argument('--cf', type=str, required=True) # .clstr file path file to do CD-HIT on.
    parser.add_argument('--df', type=str, required=True) # .fas dataset file path file to do CD-HIT on.

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
    print("\n-------------------- START of \"<pbd_CDHIT_compare.py.py>\" script --------------------")
    main()
    print("-------------------- END of \"<pbd_CDHIT_compare.py.py>\" script --------------------\n")