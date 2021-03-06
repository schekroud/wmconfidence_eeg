#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:03:07 2019

@author: sammirc
"""
import numpy as np
import scipy as sp
import pandas as pd
import mne
from copy import deepcopy
import os
import os.path as op
import sys
from matplotlib import pyplot as plt

#sys.path.insert(0, '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence_eegfmri/analysis_scripts')
sys.path.insert(0, '/home/sammirc/Desktop/DPhil/wmConfidence/analysis_scripts')
from wmConfidence_funcs import get_subject_info_wmConfidence

wd = '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence'; #laptop wd
wd = '/home/sammirc/Desktop/DPhil/wmConfidence' #workstation wd
os.chdir(wd)


#subs = np.array([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
subs = np.array([17, 18])
subs = np.array([18, 19, 20, 21])

for i in subs:
    sub   = dict(loc = 'workstation', id = i)
    param = get_subject_info_wmConfidence(sub)
    
    if i in [1,2]: #these are two pilot subjects that have 10 blocks in one session, probably not going to be used
        raw = mne.io.read_raw_eeglab(
                input_fname=param['rawset'],
                montage = 'easycap-M1',
                eog=['VEOG', 'HEOG'], preload = True)
        raw.rename_channels({'PO6':'PO8'})
        raw.set_montage('easycap-M1')
        
        raw.filter(1, 40) #filter raw data
        ica = mne.preprocessing.ICA(n_components = .99, method = 'infomax').fit(raw)
        eog_epochs = mne.preprocessing.create_eog_epochs(raw)
        eog_inds, eog_scores = ica.find_bads_eog(eog_epochs)
        ica.plot_scores(eog_scores)
        
        ica.plot_components(inst=raw)
        ica.exclude.extend(eog_inds)
        ica.apply(inst=raw)
        
        raw.save(fname = param['rawcleaned'], fmt='double')
    elif i in [3, 10, 19]:
        raw = mne.io.read_raw_eeglab(
                input_fname=param['rawset_sess1'],
                montage = 'easycap-M1',
                eog=['VEOG', 'HEOG'], preload = True)
        raw.set_montage('easycap-M1')
        
        raw.filter(1, 40) #filter raw data
        ica = mne.preprocessing.ICA(n_components = 60, method = 'infomax').fit(raw)
        eog_epochs = mne.preprocessing.create_eog_epochs(raw)
        eog_inds, eog_scores = ica.find_bads_eog(eog_epochs)
        ica.plot_scores(eog_scores)
        
        ica.plot_components(inst=raw)
        ica.exclude.extend(eog_inds)
        ica.apply(inst=raw)
        
        raw.save(fname = param['rawcleaned_sess1'], fmt='double')
        
    else:
        for part in [1,2]:#[1, 2]:
            raw = mne.io.read_raw_eeglab(
                input_fname=param['rawset_sess'+str(part)],
                montage = 'easycap-M1',
                eog=['VEOG', 'HEOG'], preload = True)
            raw.set_montage('easycap-M1')
            
            raw.filter(1, 40) #filter raw data
#            if i == 11 and part == 2: 
#                #for some reason it fails on this session because of some pca component, but setting a number of components works fine
#                ica = mne.preprocessing.ICA(n_components = 60, method = 'infomax').fit(raw)
#            else:
#                ica = mne.preprocessing.ICA(n_components = .99, method = 'infomax').fit(raw)
            ica = mne.preprocessing.ICA(n_components=60, method = 'infomax').fit(raw)
            
            eog_epochs = mne.preprocessing.create_eog_epochs(raw)
            eog_inds, eog_scores = ica.find_bads_eog(eog_epochs)
            ica.plot_scores(eog_scores, eog_inds)
            
            ica.plot_components(inst=raw)
            print('subject %d, part %d components to remove:'%(i, part), eog_inds)
            ica.exclude.extend(eog_inds)#[0:2])
            ica.apply(inst=raw)
            
            raw.save(fname = param['rawcleaned_sess'+str(part)], fmt='double', overwrite = 'True')

#%%  