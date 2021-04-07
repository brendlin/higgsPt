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
They should by run e.g. using the command/arguments `source run_X.py MyJO.py outputDir`.

| Script | Example working JO (Argument 1) | Description |
| ------ | ---------------- | ----------- |
| `source run_noGridpack_noShowering.sh JO.py outDir` | mc.aMC_ppToHj_SMEFTatNLO_Nominal.py | Run without gridpack or showering |
| `source run_noGridpack_Pythia8.sh JO.py outDir` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_Nominal.py | Run without gridpack, but interface to Pythia8 |
| `source run_makeGridpack_Pythia8.sh JO.py outDir` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py | Make gridpack (with Pythia8) |
| `source run_generateFromGridpack_Pythia8.sh JO.py outDir` | &nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" | Run from gridpack generated from above |

Currently the best available option is the two-step option: make a gridpack, and then generate events from it.

Madgraph Reweighting
=========

For more information and some reweight_card generation examples, see
[Reweight Cards in Athena](https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/MadGraph5aMCatNLOreweight) as well as the
[Madgraph Webpage](https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Reweight#Contentofthereweight_card).

Setting a Single Operator
----------
If you want to set a *single* operator to a different value (which technically is not using the reweighting functionality), you can set the operator value
in the `extras` argument of `build_run_card`, e.g. to set the `ctG` operator to -0.6, you can specify in the JO file:

```python
extras = { ...,
    'DIM62F' : {'ctG':'-0.6'}
}
...
build_run_card(..., extras=extras)
```

