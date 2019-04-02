#crab config to submit jobs step1, step2, step3

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZMM_DIGI_L1_DIGI2RAW_HLT_PU'
config.General.workArea = 'Crab3Area'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.inputFiles = ['step2_DIGI_L1_DIGI2RAW_HLT_PU.py','step3_RAW2DIGI_L1Reco_RECO_RECOSIM_EI_PAT_VALIDATION_DQM_PU.py']
#config.JobType.disableAutomaticOutputCollection = True
#config.JobType.outputFiles = ['step3_inMINIAODSIM.root']
config.JobType.psetName = 'step2_DIGI_L1_DIGI2RAW_HLT_PU.py'
config.JobType.sendPythonFolder = True
config.JobType.maxMemoryMB = 4500 #step2 turn out to use a lot
#config.JobType.numCores = 2
#config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 200 #number of events per jobs
config.Data.totalUnits = -1 #number of event
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/ZMM_PU_HEDepth_GEN/syuan-ZMM_PU_HEDepth_GEN-01b325d492eb745aa9f7609172ddfa01/USER'
config.Data.outLFNDirBase = '/store/user/syuan/ZMM_UPGRADE'  
config.Data.publication = True
config.Data.outputDatasetTag = 'ZMM_PU_HEDepth_step2'
#config.Data.lumiMask = ''

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.ignoreLocality=True
#config.Site.whitelist = ["T3_US*"]

