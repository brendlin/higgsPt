#!/bin/bash

rivet-build RivetAnalysis.so HiggsFullPhaseSpace.cc
athena RivetAnalysis.py -c 'directory="../MG_athena/run_generateFromGridpack"; filename="EVNT.root"'

$AthGeneration_DIR/src/Generators/Rivet_i/share/example/convert2root Rivet.yoda
