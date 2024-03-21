#!/bin/bash

#SBATCH --job-name=pi_serial
#SBATCH --account=open
#SBATCH --partition=open
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1G
#SBATCH --constraint=sc
#SBATCH --time=00:20:00
#SBATCH --output=out/slurm-%x.out
#SBATCH --error=out/slurm-%x.err

module load anaconda
conda activate optjobs_env

python pi_serial.py > out/pi_serial.out
