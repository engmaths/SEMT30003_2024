These data are taken from 

> Brochier, Thomas, et al. "Massively parallel recordings in macaque 
> motor cortex during an instructed delayed reach-to-grasp task." 
> Scientific data 5.1 (2018): 1-23.

> The full data for this paper can be found at
> gin.g-node.org/INT/multielectrode_grasp

This example uses only a small subset of a single recording, 
i140703-001_lfp-spikes.mat, which you can download at

> gin.g-node.org/INT/multielectrode_grasp/
> src/master/datasets_matlab/i140703-001_lfp-spikes.mat

To make this file
- We selected 100 nurons from the larger dataset
- We extracted single-trial data aligned to the go cue for each trial
- We kept only 500 of the total spike waveforms
- We discarded irregular trials

Refer to `i140703-001_lfp-spikes.mat` for the full details

Variables
=========

unit_id: nneurons int array
    List of neuron ID numbers in the original Brochier et al. data.

channel_id: nchannels int array
    List of LFP channel ID numbers in the original Brochier et al. data.

waveform_examples: neruons × sample × time(@30KHz) float16 array
    For each unit, 500 randomly selected spikes saved at the higher 30 KHz sampling rate.
    Units are microvolts.

trial_spikes: trials × neruons × time(@1KHz) boolean array
    For each trial and unit, boolean signal that is 1 for bins containing a spike
    Units are spikes per millisecond.

trial_lfp: trials × channels × time(@1KHz) float61array
    For each trial and electrode, the low-pass electrial voltage recorded at 1 KHz.
    Units are millivolts.

ms_start: int
    bin (ms) that each trial starts
    
ms_cue: int
    bin (ms) when cue was presented in each trial
    
ms_go: int
    bin (ms) when go signal was presented in each trial
    
ms_stop: int
    bin (ms) when subject completed each trial

fs_waveform: int
    Sample rate of waveform data

fs: int
    Sample rate of spike rasters, LFP data