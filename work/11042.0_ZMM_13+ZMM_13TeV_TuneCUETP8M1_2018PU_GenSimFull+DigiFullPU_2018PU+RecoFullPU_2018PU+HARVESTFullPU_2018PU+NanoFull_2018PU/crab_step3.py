#crab config to submit jobs step1, step2, step3

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZMM_MINIAOD'
config.General.workArea = 'Crab3Area'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.inputFiles = ['step2_DIGI_L1_DIGI2RAW_HLT_PU.py','step3_RAW2DIGI_L1Reco_RECO_RECOSIM_EI_PAT_VALIDATION_DQM_PU.py']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['step3_inMINIAODSIM.root','step3.root']
config.JobType.psetName = 'step3_RAW2DIGI_L1Reco_RECO_RECOSIM_EI_PAT_VALIDATION_DQM_PU.py'
config.JobType.sendPythonFolder = True
config.JobType.maxMemoryMB = 5000 #step2/3 turn out to use a lot
#config.JobType.maxJobRuntimeMin = 600 #Should not take too long
#config.JobType.numCores = 2
#config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 200 #number of events per jobs
config.Data.totalUnits = -1 #number of event
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/ZMM_PU_HEDepth_GEN/syuan-ZMM_PU_HEDepth_step2-bdc6ad02bd5139dae8f07b36fbd0c1f1/USER'
config.Data.outLFNDirBase = '/store/user/syuan/ZMM_UPGRADE'  
config.Data.publication = True
config.Data.outputDatasetTag = 'ZMM_PU_HEDepth_step3'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
# json with 3.99/fb

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.ignoreLocality=True
#config.Site.whitelist = ["T3_US*"]

