Rivet in Athena
===========
For more general information on the use of Rivet in Athena, see [Generators/Rivet_i](https://gitlab.cern.ch/atlas/athena/-/tree/21.6/Generators/Rivet_i).

How to run Rivet with Athena on output EVNT.root files
============

First, make sure you have successfully produced an EVNT.root file
using Madgraph interfaced to Athena. Then proceed with the following steps.

Setup
---------
```bash
asetup 21.6.57,AthGeneration
source setupRivet.sh # This does not look like it should work, but it does
ln -s ../madgraphsetup/Rivet/HiggsDiphotonFiducialCrossSectionAnalysis2020.cc .
```

Running
---------

This takes in an EVNT.root file, and spits out a Yoda file. One question you may ask is,
"Is there a way to automatically create a root file instead of a Yoda file during the athena
running" ? The answer is "no" -- it used to be possible, but due to an update in Yoda histogram
naming that was not propagated to `Generators/Rivet_i/src/Rivet_i.cxx`, the root histograms will
simply not show up, without throwing any warning. See below for how to convert a yoda file to a
root histogram file.

```
rivet-build RivetAnalysis.so HiggsFullPhaseSpace.cc
athena RivetAnalysis.py -c 'directory="../MG_athena/run_generateFromGridpack"; filename="EVNT.root"'
```

Converting output to a Root File
----------

```bash
$AthGeneration_DIR/src/Generators/Rivet_i/share/example/convert2root Rivet.yoda
```
