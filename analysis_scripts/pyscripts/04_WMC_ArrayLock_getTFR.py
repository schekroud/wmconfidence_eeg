#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:03:10 2019

@author: sammirc
"""


import numpy as np
import pandas as pd
import mne
import os
import os.path as op
import sys

#sys.path.insert(0, '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence_eegfmri/analysis_scripts')
sys.path.insert(0, '/home/sammirc/Desktop/DPhil/wmConfidence/analysis_scripts')
from wmConfidence_funcs import get_subject_info_wmConfidence
from wmConfidence_funcs import gesd, plot_AR

wd = '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence'; #laptop wd
wd = '/home/sammirc/Desktop/DPhil/wmConfidence' #workstation wd
os.chdir(wd)


subs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
subs = np.array([         4, 5, 6, 7, 8, 9,     11, 12, 13, 14, 15, 16, 17, 18,     20, 21, 22,     24, 25, 26])
#subs = np.array([24,25])


for i in subs:
    print('\n\nworking on subject ' + str(i) +'\n\n')
    sub = dict(loc = 'workstation', id = i)
    param = get_subject_info_wmConfidence(sub)

    arraylocked = mne.epochs.read_epochs(fname = param['arraylocked'].replace('arraylocked', 'arraylocked_cleaned'), preload=True) #read raw data
    arraylocked.resample(100) #downsample to 100Hz so don't overwork the workstation
    arraylocked = mne.add_reference_channels(arraylocked, ref_channels = 'LM')
    arraylocked.set_eeg_reference(ref_channels = ['LM','RM']) #re-reference average of the left and right mastoid now


#    #will do an automated process of looking for trials with heightened variance (noise) and output which trials to keep
#    _, keeps = plot_AR(arraylocked, method = 'gesd', zthreshold = 1.5, p_out=.1, alpha = .05, outlier_side = 1)
#    keeps = keeps.flatten()
#
#    discards = np.ones(len(arraylocked), dtype = 'bool')
#    discards[keeps] = False
#    arraylocked = arraylocked.drop(discards) #first we'll drop trials with excessive noise in the EEG

    arraylocked = arraylocked['arraycueblink == 0'] #also exclude trials where blinks happened in the array or cue period

    #check to see if there are any trials where the previous trial confdiff is nan (i.e. no previous trial bcos start of session or block)

    # set up params for TF decomp
    freqs = np.arange(1, 41, 1)  # frequencies from 2-35Hz
    n_cycles = freqs *.3  # 300ms timewindow for estimation

    print('\nrunning TF decomposition\n')
    # Run TF decomposition overall epochs
    tfr = mne.time_frequency.tfr_morlet(arraylocked, freqs=freqs, n_cycles=n_cycles,
                         use_fft=True, return_itc=False, average=False)
    tfr.metadata.to_csv(param['arraylocked_tfr_meta'], index=False)
    tfr.save(fname = param['arraylocked_tfr'], overwrite = True)

    del(arraylocked)
    del(tfr)