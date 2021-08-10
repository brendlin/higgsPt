High-p<sub>T</sub> Higgs Project
========

Checking out the Code
---------

```bash
git clone --recursive ssh://git@gitlab.cern.ch:7999/brendlin/higgspt.git
```

Reading Material
========

Our ATLAS Talks
---------
 - Nils' talk at HComb, July 21, 2021, "Interpretation of high-pTH regime": https://indico.cern.ch/event/1044657/

Theory
---------
 - Original paper, "Boosted Higgs Shapes": [arXiv:1405.4295](https://arxiv.org/pdf/1405.4295.pdf)
 - Grazzini et al: [arXiv:1612.00283](https://arxiv.org/abs/1612.00283)
 - Grazzini et al: [arXiv:1806.08832](https://arxiv.org/abs/1806.08832)

Experimental
---------
 - CMS differential interpretation: [arXiv:1812.06504](https://arxiv.org/abs/1812.06504)
 - H→γγ Couplings @139 fb<sup>–1</sup> (in progress) [ANA-HIGG-2020-16-INT1](https://cds.cern.ch/record/2712570)
    - Uses SMEFTsim and SMEFT@NLO in an EFT fit approach
    - Effect of operators is parameterized, applied as a correction to the SM prediction
    - Discussion of parameterization of Higgs boson decay widths
 - H→γγ differential interpretation @140 fb<sup>-1</sup>: [CDS](https://cds.cern.ch/record/2655119/files/ATL-COM-PHYS-2019-039.pdf)
    - Uses SMEFTsim in an EFT fit approach
    - Uses both SILH and Warsaw basis
    - Uses Professor method for interpolation
 - H→γγ Couplings @36 fb<sup>–1</sup> [arXiv:1802.04146](https://arxiv.org/pdf/1802.04146.pdf)
    - Section 9.5.8: description of EFT fit
    - Uses the Professor method for interpolation
    - Discussion of Higgs boson decay width using the MG5_aMC@NLO partial width calculator
 - High-pt H→bb Moriond 2021 analysis:
    - Includes some description of MoReHqT, though incomplete
    - See the supporting note: [ATL-COM-PHYS-2019-1425](https://cds.cern.ch/record/2703097/files/ATL-COM-PHYS-2019-1425.pdf)

Professor
--------
 - Code is available here: https://professor.hepforge.org/
 - See previous section for examples of ATLAS results that use Professor
 - Link to paper: [arXiv:0907.2973](https://arxiv.org/abs/0907.2973)


Madgraph resources
--------

 - Twiki page for using MadGraph5_aMC@NLO on ATLAS: https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/MadGraph5aMCatNLOForAtlas
 - A reference for the MadGraph5_aMC@NLO generator: [arXiv:1405.0301](https://arxiv.org/abs/1405.0301)
 - For loop-induced processes, also cite: [arXiv:1507.00020](https://arxiv.org/abs/1507.00020)
 - MadGraph issues in Jira:
   - [AGENE-1692](https://its.cern.ch/jira/browse/AGENE-1692)
   - [AGENE-1862](https://its.cern.ch/jira/browse/AGENE-1862)

SMEFT@NLO
--------
 - [Link to FeynRules](http://feynrules.irmp.ucl.ac.be/wiki/SMEFTatNLO)

Running the Code
========

Event generation (and subsequent plotting of histograms) is achieved in the following steps:
 - **Run Madgraph using the Athena interface.** This consists of three steps:
   - Generating a "Gridpack" (the integration step of Madgraph) -- note that this can either be a separate step, or run in the same job as the next step.
   - Using this Gridpack to generate discrete events (also with Madgraph) of LHE format
   - Taking LHE events and showering them with Pythia8 (to create a `EVNT.root` file)
   - For more information on this step, see `MG_athena/README.md`
 - **Run a Rivet routine on the output `EVNT.root` file.** This applies a truth selection and outputs histograms (in YODA format).
   - There is a simple script to convert a YODA file to a Root file.
   - For more information on this step, see `rivet/README.md`
