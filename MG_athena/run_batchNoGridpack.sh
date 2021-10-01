#!/bin/bash

#
# Usage  : source run_batchNoGridpack.sh JO_FILE.py OUTPUTDIR NJOBS
# Example: source run_batchNoGridpack.sh mc.aMCPy8EG_ppToHj_SMEFTatNLO_Nominal.py outdir 20
# (Check the file "batchrunNoGridpack" for the nevents per job (typically 500)
#

# asetup AthGeneration,21.6.57,here
THEJO=$1 # Example is: mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py
THEDIR=$2 # Old directory was: run_batchFromGridpack
NJOBS=$3 # Check batchrunNoGridpack for the number of events per job (typically 500)
THERUNNUMBER=999999

GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ ! -d SMEFTatNLO ]; then
    echo -e ${GREEN} Downloading SMEFTatNLO. ${NC};
    wget https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/SMEFTatNLO/SMEFTatNLO_v1.0.1.tar.gz
    tar -xzf SMEFTatNLO_v1.0.1.tar.gz
    # Change cpG to be a small, non-zero value (to make it editable)
    sed -i 's/8 0.000000 # cpG/8 0.000001 # cpG/g' SMEFTatNLO/restrict_NLO.dat
fi;

# Make the directory, copy submit and run files there.
mkdir -p $THEDIR

# Make the output directories (e.g. job001), which will be populated by the batch jobs
for i in $(seq 0 $NJOBS ); do
    THEJOBDIR=job$(printf "%03d" $i);
    mkdir -p $THEDIR/$THEJOBDIR;
    mkdir -p $THEDIR/$THEJOBDIR/$THERUNNUMBER;
done;

# Make a copy of the job steering scripts
cp batchrunNoGridpack $THEDIR/.
cp submit $THEDIR/.

# Submit from the new directory that you created.
cd $THEDIR
echo condor_submit submit THEDIR=$PWD THEJO=$THEJO EXECUTABLE=batchrunNoGridpack NJOBS=$NJOBS
condor_submit submit THEDIR=$PWD THEJO=$THEJO EXECUTABLE=batchrunNoGridpack NJOBS=$NJOBS
cd - > /dev/null;
echo -e ${GREEN} Submitted. ${NC};
echo -e ${GREEN} Done. ${NC};
