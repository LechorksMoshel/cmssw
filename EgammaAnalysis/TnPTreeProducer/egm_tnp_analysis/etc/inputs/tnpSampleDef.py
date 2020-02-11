from libPython.tnpClassUtils import tnpSample

### qll stat
eosDir1 = 'root://cmseos.fnal.gov//store/user/syuan/TnP/ntuples_12172019/2017MC_3/'
Data2017_10_1_X = {
    ### MiniAOD TnP for IDs scale factors
    'mc'          : tnpSample('DY_madgraph',
                                       eosDir1 + 'mc/merged_0131.root',
                                       isMC = True, nEvts =  -1 ),

    'data' : tnpSample('data' , eosDir1 + 'data/merged_0131.root' , lumi = 41.6 ),

    }

