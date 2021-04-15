#!/bin/bash

# asetup AthGeneration,21.6.57,here
THEDIR=$2 # Old directory was: run_batchFromGridpack
THERUNNUMBER=999999
THEJO=$1 # Example is: mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py

GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ ! -d SMEFTatNLO ]; then
    echo -e ${GREEN} Downloading SMEFTatNLO. ${NC};
    wget https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/SMEFTatNLO/SMEFTatNLO_v1.0.1.tar.gz
    tar -xzf SMEFTatNLO_v1.0.1.tar.gz
fi;

# Make the directory, copy submit and run files there.
mkdir -p $THEDIR

cp batchrunNoGridpack $THEDIR/.
cp submit $THEDIR/.

cd $THEDIR
echo condor_submit submit THEDIR=$THEDIR THEJO=$THEJO EXECUTABLE=batchrunNoGridpack
condor_submit submit THEDIR=$THEDIR THEJO=$THEJO EXECUTABLE=batchrunNoGridpack
cd -
echo -e ${GREEN} Submitted. ${NC};

echo -e ${GREEN} Done. ${NC};
