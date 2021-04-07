#!/bin/bash

asetup AthGeneration,21.6.58,here
THEDIR=$2 # Old directory was: noGridpack_noShowering
THERUNNUMBER=999999
THEJO=$1 # Example is: mc.aMC_ppToHj_SMEFTatNLO_Nominal.py

GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ ! -d SMEFTatNLO ]; then
    echo -e ${GREEN} Downloading SMEFTatNLO. ${NC};
    wget https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/SMEFTatNLO/SMEFTatNLO_v1.0.1.tar.gz
    tar -xzf SMEFTatNLO_v1.0.1.tar.gz
fi;

# Make sure that your model is in your python path (achieved via symbolic link)
# Apparently this directory should be empty!
echo -e ${GREEN} Linking files. ${NC};

mkdir -p $THEDIR/$THERUNNUMBER

cd $THEDIR;
ln -s ../SMEFTatNLO .
cd -;

cd $THEDIR/$THERUNNUMBER;
ln -s ../../$THEJO .
cd -;

# Test, SMEFT@NLO, no gridpack, on-the-fly
echo -e ${GREEN} Running Gen_tf.py, no gridpack, no showering ${NC};
cd $THEDIR;
echo -e ${GREEN} Running from directory ${PWD} ${NC};
Gen_tf.py --ecmEnergy=13000. --maxEvents=100 --firstEvent=1 --randomSeed=123456 --outputTXTFile=test_lhe_events --jobConfig=$THERUNNUMBER
cd -;

echo -e ${GREEN} Finished. ${NC};

