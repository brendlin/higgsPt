theApp.EvtMax = -1

import os,sys
import glob

import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AppMgr import ServiceMgr as svcMgr

#svcMgr.EventSelector.InputCollections = ["/afs/cern.ch/user/s/sheim/public/ForRivetPackage/EVNT.05895633._000030.pool.root.1"]
#svcMgr.EventSelector.InputCollections = ["/afs/cern.ch/work/s/sheim/HZZ/CrossSections/Rivet/evgenfile/mc15_13TeV/EVNT.05550958._000201.pool.root.1"]

# See if a filename was specified, otherwise set to EVNT.root
try :
    tmp = filename
except NameError :
    filename = 'EVNT.root'

try :
    print 'Finding all files named %s in directory %s'%(filename,directory)
except NameError :
    print 'Usage: python RivetAnalysis.py',
    print '-c \'directory = "../path/to/location/of/basedir"; filename "EVNT.root"\''
    print '(e.g. the script will look for all files named e.g. EVNT.root inside of basedir)'
    print 'Exiting -- please try the usage described above.'
    sys.exit()

list_of_files = list(os.path.abspath(i) for i in glob.glob('%s/*%s'%(directory,filename)))
svcMgr.EventSelector.InputCollections = list_of_files
print svcMgr.EventSelector.InputCollections

from AthenaCommon.AlgSequence import AlgSequence
job = AlgSequence()

from Rivet_i.Rivet_iConf import Rivet_i
rivet = Rivet_i("Rivet")
rivet.AnalysisPath = os.environ['PWD']
rivet.Analyses += [ 'HiggsFullPhaseSpace' ]
rivet.RunName = 'Rivet'

rivet.HistoFile = 'Rivet.yoda'
rivet.DoRootHistos = False
#rivet.CrossSection = 1.0
job += rivet

import AthenaCommon.AlgSequence as acas
acas.dumpMasterSequence()
