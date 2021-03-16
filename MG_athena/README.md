How to run Madgraph with Athena and SMEFT@NLO
=============

Setup
---------

asetup AthGeneration,21.6.58,here

Running
---------

A few simple "warmup" scripts have been added to validate that the process is working.

| Script | Corresponding JO | Description |
| ------ | ---------------- | ----------- |
| `source run_noGridpack_noShowering.sh` | mc.aMC_ppToHj_SMEFTatNLO_Nominal.py | Run without gridpack or showering |
| `source run_noGridpack_Pythia8.sh` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_Nominal.py | Run without gridpack, but interface to Pythia8 |
| `source run_makeGridpack_Pythia8.sh` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py | Make gridpack (with Pythia8) |
| `source run_generateFromGridpack_Pythia8.sh` | &nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" | Run from gridpack generated from above |

