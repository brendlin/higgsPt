#!/bin/bash

# asetup AthGeneration,21.6.57,here
THEDIR=$2 # Old directory was: run_batchFromGridpack
THERUNNUMBER=999999
THEJO=$1 # Example is: mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py

TMP=${THEJO/mc\./mc_13TeV\.}
THEGRIDPACK=${TMP/\.py/\.GRID\.tar\.gz}
THEGRIDPACKDIR=${THEDIR/batchFrom/make}

GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Test to make sure that the gridpack exists!
echo  -e ${GREEN} Checking for Gridpack $THEGRIDPACKDIR/$THEGRIDPACK ${NC};
if [ ! -f $THEGRIDPACKDIR/$THEGRIDPACK ]; then
    echo  -e ${GREEN} Could not find Gridpack $THEGRIDPACKDIR/$THEGRIDPACK. Stopping. ${NC};
else
    # Make the directory, copy submit and run files there.
    mkdir -p $THEDIR
    cp submit $THEDIR/.

    cp batchrun $THEDIR/.
    cp submit $THEDIR/.

    cd $THEDIR
    echo condor_submit submit THEDIR=$THEDIR THEJO=$THEJO
    condor_submit submit THEDIR=$THEDIR THEJO=$THEJO 
    cd -
    echo -e ${GREEN} Submitted. ${NC};
fi;

echo -e ${GREEN} Done. ${NC};
