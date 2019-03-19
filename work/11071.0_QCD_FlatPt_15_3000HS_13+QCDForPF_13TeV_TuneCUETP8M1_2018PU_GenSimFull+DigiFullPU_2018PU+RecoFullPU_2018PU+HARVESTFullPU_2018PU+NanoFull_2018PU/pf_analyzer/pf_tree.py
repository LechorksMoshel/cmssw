import numpy as n

rhoall     = n.zeros(1,dtype=float)
maxpf = 100000
    
    #event information
nrun       = n.zeros(1,dtype=int)
nlumi      = n.zeros(1,dtype=int)
nevent     = n.zeros(1,dtype=float)
npv        = n.zeros(1,dtype=int)
rhoall     = n.zeros(1,dtype=float)
rhocentral = n.zeros(1,dtype=float)
rhoneutral = n.zeros(1,dtype=float)
rhochargedpileup = n.zeros(1,dtype=float)
dphipfmet = n.zeros(1,dtype=float)

    #pf information
npf       = n.zeros(1,dtype=int)
pf_pid    = n.zeros(maxpf, dtype=int)
pf_pt     = n.zeros(maxpf, dtype=float)
pf_eta     = n.zeros(maxpf, dtype=float)
pf_depth     = n.zeros([maxpf,7], dtype=float)
    
def declare_branches(t):

    t.Branch("run", nrun, 'run/I')
    t.Branch("lumi", nlumi, 'lumi/I')
    t.Branch("event", nevent, 'event/D')
    t.Branch("npv", npv, 'npv/I')
    t.Branch("dphipfmet", dphipfmet, 'dphipfmet/D')
    t.Branch("rhoall", rhoall, 'rhoall/D')
    t.Branch("rhocentral", rhocentral, 'rhocentral/D')
    t.Branch("rhoneutral", rhoneutral, 'rhoneutral/D')
    t.Branch("rhochargedpileup", rhochargedpileup, 'rhochargedpileup/D')

    t.Branch("npf", npf, 'npf/I')
    t.Branch("pf_pid", pf_pid, 'pf_pid[npf]/I')
    t.Branch("pf_pt", pf_pt, 'pf_pt[npf]/D')
    t.Branch("pf_eta", pf_eta, 'pf_eta[npf]/D')
    t.Branch("pf_depth", pf_depth, 'pf_depth[npf][7]/D')


    print "All branches configured"
