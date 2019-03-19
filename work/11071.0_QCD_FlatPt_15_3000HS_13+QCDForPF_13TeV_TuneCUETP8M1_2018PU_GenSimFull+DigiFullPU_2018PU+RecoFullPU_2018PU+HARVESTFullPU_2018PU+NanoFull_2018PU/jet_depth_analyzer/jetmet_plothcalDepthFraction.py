# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('python')

#default options
options.inputFiles="../step3_inMINIAODSIM.root"
options.outputFile="jetmetNtuples.root"
options.maxEvents=-1

#overwrite if given any command line arguments
options.parseArguments()

# define deltaR
from math import hypot, pi, sqrt, fabs
import numpy as n

from jetmet_tree import *
from functions import *

# create an oput tree.

#fout = ROOT.TFile ("jetmet.root","recreate")
fout = ROOT.TFile (options.outputFile,"recreate")
t    = ROOT.TTree ("events","events")

declare_branches(t)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

pfs, pfLabel        = Handle("std::vector<pat::PackedCandidate>"), "packedPFCandidates"

rhoall_, rhoallLabel         = Handle("double"), "fixedGridRhoFastjetAll"
rhocentral_, rhocentralLabel = Handle("double"), "fixedGridRhoFastjetCentral"
rhoneutral_, rhoneutralLabel = Handle("double"), "fixedGridRhoFastjetCentralNeutral"
rhochargedpileup_, rhochargedpileupLabel = Handle("double"), "fixedGridRhoFastjetCentralChargedPileUp"

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
#events = Events("file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValTTbar_13/MINIAODSIM/PU25ns_94X_mc2017_realistic_PixFailScenario_Run305081_FIXED_HS_AVE50-v1/10000/02B605A1-86C2-E711-A445-4C79BA28012B.root")
events = Events(options)

h1=ROOT.TH1F("DepthDistribution","DepthDistribution",7,0,7)


for ievent,event in enumerate(events):

    if options.maxEvents is not -1:
        if ievent > options.maxEvents: continue
    
    event.getByLabel(pfLabel, pfs)

    event.getByLabel(rhoallLabel,rhoall_)
    event.getByLabel(rhocentralLabel,rhocentral_)
    event.getByLabel(rhoneutralLabel,rhoneutral_)
    event.getByLabel(rhochargedpileupLabel,rhochargedpileup_)

    rhoall[0]     = rhoall_.product()[0]
    rhocentral[0] = rhocentral_.product()[0]
    rhoneutral[0] = rhoneutral_.product()[0]
    rhochargedpileup[0] = rhochargedpileup_.product()[0]

    #print "\nEvent %d: run %6d, lumi %4d, event %12d" % (ievent,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
    if ievent%5000==0: print("processing events number: "+str(ievent))



    for ipf,pf in enumerate(pfs.product()):
		for i in range(1,8):
			h1.Fill(i-0.5, pf.hcalDepthEnergyFraction(i)*pf.p())

canv=ROOT.TCanvas("canv","canv")
h1.DrawNormalized()
canv.Print("hcalDepthDistribution.png")
