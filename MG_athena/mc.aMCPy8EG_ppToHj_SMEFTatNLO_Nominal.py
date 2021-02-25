from MadGraphControl.MadGraphUtils import *

# PDF base fragment
# Do we need NNPDF30NLO or NNPDF30NLOnf4 ?
import MadGraphControl.MadGraph_NNPDF30NLO_Base_Fragment

nevents = runArgs.maxEvents*1.1 if runArgs.maxEvents>0 else 1.1*evgenConfig.nEventsPerJob

process="""
import model SMEFTatNLO-NLO
generate p p > H j QED=1 QCD=3 NP=2 [QCD]
output -f"""

process_dir = new_process(process)

#Fetch default NLO run_card.dat and set parameters
settings = {
    'nevents':int(nevents)
}
modify_run_card(process_dir=process_dir,runArgs=runArgs,settings=settings)

generate(process_dir=process_dir,runArgs=runArgs)
arrange_output(process_dir=process_dir,runArgs=runArgs,lhe_version=3,saveProcDir=True)  

evgenConfig.description = 'aMcAtNlo_Hj'
evgenConfig.keywords+=['Higgs']

# Includes required for Pythia8 showering
include("Pythia8_i/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
include("Pythia8_i/Pythia8_aMcAtNlo.py")

# Force the Higgs to decay to two Higgs photons
genSeq.Pythia8.Commands += [ '25:onMode = off',
                             '25:onIfMatch = 22 22' ]
