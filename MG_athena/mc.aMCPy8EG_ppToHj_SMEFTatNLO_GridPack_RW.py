#
# This file should serve as both the JO for *making* the Gridpack and subsequently *running*

from MadGraphControl.MadGraphUtils import *
import subprocess

# PDF base fragment
# Do we need NNPDF30NLO or NNPDF30NLOnf4 ?
import MadGraphControl.MadGraph_NNPDF30NLO_Base_Fragment

nevents = runArgs.maxEvents*1.1 if runArgs.maxEvents>0 else 1.1*evgenConfig.nEventsPerJob

# Indicate that we are in gridpack mode
gridpack_mode=True

# If we want to generate a new process for a gridpack, then we will make a new process.
# Otherwise, we will grab the existing gridpack from the gridpack location.
if not is_gen_from_gridpack():
    process="""
    import model SMEFTatNLO-NLO
    generate p p > H j QED=1 QCD=3 NP=2 [QCD]
    output -f"""

    process_dir = new_process(process)
else :
    process_dir = MADGRAPH_GRIDPACK_LOCATION

#Fetch default NLO run_card.dat and set parameters
settings = {
    'nevents':int(nevents),
    # 'reweight':'ON'
#    'store_rwgt_info':True
}
modify_run_card(process_dir=process_dir,runArgs=runArgs,settings=settings)

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
launch --rwgt_name=ctG_0p0_ctp_m1p0
    set DIM62F ctG 0.0
    set DIM62F ctp -1.0
launch --rwgt_name=ctG_0p0_ctp_0p0
    set DIM62F ctG 0.0
    set DIM62F ctp 0.0
"""

rcard.write(reweightCommand)
rcard.close()
subprocess.call('cp reweight_card.dat ' + process_dir+'/Cards/', shell=True)

generate(process_dir=process_dir,runArgs=runArgs,grid_pack=gridpack_mode)
arrange_output(process_dir=process_dir,runArgs=runArgs,lhe_version=3,saveProcDir=True)  

evgenConfig.description = 'aMcAtNlo_Hj'
evgenConfig.keywords+=['Higgs']

# Includes required for Pythia8 showering
include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
include("Pythia8_i/Pythia8_aMcAtNlo.py")

# Force the Higgs to decay to two Higgs photons
genSeq.Pythia8.Commands += [ '25:onMode = off',
                             '25:onIfMatch = 22 22' ]
