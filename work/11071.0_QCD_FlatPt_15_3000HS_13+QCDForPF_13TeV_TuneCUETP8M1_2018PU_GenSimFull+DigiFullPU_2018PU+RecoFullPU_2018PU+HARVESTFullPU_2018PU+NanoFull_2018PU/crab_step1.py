#crab config to submit jobs step1, step2, step3

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'QCD_FlatPT_GEN'
config.General.workArea = 'Crab3Area_step1'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
#config.JobType.inputFiles = ['step2_DIGI_L1_DIGI2RAW_HLT_PU.py','step3_RAW2DIGI_L1Reco_RECO_RECOSIM_EI_PAT_VALIDATION_DQM_PU.py']
#config.JobType.disableAutomaticOutputCollection = True
#config.JobType.outputFiles = ['step3_inMINIAODSIM.root']
config.JobType.psetName = 'QCDForPF_13TeV_TuneCUETP8M1_cfi_GEN_SIM.py'
#config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 200 #number of events per jobs
config.Data.totalUnits = 10000 #number of event
config.Data.outLFNDirBase = '/store/user/syuan/QCD_FlatPT'  
config.Data.publication = True
config.Data.outputDatasetTag = 'QCD_FlatPT_2018_PU_HEDepth_GEN'
config.Data.outputPrimaryDataset = 'QCD_FlatPT_2018_PU_HEDepth_GEN'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
# json with 3.99/fb

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.storageSite = 'T2_CH_CERN'
config.Data.ignoreLocality=True
config.Site.whitelist = ["T3_US*"]

