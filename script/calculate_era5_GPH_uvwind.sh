#!/bin/bash
#SBATCH --account=def-tgan
#SBATCH --ntasks=1               # number of MPI processes
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=16384M      # memory; default unit is megabytes
#SBATCH --time=1:00:00           # time (DD-HHMM)
#SBATCH --mail-user=huangzq681@gmail.com
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE
#SBATCH --mail-type=ALL

module load python/3.9.6
module load scipy-stack
source ~/hzqENV/bin/activate

cd $PBS_O_WORKDIR
cd /home/xtan/scratch/hzq/reanalysis/era5_newversion

echo "Current working directory is `pwd`"
echo "Running on hostname `hostname`"
echo "Starting run at: `date`"
python calculate_era5_GPH_uvwind.py

echo "Program diffuse finished with exit code $? at: `date`"
