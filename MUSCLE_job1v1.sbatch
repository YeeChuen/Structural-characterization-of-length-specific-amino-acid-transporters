#!/bin/bash

# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename

#SBATCH --time=24:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=64   # 64 processor core(s) per node
#SBATCH --mem=64G   # maximum memory per node
#SBATCH --partition=huge    # huge node(s)
#SBATCH --job-name="MUSCLE_job"
#SBATCH --output="MUSCLE_job1v1_%j" # job standard output file (%j replaced by job id)

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE

cd /work/ratul/chuen/viralescape/step1_viralescape
module load miniconda3/4.10.3-svrr7oe
source activate viralescape_conda_env

python pbd_muscle_one.py --a PoreDB_nonRNA/PoreDB_nonRNA_le1000.fas --t PoreDB_nonRNA/PoreDB_nonRNA_eq1000.fas --f muscle_long --i 0

conda deactivate
module purge

