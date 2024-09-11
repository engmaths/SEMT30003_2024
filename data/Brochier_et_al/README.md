## 

https://githubtocolab.com/engmaths/SEMT30003_2024/blob/main/data/Brochier_et_al/brochier_et_al_excerpt.ipynb

These data are taken from 

> [Brochier, Thomas, et al. "Massively parallel recordings in macaque 
> motor cortex during an instructed delayed reach-to-grasp task." 
> Scientific data 5.1 (2018): 1-23.](https://www.nature.com/articles/sdata201855)


The full data for this paper can be found at
[https://gin.g-node.org/INT/multielectrode_grasp](https://gin.g-node.org/INT/multielectrode_grasp)

This example uses data from the file [`i140703-001_lfp-spikes.mat`](gin.g-node.org/INT/multielectrode_grasp/src/master/datasets_matlab/i140703-001_lfp-spikes.mat
).
This is only a small subset of the available data and metadata. Please refer to the  `i140703-001_lfp-spikes` for the full details.

Variables
=========

`unit_id:` 
> List of neuron ID numbers in the original Brochier et al. data.

`channel_id:` 
> List of LFP channel ID numbers in the original Brochier et al. data.

`waveform_examples:` neurons × sample × time(@30KHz) float16 array
> For each unit, 500 randomly selected spikes waveforms saved at the higher 30 KHz sampling rate. Units are microvolts.

`trial_spikes:` trials × neurons × time(@1KHz) uint8 array
> For each trial and unit, an array of timesamples where 1 denotes "spike" and 0 denotes "no spike".

`trial_lfp:` trials × channels × time(@1KHz) float16 array
> For each trial and electrode, the low-pass electrical voltage recorded at 1 KHz. Units are millivolts.

`ms_start:` int
> bin (ms) that each trial starts

`ms_cue:` int
> bin (ms) when cue was presented in each trial

`ms_go:` int
> bin (ms) when go signal was presented in each trial

`ms_stop:` int
> bin (ms) when subject completed each trial

`fs_waveform:` int
> Sample rate of waveform data

`fs:` int
> Sample rate of spike rasters, LFP data

