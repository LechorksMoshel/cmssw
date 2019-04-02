# Code used on jet/met analysis

Code pulled from <https://github.com/cms-sw/cmssw/blob/d46e37b67d976833df667eac2484ddf8d3d6f6d2/PhysicsTools/PatAlgos/python/slimming/packedPFCandidates_cfi.py#L23>
## Locations of my code:
- All code for MC production are in work/ directory. 
- each directory under work/ is for a specific workflow. For example 11042.0 for Z to mumu sample. 
- under 11071*/ there is a jet_depth_analyzer for analyzing the hcal depth segmentation for jets. There is a pf_analyzer to analyze similar depth segmentation in pf candidate level. There is a performance/ directory that contains code to make purity and efficiency code.

## Example: To make purity plots with ZMM samples:
```
cd work/11042*/performance/
cmsenv
python jet_efficiency_purity.py inputFiles=<either a single file or a textfile containing a list of root files>
```
