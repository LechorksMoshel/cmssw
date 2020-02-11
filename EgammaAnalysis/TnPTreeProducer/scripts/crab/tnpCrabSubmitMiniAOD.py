from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys

# this will use CRAB client API
from CRABAPI.RawCommand import crabCommand

# talk to DBS to get list of files in this dataset
from dbs.apis.dbsClient import DbsApi
dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')

dataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
fileDictList=dbs.listFiles(dataset=dataset)

print ("dataset %s has %d files" % (dataset, len(fileDictList)))

# DBS client returns a list of dictionaries, but we want a list of Logical File Names
lfnList = [ dic['logical_file_name'] for dic in fileDictList ]

# this now standard CRAB configuration

from WMCore.Configuration import Configuration

config = config()

submitVersion ="2017MC_3"
doEleTree = 'doEleID=False'
doPhoTree = 'doPhoID=False'
doHLTTree = 'doTrigger=True'
useMiniAOD = 'isAOD=False'

mainOutputDir = '/store/user/syuan/TnP/ntuples_12172019/%s' % submitVersion

config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/uscms/home/syuan/nobackup/workzone/work/1106EleTrigEff/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'
#config.Data.allowNonValidInputDataset = False
config.JobType.sendExternalFolder     = True

config.Data.inputDBS = 'global'
config.Data.publication = False
config.Data.allowNonValidInputDataset = True
#config.Data.publishDataName = 

config.Site.storageSite = 'T3_US_FNALLPC'


 
if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC

#    config.Data.splitting     = 'FileBased'
#    config.Data.unitsPerJob   = 10
#    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISpring18MiniAOD-100X_upgrade2018_realistic_v10-v2/MINIAODSIM'

    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.JobType.pyCfgParams  = ['isMC=True',doEleTree,doPhoTree,doHLTTree,useMiniAOD]
    config.Data.splitting = 'FileBased'
    config.General.requestName  = 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8'
    config.Data.unitsPerJob = 1
    config.Data.userInputFiles = lfnList
    #submit(config)
    del config.Data.userInputFiles


    ##### now submit DATA
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'data')
    config.Data.splitting     = 'FileBased'
    config.Data.lumiMask      = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
    config.Data.unitsPerJob   = 10
    config.JobType.pyCfgParams  = ['isMC=False','isEarly2017=True',doEleTree,doPhoTree,doHLTTree,useMiniAOD]
 
    config.General.requestName  = '2017_RunB_v1'
    config.Data.inputDataset    = '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.JobType.pyCfgParams  = ['isMC=False',doEleTree,doPhoTree,doHLTTree,useMiniAOD]

    config.General.requestName  = '2017_RunC_v1'
    config.Data.inputDataset    = '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.General.requestName  = '2017_RunD_v1'
    config.Data.inputDataset    = '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.General.requestName  = '2017_RunE_v1'
    config.Data.inputDataset    = '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.General.requestName  = '2017_RunF_v1'
    config.Data.inputDataset    = '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD'
    #submit(config)    

    ##### Submit SinglePhoton datasets
    config.JobType.pyCfgParams  = ['isMC=False','isEarly2017=True',doEleTree,doPhoTree,doHLTTree,useMiniAOD]
 
    config.General.requestName  = '2017_RunB_SinglePhoton'
    config.Data.inputDataset    = '/SinglePhoton/Run2017B-31Mar2018-v1/MINIAOD'
    submit(config)    

    config.JobType.pyCfgParams  = ['isMC=False',doEleTree,doPhoTree,doHLTTree,useMiniAOD]

    config.General.requestName  = '2017_RunC_SinglePhoton'
    config.Data.inputDataset    = '/SinglePhoton/Run2017C-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.General.requestName  = '2017_RunD_SinglePhoton'
    config.Data.inputDataset    = '/SinglePhoton/Run2017D-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.General.requestName  = '2017_RunE_SinglePhoton'
    config.Data.inputDataset    = '/SinglePhoton/Run2017E-31Mar2018-v1/MINIAOD'
    #submit(config)    

    config.General.requestName  = '2017_RunF_SinglePhoton'
    config.Data.inputDataset    = '/SinglePhoton/Run2017F-31Mar2018-v1/MINIAOD'
    #submit(config)    
