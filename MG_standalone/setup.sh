#!/bin/bash

##
## General setup
##
export TestArea=`pwd`
mkdir -p build;
lsetup "python 3.7.4-x86_64-centos7"
export LC_ALL="en_US.UTF-8"
TheMadgraphVersion='2.8.3.2'
TheMadgraphVersion_Underscore="${TheMadgraphVersion//\./_}"
LHAPDF_DATA_PATH=/cvmfs/sft.cern.ch/lcg/external/lhapdfsets/current
GREEN='\033[0;32m'
NC='\033[0m' # No Color

##
## One-time installation of six, for MadGraph
##
echo -e ${GREEN} Madgraph with Python3 requires the six module. Installing now. ${NC}
python3 -c "import six" || pip3 install six --user

##
## Download and untar Madgraph
## To run:
##  ./bin/mg5_aMC
##
cd $TestArea
if [ ! -d MG5_aMC_v${TheMadgraphVersion_Underscore} ]; then
    echo -e ${GREEN} Setting up Madgraph: downloading MG5_aMC_v${TheMadgraphVersion}.tar.gz ${NC};
    wget https://launchpad.net/mg5amcnlo/2.0/2.8.x/+download/MG5_aMC_v${TheMadgraphVersion}.tar.gz;
    tar -xzf MG5_aMC_v${TheMadgraphVersion}.tar.gz;
else
    echo -e ${GREEN} Madgraph version ${TheMadgraphVersion} found. ${NC}
fi;

##
## Download and build LHAPDF
##
if [ ! -f build/bin/lhapdf-config ]; then
    echo -e ${GREEN} Downloading lhapdf and connecting it to madgraph. ${NC}
    wget https://lhapdf.hepforge.org/downloads/?f=LHAPDF-6.3.0.tar.gz -O LHAPDF-6.3.0.tar.gz
    tar -xzf LHAPDF-6.3.0.tar.gz

    cd LHAPDF-6.3.0
    ./configure --prefix=$TestArea/build
    make
    make install
    cd -

    echo -e ${GREEN} Linking LHAPDF with Madgraph... ${NC}
    echo "lhapdf     = ${TestArea}/build/bin/lhapdf-config" >> MG5_aMC_v${TheMadgraphVersion_Underscore}/input/mg5_configuration.txt
    echo "lhapdf_py3 = ${TestArea}/build/bin/lhapdf-config" >> MG5_aMC_v${TheMadgraphVersion_Underscore}/input/mg5_configuration.txt
else
    echo -e ${GREEN} LHAPDF version already exists. ${NC}
fi

echo -e ${GREEN} Finished setting up. ${NC}
