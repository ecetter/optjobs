#!/bin/bash

#SBATCH --job-name=pi_parallel
#SBATCH --account=open
#SBATCH --partition=open
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4
#SBATCH --mem=1G
#SBATCH --constraint=sc
#SBATCH --time=00:20:00
#SBATCH --output=out/slurm-%x.out
#SBATCH --error=out/slurm-%x.err

module load anaconda/2023 intel
conda activate optjobs_env

srun python pi_parallel.py > out/pi_parallel.out
