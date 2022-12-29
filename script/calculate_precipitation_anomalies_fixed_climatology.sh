#!/bin/bash
#SBATCH --account=def-tgan
#SBATCH --ntasks=1               # number of MPI processes
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=16384M      # memory; default unit is megabytes
#SBATCH --time=36:00:00           # time (DD-HHMM)
#SBATCH --output=R_%x.out
#SBATCH --mail-user=huangzq681@gmail.com
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE
#SBATCH --mail-type=ALL

module load python/3.8.2
source ~/hzqENV/bin/activate

cd $PBS_O_WORKDIR
cd /home/xtan/scratch/hzq/anomalous_PREC

echo "Current working directory is `pwd`"
echo "Running on hostname `hostname`"
echo "Starting run at: `date`"
python script/calculate_precipitation_anomalies_fixed_climatology.py

echo "Program diffuse finished with exit code $? at: `date`"
