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

Note that **the gridpack mode still crashes when used in conjunction with madgraph reweighting** (typically JobOptions with _RW in the name).

Batch Running
---------

You can run on the NAF batch in two ways: either running the full job on the batch system, or by generating (locally) a gridpack first and
then running on the batch system while pointing to that gridpack. **Note that the gridpack mode still crashes when used in conjunction with madgraph reweighting**, so the full-job running
is currently the only option there.

| Script | Example working JO (Argument 1) | Description |
| ------ | ---------------- | ----------- |
| `source run_batchNoGridpack.sh JO.py outDir` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_Nominal.py | Run without generating an intermediate gridpack |
| `source run_batchGenerateFromGridpack.sh JO.py outDir` | mc.aMCPy8EG_ppToHj_SMEFTatNLO_GridPack.py | Run from gridpack generated from a (local) run. **Not yet working with reweighting** |

Madgraph Reweighting
=========

For more information and some reweight_card generation examples, see
[Reweight Cards in Athena](https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/MadGraph5aMCatNLOreweight) as well as the
[Madgraph Webpage](https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/Reweight#Contentofthereweight_card).

Using Built-in Madgraph Reweighting cards
----------

To use the Madgraph built-in reweight functionality to generate different operator weights, you can add the following type of text to the JO.py file (AFTER the `modify_run_card` call but BEFORE the `generate` call):

```
# Add reweight card
rcard = open('reweight_card.dat','w')

reweightCommand = \
"""
launch --rwgt_name=ctG_m1p0_ctp_m1p0
    set DIM62F ctG -1.0
    set DIM62F ctp -1.0
launch --rwgt_name=ctG_m1p0_ctp_0p0
    set DIM62F ctG -1.0
    set DIM62F ctp 0.0
"""

rcard.write(reweightCommand)
rcard.close()
subprocess.call('cp reweight_card.dat ' + process_dir+'/Cards/', shell=True)
```

For this to work, of course all parameters which are to be reweighted must not be 0 during the original generation. Also, MadGraph fixes parameters and does not allow them to be reweighted if they are set to either 0 or 1 in the restriction card. To circumvent this, either set the parameters to an arbitrary value in the restriction card, or set them to 9.999999e-01 - the latter will be treated by MadGraph as a mutable value of 1.

Note that this **currently does not work with the two-step gridpack generation process**.

**To automatically generate the code for a complex scan, you can modify `ParameterScanExample.py` to generate the scan points that you want.**

Setting a Single Operator ("Roger's Method")
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

