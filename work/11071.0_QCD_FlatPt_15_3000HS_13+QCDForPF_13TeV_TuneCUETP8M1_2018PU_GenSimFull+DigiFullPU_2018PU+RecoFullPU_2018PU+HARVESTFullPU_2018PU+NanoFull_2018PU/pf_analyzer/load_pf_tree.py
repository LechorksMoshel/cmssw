import numpy as n
import ROOT

rhoall     = n.zeros(1,dtype=float)
maxpf = 10000
    
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

npf       = n.zeros(1,dtype=int)
pf_pid    = n.zeros(maxpf, dtype=int)
pf_pt     = n.zeros(maxpf, dtype=float)
pf_eta     = n.zeros(maxpf, dtype=float)
pf_depth     = n.zeros([maxpf,7], dtype=float)

#Init branches
b_rhoall                 = ROOT.TBranch()
b_maxjet                 = ROOT.TBranch()
b_nrun                   = ROOT.TBranch()
b_nlumi                  = ROOT.TBranch()
b_nevent                 = ROOT.TBranch()
b_npv                    = ROOT.TBranch()
b_rhoall                 = ROOT.TBranch()
b_rhocentral             = ROOT.TBranch()
b_rhoneutral             = ROOT.TBranch()
b_rhochargedpileup       = ROOT.TBranch()
b_dphipfmet              = ROOT.TBranch()
b_npf                   = ROOT.TBranch()
b_pf_pid                   = ROOT.TBranch()
b_pf_pt                   = ROOT.TBranch()
b_pf_eta                   = ROOT.TBranch()
b_pf_depth                   = ROOT.TBranch()
    
def declare_branches(t):

    t.SetBranchAddress("run"                    , nrun                   , b_nrun                   ) 
    t.SetBranchAddress("lumi"                   , nlumi                  , b_nlumi                  ) 
    t.SetBranchAddress("event"                  , nevent                 , b_nevent                 ) 
    t.SetBranchAddress("npv"                    , npv                    , b_npv                    ) 
    t.SetBranchAddress("dphipfmet"              , dphipfmet              , b_dphipfmet              ) 
    t.SetBranchAddress("rhoall"                 , rhoall                 , b_rhoall                 ) 
    t.SetBranchAddress("rhocentral"             , rhocentral             , b_rhocentral             ) 
    t.SetBranchAddress("rhoneutral"             , rhoneutral             , b_rhoneutral             ) 
    t.SetBranchAddress("rhochargedpileup"       , rhochargedpileup       , b_rhochargedpileup       ) 
    t.SetBranchAddress("npf"      , npf      , b_npf      ) 
    t.SetBranchAddress("pf_pid"   , pf_pid   , b_pf_pid   ) 
    t.SetBranchAddress("pf_pt"    , pf_pt    , b_pf_pt    ) 
    t.SetBranchAddress("pf_eta"   , pf_eta   , b_pf_eta   ) 
    t.SetBranchAddress("pf_depth" , pf_depth , b_pf_depth ) 


    print "All branches configured"
