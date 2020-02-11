from array import array
import numpy as np
import ROOT

file_list = [
        "root://cmseos.fnal.gov://store/user/syuan/TnP/ntuples_12172019/2017MC_3/data/SinglePhoton/crab_2017_RunB_SinglePhoton/200207_201307/0000/TnPTree_data_15.root",
        "root://cmseos.fnal.gov://store/user/syuan/TnP/ntuples_12172019/2017MC_3/data/SinglePhoton/crab_2017_RunB_SinglePhoton/200207_201307/0000/TnPTree_data_15.root",
        ]


chain = ROOT.TChain("tnpEleTrig/fitter_tree")

for filename in file_list:
    chain.Add(filename)

print("initial #entries = "+str(chain.GetEntries()))
event = np.zeros(1,dtype=int)
chain.SetBranchAddress('event',event)

outputFile = ROOT.TFile.Open("merged.root","recreate")
outputFile.mkdir("tnpEleTrig").cd()
newtree = chain.CloneTree(0)

eventlist = {}
skipped_events = 0
for iEntry in range(chain.GetEntries()):
    chain.GetEvent(iEntry)
    itree = chain.GetTreeNumber()
    if not event[0] in eventlist.keys() or eventlist[event[0]]==itree:
        eventlist[event[0]] = itree
        newtree.Fill()
    else:
        skipped_events+=1

print("final #entries = " + str(newtree.GetEntries()))
print("skipped events: "+str(skipped_events))
newtree.Write()
outputFile.Close()
