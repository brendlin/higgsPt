How to run Madgraph with Athena and SMEFT@NLO
=============

For more information on generators in Athena, see the [PmgMcSoftware twiki](https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/PmgMcSoftware)
(which includes important information on valid/blacklisted release versions).

The twiki for Madgraph with Athena is here: [MadGraph5aMCatNLOForAtlas](https://twiki.cern.ch/twiki/bin/view/AtlasProtected/MadGraph5aMCatNLOForAtlas).

Setup
---------

No setup is required; asetup is done inside the source files.

Running
---------

A few simple "warmup" scripts have been added to validate that the process is working.

| Script | Corresponding JO | Description |
| ------ | ---------------- | ----------- |
| `source run_noGridpack_noShowering.sh` | mc.aMC_ppToHj_SMEFTatNLO_Nominal.py | Run without gridpack or showering |
| `source run_noGridpack_Pythia8.sh` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_Nominal.py | Run without gridpack, but interface to Pythia8 |
| `source run_makeGridpack_Pythia8.sh` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py | Make gridpack (with Pythia8) |
| `source run_generateFromGridpack_Pythia8.sh` | &nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" | Run from gridpack generated from above |

Currently the best available option is the two-step option: make a gridpack, and then generate events from it.

Madgraph Reweighting
-------

For more information and some reweight_card generation examples, see
[Reweight Cards in Athena](https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/MadGraph5aMCatNLOreweight) as well as the
[Madgraph Webpage](https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Reweight#Contentofthereweight_card).
