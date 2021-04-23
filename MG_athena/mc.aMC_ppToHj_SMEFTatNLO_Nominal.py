from MadGraphControl.MadGraphUtils import *

# PDF base fragment
from MadGraphControl.MadGraph_NNPDF30NLO_Base_Fragment import *

nevents = runArgs.maxEvents*1.1 if runArgs.maxEvents>0 else 1.1*evgenConfig.nEventsPerJob

process="""
import model SMEFTatNLO-NLO
generate p p > H j QED=1 QCD=3 NP=2 [QCD]
output -f"""

process_dir = new_process(process)

#Fetch default NLO run_card.dat and set parameters
settings = {
    #'parton_shower':'PYTHIA8',
    'nevents':int(nevents)
}
modify_run_card(process_dir=process_dir,runArgs=runArgs,settings=settings)

generate(process_dir=process_dir,runArgs=runArgs)
arrange_output(process_dir=process_dir,runArgs=runArgs,lhe_version=3,saveProcDir=True)  

evgenConfig.generators = ["aMcAtNlo"]

############################
# Shower JOs will go here
theApp.finalize()
theApp.exit()
