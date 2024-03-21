#!/bin/bash

NODEFILE="$(pwd)/slurmhosts.$SLURM_JOB_ID.txt"
srun /bin/hostname -s &> $NODEFILE
cat $NODEFILE
