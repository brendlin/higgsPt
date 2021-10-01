#!/bin/bash

THEDIR=$2 # old directory was run_generateFromGridpack
THERUNNUMBER=999999
THEJO=$1 # Example is mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py

TMP=${THEJO/mc\./mc_13TeV\.}
THEGRIDPACK=${TMP/\.py/\.GRID\.tar\.gz}
THEGRIDPACKDIR=${THEDIR/generateFrom/make}

GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ ! -d SMEFTatNLO ]; then
    echo -e ${GREEN} Downloading SMEFTatNLO. ${NC};
    wget https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/SMEFTatNLO/SMEFTatNLO_v1.0.1.tar.gz
    tar -xzf SMEFTatNLO_v1.0.1.tar.gz
fi;

# Test to make sure that the gridpack exists!
echo  -e ${GREEN} Checking for Gridpack $THEGRIDPACKDIR/$THEGRIDPACK ${NC};
if [ ! -f $THEGRIDPACKDIR/$THEGRIDPACK ]; then
    echo  -e ${GREEN} Could not find Gridpack $THEGRIDPACKDIR/$THEGRIDPACK. Stopping. ${NC};
else
    # Make sure that your model is in your python path (achieved via symbolic link)
    # Apparently this directory should be empty!
    echo -e ${GREEN} Linking files. ${NC};

    mkdir -p $THEDIR/$THERUNNUMBER

    cd $THEDIR;
    ln -s ../SMEFTatNLO .
    cd -;

    cd $THEDIR/$THERUNNUMBER;
    ln -s ../../$THEJO .
    ln -s ../../$THEGRIDPACKDIR/$THEGRIDPACK .
    cd -;

    # Test, SMEFT@NLO, no gridpack, on-the-fly
    echo -e ${GREEN} Running Gen_tf.py, generating gridpack ${NC};
    cd $THEDIR;
    asetup AthGeneration,21.6.73,here
    echo -e ${GREEN} Adding $(pwd) to PYTHONPATH.${NC};
    export PYTHONPATH=`pwd`:$PYTHONPATH
    echo -e ${GREEN} Running from directory ${PWD} ${NC};
    Gen_tf.py --ecmEnergy=13000. --maxEvents=5000 --firstEvent=1 --randomSeed=123456 --outputEVNTFile=EVNT.root --jobConfig=$THERUNNUMBER
    cd -;
fi;

echo -e ${GREEN} Finished. ${NC};
