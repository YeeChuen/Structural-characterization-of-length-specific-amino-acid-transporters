# Author/s: Yee Chuen Teh
# Title: pbd_muscle_one.py (update 2/8/2023)
# Project: Chowdhury Lab Viral Escape research
# Description: this script mainly to do MUSCLE alignment one protein at a time.
# Reference:
'''
TODO: write your reference here
'''

#____________________________________________________________________________________________________
# imports 
    # TODO: write your imports here
import os
from tqdm import tqdm
import time
import argparse

#____________________________________________________________________________________________________
# set ups 
    # TODO: write your functions here
def to_list(file):
    list = []
    with open(file, 'r') as f:
        text = f.read()
        text_list = text.split("\n")
        for t in text_list:
            list.append(t)
        list.pop()
        return list

def get_name(description):
    n_list = description.split("|")
    name = n_list[0]
    truename = name.replace(">","")
    return truename

def generate_fas(target_list, all_list, target):
    for i in tqdm(range(0, len(all_list)),
               desc="Generating individual alignment...",
               ascii=False, ncols=75):
        if i%2 != 0:
            continue
        with open(get_name(target_list[target])+"_align_{}".format(get_name(all_list[i])), 'a') as f:
            f.write(target_list[target]+"\n")
            f.write(target_list[target+1]+"\n")
            f.write(all_list[i]+"\n")
            f.write(all_list[i+1]+"\n")
        time.sleep(0.001)

def run_muscle(path, name, save_path, target_name):
    # this function run in the output directory
    fas_list = os.listdir(path)

    for i in range(len(fas_list)):
        os.system('muscle -super5 {}/{} -output {}_MSA_{}'.format(path,fas_list[i],name,str(fas_list[i])[-6:]))

    msa_list = os.listdir(os.getcwd())
    msa_name = 'Muscle_{}'.format(name)

    

    with open(msa_name, 'a') as m:
        for i in range(len(msa_list)):
            p_name = ""
            p_sequence = ""
            with open(msa_list[i], 'r') as n:
                n_whole = n.read()
                n_list = n_whole.split("\n")
                n_list.pop()
                pause = False
                for n in n_list:
                    if n[0] == ">":
                        if get_name(n) == target_name:
                            pause = True
                        else:
                            pause = False
                        if pause == False:
                            p_name = n
                    elif pause == False:
                        p_sequence += n
            m.write(p_name+"\n")
            m.write(p_sequence+"\n")
    os.system('mv {} {}'.format(msa_name, save_path))

# target is an integer, determine which pbd to do alignment in
def prep_muscle(filename, target_list, all_list, target):
    target_name = get_name(target_list[target])

    isExist = os.path.exists(filename)
    path=os.getcwd()
    global save_path
    if not isExist:
        print("created file: {}".format(str(filename)))
        # Create a new directory because it does not exist
        os.makedirs(filename)
        save_path = path + "/" + filename
        os.chdir(save_path)
    else:
        name = filename.split("_")
        digit = name[len(name)-1]
        mainname = filename
        if digit.isdigit():
            name.pop()
            mainname = name[0]
            for i in range(1,len(name)):
                mainname = +"_"+name[i]
                
        track = 0
        filename = mainname+"_{}".format(str(track))
        isExist = os.path.exists(filename)
        while isExist:
            track+=1
            filename=mainname+"_{}".format(str(track))
            isExist = os.path.exists(filename)
        print("created file: {}".format(str(filename)))
        # Create a new directory because it does not exist
        os.makedirs(filename)
        save_path = path + "/"+ filename
        os.chdir(save_path)

    muscle_input = target_name+"_input"
    isExist = os.path.exists(muscle_input)
    if not isExist:
        print("created file: {}".format(str(muscle_input)))
        # Create a new directory because it does not exist
        os.makedirs(muscle_input)
        new_path = save_path + "/" + muscle_input
        os.chdir(new_path)

        # now generate your new MSA in here
        generate_fas(target_list, all_list, target)
        os.chdir(save_path)

    # after generating the individual fas file run muscle in each of them
    muscle_output = target_name+"_output"
    isExist = os.path.exists(muscle_output)
    if not isExist:
        print("created file: {}".format(str(muscle_output)))
        # Create a new directory because it does not exist
        os.makedirs(muscle_output)
        new_path = save_path + "/" + muscle_output
        os.chdir(new_path)
        
        input_path = save_path + "/" + muscle_input
        # execute MUSCLE in each fas in filename
        run_muscle(input_path, get_name(target_list[target]), save_path, target_name)
        os.chdir(save_path)
    
    os.chdir(path)

def main():
    #initiate argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', type=str, required=True) # fas path for all to be align
    parser.add_argument('--t', type=str, required=True) # fas path for one to be align (target file, long or short)
    parser.add_argument('--f', type=str, required=True) # final file name
    parser.add_argument('--i', type=int, required=True) # index of the target protein in target file
    
    args = parser.parse_args() 


    file_target = args.t
    file_all = args.a
    file_name = args.f
    target = args.i

    target_list = to_list(file_target)
    all_list = to_list(file_all)

    prep_muscle(file_name, target_list, all_list, target)
    pass

#____________________________________________________________________________________________________
# main 
if __name__ == "__main__":
    print("\n-------------------- START of \"<pbd_muscle_one.py>\" script --------------------")
    # TODO: write your code here
    main()
    print("-------------------- END of \"<pbd_muscle_one.py>\" script --------------------\n")
