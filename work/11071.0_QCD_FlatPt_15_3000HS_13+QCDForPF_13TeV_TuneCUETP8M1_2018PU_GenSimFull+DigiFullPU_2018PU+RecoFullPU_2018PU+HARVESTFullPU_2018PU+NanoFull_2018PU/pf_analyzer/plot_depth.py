import os,sys,socket,argparse,time
import re
import ROOT
import math
import numpy as np
from array import array
from tdrStyle import *
setTDRStyle()  

f_in = ROOT.TFile("pfNtuples.root","READ")
t = f_in.Get("events")
_pt = np.array([25,50,80,200])
_eta = np.array([0,0.4,0.8,1.2,1.3,1.4,1.6,1.8,2.1,2.3,2.5,2.8,3.0,5.0])
_rho = np.array([0,30,40,70])
_depth = np.array(range(8))
_ratio = np.arange(1,5,0.4) #try to plot the distribution of layer2/layer1

ROOT.gStyle.SetOptStat(0)


#init depth distribution histograms with different Pt
h_eta = []
for ieta,eta in enumerate(_eta[:-1]):
	rangename="eta_"+str(eta)+"_"+str(_eta[ieta+1])
	h_eta.append(ROOT.TH1D(rangename,rangename,len(_depth)-1,array('d',_depth)))

#Load branches
from load_pf_tree import *
declare_branches(t)

#in order to print out the progress
def print_same_line(s):
	sys.stdout.write(s)                     # just print
	sys.stdout.flush()                      # needed for flush when using \x08
	sys.stdout.write((b'\x08' * len(s)).decode())# back n chars    	
	#time.sleep(0.2)

ROOT.TH1.SetDefaultSumw2()
#Loop through tree
nentries = t.GetEntriesFast()
nbytes,nb=0,0
for jentry in range(nentries):
	print_same_line('Now loading ... '+str(round(100.*jentry/nentries,2))+'%')
	ientry = t.LoadTree(jentry)
	if (ientry < 0): break
	nb = t.GetEntry(jentry)
	nbytes+=nb
	#print njet,npjet
	for ipf in range(npf[0]):
		ieta=_eta.searchsorted(pf_eta[ipf])-1
		if ieta>=0 and ieta<len(h_eta): 
			for idepth in range(len(_depth)-1):
				h_eta[ieta].Fill(idepth+0.5, pf_depth[ipf][idepth])

f_out = ROOT.TFile("hists.root","recreate")

#Plot the histograms
def plot_hists(hists,filename):
	c = ROOT.TCanvas("c","c",800,800) #who cares about your name?
	colors=[ROOT.kCyan+1,ROOT.kBlue+1,ROOT.kMagenta+1,ROOT.kRed+1,ROOT.kOrange,ROOT.kYellow+1,ROOT.kGreen+1,ROOT.kGray] 
	firstDraw=True
	legend=ROOT.TLegend(0.60,0.65,0.95,1)
	for ihist,hist in enumerate(hists):
		hist[0].SetLineColor(colors[ihist])
		hist[1].SetLineColor(colors[ihist])
		hist[1].SetLineStyle(8) #dash line
		if firstDraw:
			firstDraw=False
			hist[0].GetXaxis().SetTitle("layer")
			hist[0].GetXaxis().SetTitleOffset(1.2)
			hist[0].GetYaxis().SetTitle("Percentage of distributed energy")
			hist[0].GetYaxis().SetTitleOffset(1.3)
			hist[0].SetTitle("")
			if hist[0].GetName()[0]=='r':
				hist[0].GetXaxis().SetTitle("layer2/layer1")
				hist[0].GetYaxis().SetTitle("Distribution")
			htmp=hist[0].DrawNormalized()
			htmp.GetYaxis().SetRangeUser(0,1.05)
			htmp.Draw()
		else:
			hist[0].DrawNormalized("same")
		hist[1].DrawNormalized("same")
		legend.AddEntry(hist[0], hist[0].GetName(),"lp")
		legend.AddEntry(hist[1], hist[1].GetName(),"lp")
		hist[0].Write()
		hist[1].Write()
	legend.Draw("same")
	c.Print("result/"+filename)

c = ROOT.TCanvas("c","c",800,800)
for ihist in h_eta:
	ihist.Draw()
	c.Print(ihist.GetName()+".png")
