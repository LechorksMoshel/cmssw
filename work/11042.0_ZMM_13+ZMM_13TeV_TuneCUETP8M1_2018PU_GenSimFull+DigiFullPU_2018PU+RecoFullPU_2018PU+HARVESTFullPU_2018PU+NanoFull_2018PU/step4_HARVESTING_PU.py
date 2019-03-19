# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --conditions auto:phase1_2018_realistic -s HARVESTING:@standardValidation+@standardDQM+@ExtraHLT+@miniAODValidation+@miniAODDQM --pileup_input das:/RelValMinBias_13/CMSSW_10_3_0_pre5-103X_upgrade2018_realistic_v7-v1/GEN-SIM -n 10 --era Run2_2018 --scenario pp --pileup AVE_50_BX_25ns --filetype DQM --geometry DB:Extended --mc --filein file:step3_inDQM.root --fileout file:step4.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HARVESTING',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring('file:step3_inDQM.root')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('FULLMERGE')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(50.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_10_3_0_pre5/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v7-v1/10000/F9E9DD52-4C1B-834C-AC55-C0F4BEA6E7DF.root', '/store/relval/CMSSW_10_3_0_pre5/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v7-v1/10000/E71FB48E-AA82-B04E-A466-62783B73379A.root', '/store/relval/CMSSW_10_3_0_pre5/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v7-v1/10000/022A4F76-7CF3-3A4F-9AD3-9708662D0CC4.root', '/store/relval/CMSSW_10_3_0_pre5/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v7-v1/10000/D85A338F-CCF2-7B49-ADB1-246F67EC85D4.root', '/store/relval/CMSSW_10_3_0_pre5/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v7-v1/10000/AF4BA788-237D-8540-8C51-F1D98DB52767.root', '/store/relval/CMSSW_10_3_0_pre5/RelValMinBias_13/GEN-SIM/103X_upgrade2018_realistic_v7-v1/10000/D12742E3-ED09-BB44-955F-21A001BADE7F.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

# Path and EndPath definitions
process.dqmHarvestingFakeHLT = cms.Path(process.DQMOffline_SecondStep_FakeHLT+process.DQMOffline_Certification)
process.validationHarvestingHI = cms.Path(process.postValidationHI)
process.alcaHarvesting = cms.Path()
process.validationHarvestingNoHLT = cms.Path(process.postValidation+process.postValidation_gen)
process.validationHarvestingFS = cms.Path(process.postValidation+process.hltpostvalidation+process.postValidation_gen)
process.validationpreprodHarvesting = cms.Path(process.postValidation_preprod+process.hltpostvalidation_preprod+process.postValidation_gen)
process.genHarvesting = cms.Path(process.postValidation_gen)
process.validationprodHarvesting = cms.Path(process.hltpostvalidation_prod+process.postValidation_gen)
process.validationpreprodHarvestingNoHLT = cms.Path(process.postValidation_preprod+process.postValidation_gen)
process.dqmHarvestingPOGMC = cms.Path(process.DQMOffline_SecondStep_PrePOGMC)
process.DQMHarvestMiniAOD_step = cms.Path(process.DQMHarvestMiniAOD)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(process.validationHarvesting,process.dqmHarvesting,process.dqmHarvestingExtraHLT,process.validationHarvestingMiniAOD,process.DQMHarvestMiniAOD_step,process.dqmsave_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
