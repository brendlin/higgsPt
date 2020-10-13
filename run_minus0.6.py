from MadGraphControl.MadGraphUtils import *

nevents_x=10000
test=[999999]
gridpack_mode=True
runName='run_minus0.6'

gridpack_dir='madevent/'

    #import model loop_sm_yukawa_b_lowMass
fcard = open('proc_card_mg5.dat','w')
fcard.write("""
    import model SMEFTatNLO_U2_2_U3_3_cG_4F_LO_UFO-HHloop
    generate p p > H j NP=2 QCD=3 QED=1 [QCD] 
    output -f""")
fcard.close()


beamEnergy=-999
if hasattr(runArgs,'ecmEnergy'):
    beamEnergy = runArgs.ecmEnergy / 2.
else: 
    raise RuntimeError("No center of mass energy found.")


process_dir = new_process(grid_pack=gridpack_dir)
extras = { 'lhe_version':'2.0', 
           'cut_decays':'F', 
           'pdlabel':"'nn23lo1'",
           'use_syst':"False",
           'DIM62F' : {'ctG':'-0.6' }  
}
    


build_run_card(run_card_old=get_default_runcard(proc_dir=process_dir),run_card_new='run_card.dat', 
              #rand_seed=runArgs.randomSeed,beamEnergy=beamEnergy,extras=extras)
              nevts=nevents_x,rand_seed=runArgs.randomSeed,beamEnergy=beamEnergy,extras=extras)

print_cards()
from shutil import copyfile

copyfile(os.environ['MADPATH']+'/Template/loop_material/StandAlone/Cards/MadLoopParams.dat',process_dir+'/Cards/MadLoopParams_default.dat')

os.environ['FC'] = 'gfortran'

generate(run_card_loc='run_card.dat',param_card_loc=None,mode=0,njobs=1,proc_dir=process_dir,run_name=runName,
         #grid_pack=gridpack_mode,gridpack_dir=gridpack_dir,random_seed=runArgs.randomSeed)
         grid_pack=gridpack_mode,gridpack_dir=gridpack_dir,nevents=nevents_x,random_seed=runArgs.randomSeed)

arrange_output(run_name=runName,proc_dir=process_dir,outputDS=runName+'._00001.events.tar.gz',lhe_version=3,saveProcDir=True)



