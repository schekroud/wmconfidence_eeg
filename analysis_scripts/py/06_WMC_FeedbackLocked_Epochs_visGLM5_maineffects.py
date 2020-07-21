#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:58:16 2019

@author: sammirc
"""
import numpy as np
import scipy as sp
import pandas as pd
import mne
import os
import os.path as op
import sys
from matplotlib import pyplot as plt
from copy import deepcopy
from scipy import stats
from scipy import ndimage

np.random.seed(seed = 10)



sys.path.insert(0, '/home/sammirc/Desktop/DPhil/wmConfidence/analysis_scripts')
from wmConfidence_funcs import get_subject_info_wmConfidence
from wmConfidence_funcs import gesd, plot_AR, toverparam, runclustertest_epochs

wd = '/home/sammirc/Desktop/DPhil/wmConfidence' #workstation wd
os.chdir(wd)

figpath = op.join(wd, 'figures', 'eeg_figs', 'feedbacklocked', 'epochs_glm5')

subs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
subs = np.array([         4, 5, 6, 7, 8, 9,     11, 12, 13, 14, 15, 16, 17, 18,     20, 21, 22,     24, 25, 26]) #subject 2 actually only has 72 trials in total, not really a lot so exclude atm
nsubs = subs.size


contrasts = ['defcorrect', 'justcorrect', 'incorrect',
             'errdefcorrect', 'errjustcorrect', 'errincorrect',
             'confdefcorrect', 'confjustcorrect', 'confincorrect',
             'incorrvsdef', 'incorrvsjust', 'justvsdef',
             'errorincorrvsdef', 'errorincorrvsjust', 'errorjustvsdef',
             'confincorrvsdef', 'confincorrvsjust', 'confjustvsdef']

threshold = -10
if threshold == -10:
    glmnum = 6
else:
    glmnum = 5

data = dict()
data_t = dict()
for i in contrasts:
    data[i] = []
    data_t[i] = []
for i in subs:
    print('\n\ngetting subject ' + str(i) +'\n\n')
    sub = dict(loc = 'workstation', id = i)
    param = get_subject_info_wmConfidence(sub) #_baselined
    for name in contrasts:
        data[name].append(   mne.read_evokeds(fname = op.join(param['path'], 'glms', 'feedback', 'epochs_glm'+str(glmnum), 'wmc_' + param['subid'] + '_feedbacklocked_tl_'+ name + '_betas-ave.fif'))[0])
        data_t[name].append( mne.read_evokeds(fname = op.join(param['path'], 'glms', 'feedback', 'epochs_glm'+str(glmnum), 'wmc_' + param['subid'] + '_feedbacklocked_tl_'+ name + '_tstats-ave.fif'))[0])

#drop right mastoid from literally everything here lol its not useful anymore
for cope in data.keys():
    for i in range(subs.size):
        data[cope][i]   = data[cope][i].drop_channels(['RM'])#.set_eeg_reference(ref_channels='average')
        data_t[cope][i] = data_t[cope][i].drop_channels(['RM'])#.set_eeg_reference(ref_channels='average')
#%%
gave = mne.grand_average(data['incorrect']); times = gave.times; del(gave)      
#%%     this is just a quick and dirty visualisation cos easy
for channel in ['FCz', 'Cz', 'CPz', 'Pz']:
    mne.viz.plot_compare_evokeds(
            evokeds = dict(
                    defscorrect = data['defcorrect'],
                    justcorrect   = data['justcorrect'],
                    incorrect   = data['incorrect']),
            colors = dict(
                    defscorrect = '#fc8d59',
                    justcorrect   = '#91cf60',
                    incorrect   = '#91bfdb'
                    ),
                    ci = .68, show_legend = 'upper right',
                    picks = channel, show_sensors = False,#ylim = dict(eeg=[-4,4]),
                    truncate_xaxis = False)
#%% same here but for the difference waves, no stats etc
for channel in ['FCz', 'Cz', 'CPz', 'Pz']:
    mne.viz.plot_compare_evokeds(
            evokeds = dict(
                    incorrvsdef = data['incorrvsdef'],
                    incorrvsjust   = data['incorrvsjust'],
                    justvsdef   = data['justvsdef']),
            colors = dict(
                    incorrvsdef = '#fc8d59',
                    incorrvsjust   = '#91cf60',
                    justvsdef   = '#91bfdb'
                    ),
                    ci = .68, show_legend = 'upper right',
                    picks = channel, show_sensors = False,#ylim = dict(eeg=[-4,4]),
                    truncate_xaxis = False)  
            
#%% plot the ERPs for the trial types at just specific midline channels

stat = 'beta' #choose whether you want to use the single subject tstats or betas for the analysis
if stat == 'beta':
    dat2use = deepcopy(data)
elif stat == 'tstat':
    dat2use = deepcopy(data_t)

tmin = 0
tmax = 1
for channel in ['FCz', 'Cz', 'CPz', 'Pz', 'POz', 'Oz']:
#for channel in ['FCz', 'Cz']:
    #first lets get all the single subject data into one dataframe:
    
    #for incorrect trials
    plottimes   = deepcopy(dat2use['incorrect'][0]).crop(tmax = tmax).times #this includes the baseline period for plotting
    plotdat_incorr = np.empty(shape = (subs.size, plottimes.size))
    for i in range(subs.size):
        plotdat_incorr[i,:] = np.squeeze(deepcopy(dat2use['incorrect'][i]).pick_channels([channel]).crop(tmax=tmax).data)
    
    plotdatmean_incorr = np.nanmean(plotdat_incorr, axis = 0)
    plotdatsem_incorr  = sp.stats.sem(plotdat_incorr, axis = 0)
    
    #for incorrect vs just correct contrast
    plotdat_just = np.empty(shape = (subs.size, plottimes.size))
    for i in range(subs.size):
        plotdat_just[i,:] = np.squeeze(deepcopy(dat2use['justcorrect'][i]).pick_channels([channel]).crop(tmax=tmax).data)
    
    plotdatmean_just = np.nanmean(plotdat_just, axis = 0)
    plotdatsem_just  = sp.stats.sem(plotdat_just, axis = 0)
    
    
    #for just correct vs definitely correct contrast
    plotdat_def = np.empty(shape = (subs.size, plottimes.size))
    for i in range(subs.size):
        plotdat_def[i,:] = np.squeeze(deepcopy(dat2use['defcorrect'][i]).pick_channels([channel]).crop(tmax=tmax).data)
    
    plotdatmean_def = np.nanmean(plotdat_def, axis = 0)
    plotdatsem_def  = sp.stats.sem(plotdat_def, axis = 0)
    
    
    #plotdatmean = np.multiply(plotdatmean, 10e5)
    fig = plt.figure(figsize = (12, 6))
    ax  = fig.add_subplot(111)
    ax.plot(plottimes, plotdatmean_incorr, color = '#e41a1c', lw = 1.5, label = 'incorrect')
    ax.fill_between(plottimes, plotdatmean_incorr - plotdatsem_incorr, plotdatmean_incorr + plotdatsem_incorr, alpha = .3, color = '#e41a1c')
    
    ax.plot(plottimes, plotdatmean_just, color = '#a1d99b', lw = 1.5, label = 'just correct', ls = 'dashed')
    ax.fill_between(plottimes, plotdatmean_just - plotdatsem_just, plotdatmean_just + plotdatsem_just, alpha = .3, color = '#a1d99b')
    
    ax.plot(plottimes, plotdatmean_def, color = '#31a354', lw = 1.5, label = 'definitely correct')
    ax.fill_between(plottimes, plotdatmean_def - plotdatsem_def, plotdatmean_def + plotdatsem_def, alpha = .3, color = '#31a354')
    
    
    ax.hlines([0], lw = 1, xmin = plottimes.min(), xmax = plottimes.max(), linestyles = 'dashed')
    ax.vlines([0], lw = 1, ymin = plotdatmean_incorr.min(), ymax = plotdatmean_incorr.max(), linestyles = 'dashed')
    ax.set_title('trial type  at channel '+channel)
    ax.set_ylabel('beta (AU)')
    ax.set_xlabel('Time relative to feedback onset (s)')
    ax.legend(loc = 'upper left')
    
    fig.savefig(fname = op.join(figpath, 'trialtype_erps_threshold%d_channel_%s.eps'%(abs(threshold),channel)), format = 'eps', dpi = 300)
    fig.savefig(fname = op.join(figpath, 'trialtype_erps_threshold%d_channel_%s.pdf'%(abs(threshold),channel)), format = 'pdf', dpi = 300)

#plt.close('all')
#%%
stat = 'beta' #choose whether you want to use the single subject tstats or betas for the analysis
if stat == 'beta':
    dat2use = deepcopy(data)
elif stat == 'tstat':
    dat2use = deepcopy(data_t)

#for channel in ['FCz', 'Cz', 'CPz', 'Pz', 'POz', 'Oz']:
for channel in ['FCz', 'Cz', 'Pz']:
    tmin = 0
    tmax = 1
    
    #incorrect vs definitely correct
    t_ivsd, clu_ivsd, clupv_ivsd, _ = runclustertest_epochs(data = dat2use,
                                                            contrast_name = 'incorrvsdef',
                                                            channels = [channel],
                                                            tmin = tmin,
                                                            tmax = tmax,
                                                            gauss_smoothing = None,
                                                            out_type = 'indices', n_permutations = 10000
                                                            )
    clutimes = deepcopy(dat2use['incorrect'][0]).crop(tmin = tmin, tmax = tmax).times
    masks_ivsd = np.asarray(clu_ivsd)[clupv_ivsd <= 0.05]
    
    
    #incorrect vs just correct
    t_ivsj, clu_ivsj, clupv_ivsj, _ = runclustertest_epochs(data = dat2use,
                                                            contrast_name = 'incorrvsjust',
                                                            channels = [channel],
                                                            tmin = tmin,
                                                            tmax = tmax,
                                                            gauss_smoothing = None,
                                                            out_type = 'indices', n_permutations = 10000
                                                            )
    masks_ivsj = np.asarray(clu_ivsj)[clupv_ivsj <= 0.05]
    
    #just correct vs definitely correct
    t_jvsd, clu_jvsd, clupv_jvsd, _ = runclustertest_epochs(data = dat2use,
                                                            contrast_name = 'justvsdef',
                                                            channels = [channel],
                                                            tmin = tmin,
                                                            tmax = tmax,
                                                            gauss_smoothing = None,
                                                            out_type = 'indices', n_permutations = 10000
                                                            )
    masks_jvsd = np.asarray(clu_jvsd)[clupv_jvsd <= 0.05]
    
    
    
    # now we will plot the mean with std error ribbons around the signal shape, ideally using seaborn
    
    #first lets get all the single subject data into one dataframe:
    
    #for incorrect vs definitely correct contrast
    plottimes   = deepcopy(dat2use['incorrect'][0]).crop(tmax = tmax).times #this includes the baseline period for plotting
    plotdat_ivsd = np.empty(shape = (subs.size, plottimes.size))
    for i in range(subs.size):
        plotdat_ivsd[i,:] = np.squeeze(deepcopy(dat2use['incorrvsdef'][i]).pick_channels([channel]).crop(tmax=tmax).data)
    
    plotdatmean_ivsd = np.nanmean(plotdat_ivsd, axis = 0)
    plotdatsem_ivsd  = sp.stats.sem(plotdat_ivsd, axis = 0)
    
    #for incorrect vs just correct contrast
    plotdat_ivsj = np.empty(shape = (subs.size, plottimes.size))
    for i in range(subs.size):
        plotdat_ivsj[i,:] = np.squeeze(deepcopy(dat2use['incorrvsjust'][i]).pick_channels([channel]).crop(tmax=tmax).data)
    
    plotdatmean_ivsj = np.nanmean(plotdat_ivsj, axis = 0)
    plotdatsem_ivsj  = sp.stats.sem(plotdat_ivsj, axis = 0)
    
    
    #for just correct vs definitely correct contrast
    plotdat_jvsd = np.empty(shape = (subs.size, plottimes.size))
    for i in range(subs.size):
        plotdat_jvsd[i,:] = np.squeeze(deepcopy(dat2use['justvsdef'][i]).pick_channels([channel]).crop(tmax=tmax).data)
    
    plotdatmean_jvsd = np.nanmean(plotdat_jvsd, axis = 0)
    plotdatsem_jvsd  = sp.stats.sem(plotdat_jvsd, axis = 0)
    
    
    #plotdatmean = np.multiply(plotdatmean, 10e5)
    fig = plt.figure(figsize = (12, 6))
    ax  = fig.add_subplot(111)
    ax.plot(plottimes, plotdatmean_ivsd, color = '#000000', lw = 1.5, label = 'incorrect vs definitely correct')
    ax.fill_between(plottimes, plotdatmean_ivsd - plotdatsem_ivsd, plotdatmean_ivsd + plotdatsem_ivsd, alpha = .3, color = '#636363')
    
    ax.plot(plottimes, plotdatmean_ivsj, color = '#e41a1c', lw = 1.5, label = 'incorrect vs just correct')
    ax.fill_between(plottimes, plotdatmean_ivsj - plotdatsem_ivsj, plotdatmean_ivsj + plotdatsem_ivsj, alpha = .3, color = '#e41a1c')
    
    ax.plot(plottimes, plotdatmean_jvsd, color = '#4daf4a', lw = 1.5, label = 'just correct vs definitely correct')
    ax.fill_between(plottimes, plotdatmean_jvsd - plotdatsem_jvsd, plotdatmean_jvsd + plotdatsem_jvsd, alpha = .3, color = '#4daf4a')
    
    
    ax.hlines([0], lw = 1, xmin = plottimes.min(), xmax = plottimes.max(), linestyles = 'dashed')
    ax.vlines([0], lw = 1, ymin = plotdatmean_ivsd.min(), ymax = plotdatmean_ivsd.max(), linestyles = 'dashed')
    ax.set_title('trial type contrasts at channel '+channel)
    ax.set_ylabel('beta (AU)')
    ax.set_xlabel('Time relative to feedback onset (s)')
    ax.legend(loc = 'upper left')
    
    for mask in masks_ivsd:
        ax.hlines(y = -5e-6,
                  xmin = np.min(clutimes[mask[1]]),
                  xmax = np.max(clutimes[mask[1]]),
                  lw=5, color = '#636363', alpha = .5) #plot significance timepoints for difference effect
    
    for mask in masks_ivsj:
        ax.hlines(y = -5.2e-6,
                  xmin = np.min(clutimes[mask[1]]),
                  xmax = np.max(clutimes[mask[1]]),
                  lw=5, color = '#e41a1c', alpha = .5) #plot significance timepoints for difference effect
    
    for mask in masks_jvsd:
        ax.hlines(y = -5.4e-6,
                  xmin = np.min(clutimes[mask[1]]),
                  xmax = np.max(clutimes[mask[1]]),
                  lw=5, color = '#4daf4a', alpha = .5) #plot significance timepoints for difference effect
    
    fig.savefig(fname = op.join(figpath, 'trialtype_diffwaves_20subs_threshold%s_channel_%s_%s.eps'%(str(abs(threshold)), channel, stat)), format = 'eps', dpi = 300)
    fig.savefig(fname = op.join(figpath, 'trialtype_diffwaves_20subs_threshold%s_channel_%s_%s.pdf'%(str(abs(threshold)), channel, stat)), format = 'pdf', dpi = 300)
#%%

#we know there are differences, so lets plot these differences
    
stat = 'beta' #choose whether you want to use the single subject tstats or betas for the analysis
if stat == 'beta':
    dat2use = deepcopy(data)
elif stat == 'tstat':
    dat2use = deepcopy(data_t)
    
for contrast in ['incorrvsdef', 'incorrvsjust', 'justvsdef']:
    for channel in ['FCz', 'Cz', 'Pz']:
#        if contrast == 'incorrvsdef':
#            masks2use = deepcopy(masks_ivsd)
#        elif contrast == 'incorrvsjust':
#            masks2use = deepcopy(masks_ivsj)
#        else:
#            masks2use = deepcopy(masks_jvsd)
            
        t_cope, clu_cope, clupv_cope, _ = runclustertest_epochs(data = dat2use,
                                                            contrast_name = contrast,
                                                            channels = [channel],
                                                            tmin = tmin,
                                                            tmax = tmax,
                                                            gauss_smoothing = None,
                                                            out_type = 'indices', n_permutations = 10000
                                                            )
        masks_cope = np.asarray(clu_cope)[clupv_cope <= 0.05]
        
        masks2use = masks_cope
            
        gave = mne.grand_average(dat2use[contrast])
        vmin = -3
        vmax = np.multiply(vmin,-1)
        
        fig = gave.plot_joint(picks = 'eeg', title = contrast+', clusters from '+channel,
                                  topomap_args = dict(contours = 0, outlines = 'head', extrapolate='head', vmin = vmin, vmax = vmax, cmap = 'RdBu_r'),
                                  times = np.concatenate([np.arange(0.15,0.3,.05), np.arange(.4,.7,.05)]) #plot topos in this range
                                  ) 
        ax = fig.axes[0] #get the axis of the erp plot
        tmins, tmaxs = [], [] #get the tmin and tmax of these clusters too as we're going to plot their topographies
        for mask in masks2use:
            yline = np.round(gave.data.min() * 10**6) -1
            ax.hlines(y = yline,
                      xmin = clutimes[mask[1]].min(),
                      xmax = clutimes[mask[1]].max(),
                      lw = 5, color = '#bdbdbd', alpha = .5)
            tmins.append(clutimes[mask[1]].min())
            tmaxs.append(clutimes[mask[1]].max())
        fig.savefig(fname = op.join(figpath, '%s_jointplot_20subs_threshold%d_channel_%s_clusters.pdf'%(contrast, abs(threshold), channel)), format = 'pdf', dpi = 300)
        fig.savefig(fname = op.join(figpath, '%s_jointplot_20subs_threshold%d_channel_%s_clusters.eps'%(contrast, abs(threshold), channel)), format = 'eps', dpi = 300)
        
        for mask in range(len(tmins)):
            itmin = tmins[mask] #get the start time
            itmax = tmaxs[mask] #and the end time
            
            plotdatmin = deepcopy(gave).crop(tmin = itmin, tmax = itmax).data.min()
            plotdatmax = deepcopy(gave).crop(tmin = itmin, tmax = itmax).data.max()
            print(itmin, plotdatmin, plotdatmax)
            
            tcentre = np.add(itmin, np.divide(np.subtract(itmax, itmin),2)) #get the halfway point
            twidth  = np.subtract(itmax,itmin) #and get the width of the significant cluster
            topovmin, topovmax = -3, 3
            
            if contrast in ['incorrvsjust'] :
                topovmin, topovmax = -2.5, 2.5
            elif contrast in ['justvsdef']:
                topovmin, topovmax = -1.2,1.2
            
            fig = gave.plot_topomap(times = tcentre, #plot this time point
                                    average = twidth, #and average over this time width around it (half of this value either side), so we plot the cluster time width
                                    vmin = topovmin,
                                    vmax = topovmax,
                                    #colorbar=True,
                                    contours = 4,
                                    cmap = 'RdBu_r',
                                    extrapolate = 'head',
                                    ch_type = 'eeg',
                                    res = 300, #resolution of the image
                                    title = '%s to %ss'%(str(itmin), str(itmax)))
            fig.savefig(fname = op.join(figpath, '%s_topomap_20subs_threshold%d_%s_to_%s_channel_%s_clusters.pdf'%(contrast, abs(threshold), itmin, itmax, channel)), format = 'pdf', dpi = 300)
            fig.savefig(fname = op.join(figpath, '%s_topomap_20subs_threshold%d_%s_to_%s_channel_%s_clusters.eps'%( contrast, abs(threshold), itmin, itmax, channel)), format = 'eps', dpi = 300)
            plt.close()

#%%

ftests = dict()
ftest_names = ['ME_trialtype', 'ME_error', 'ME_confidence']
for i in ftest_names:
    ftests[i] = []
for i in subs:
    print('\n\ngetting subject ' + str(i) +'\n\n')
    sub = dict(loc = 'workstation', id = i)
    param = get_subject_info_wmConfidence(sub) #_baselined
    for name in ftest_names:
        ftests[name].append( mne.read_evokeds(fname = op.join(param['path'], 'glms', 'feedback', 'epochs_glm'+str(glmnum), 'wmc_' + param['subid'] + '_feedbacklocked_tl_'+ name + '_fstat-ave.fif'))[0])

#drop right mastoid from literally everything here lol its not useful anymore
for test in ftests.keys():
    for i in range(subs.size):
        ftests[test][i]   = ftests[test][i].drop_channels(['RM'])#.set_eeg_reference(ref_channels='average')

#%%


gave = mne.grand_average(ftests['ME_trialtype'])

gave.plot_joint(picks = 'eeg', title = 'ME_trialtype', ts_args = dict(cmap = 'viridis'),
                              topomap_args = dict(contours = 0, outlines = 'head',extrapolate='head', cmap = 'viridis'),
                              times = np.arange(0.15, 0.5, .05)) #plot topos in this range

mne.grand_average(ftests['ME_error']).plot_joint(picks = 'eeg', title = 'ME_error', ts_args = dict(cmap = 'viridis'),
                              topomap_args = dict(contours = 0, outlines = 'head',extrapolate='head', cmap = 'viridis'),
                              times = np.arange(0.15, 0.5, .05)) #plot topos in this range
mne.grand_average(ftests['ME_error']).plot(picks=['FCz', 'Cz'])

gave.plot(picks='Cz')

for channel in ['FCz', 'Cz', 'CPz', 'Pz']:
    mne.viz.plot_compare_evokeds(
            evokeds = dict(
                    trialtype  = ftests['ME_trialtype'],
                    error      = ftests['ME_error'],
                    confidence = ftests['ME_confidence']),
            colors = dict(
                    trialtype = '#fc8d59',
                    error   = '#91cf60',
                    confidence   = '#91bfdb'),
                    ci = .68, show_legend = 'upper right')

plotdat = np.empty(shape = (subs.size, plottimes.size))
for i in range(subs.size):
    plotdat[i,:] = np.squeeze(deepcopy(ftests['ME_trialtype'][i]).pick_channels([channel]).crop(tmax=tmax).data)

                    picks = channel, show_sensors = False,#ylim = dict(eeg=[-4,4]),
                    truncate_xaxis = False)  
        
channel = 'Cz'
t, clu, clupv, _ = runclustertest_epochs(data = ftests,
                                         contrast_name = 'ME_trialtype',
                                         channels = ['Cz'],
                                         tmin = 0, tmax = 1,
                                         gauss_smoothing = None, out_type = 'indices',
                                         n_permutations = 5000)
masks = np.asarray(clu)[clupv<0.05]
clutimes = deepcopy(gave).crop(tmin = 0, tmax = 1).times


#for just correct vs definitely correct contrast
tmin = 0
tmax = 1
plottimes   = deepcopy(ftests['ME_trialtype'][0]).crop(tmax = tmax).times #this includes the baseline period for plotting
plotdat = np.empty(shape = (subs.size, plottimes.size))
for i in range(subs.size):
    plotdat[i,:] = np.squeeze(deepcopy(ftests['ME_trialtype'][i]).pick_channels([channel]).crop(tmax=tmax).data)

plotdatmean = np.nanmean(plotdat, axis = 0)
plotdatsem = sp.stats.sem(plotdat, axis = 0)


#plotdatmean = np.multiply(plotdatmean, 10e5)
fig = plt.figure(figsize = (12, 6))
ax  = fig.add_subplot(111)
ax.plot(plottimes, plotdatmean, color = '#000000', lw = 1.5, label = 'ME_trialtype')
ax.fill_between(plottimes, plotdatmean - plotdatsem, plotdatmean + plotdatsem, alpha = .3, color = '#636363')

ax.hlines([0], lw = 1, xmin = plottimes.min(), xmax = plottimes.max(), linestyles = 'dashed')
ax.vlines([0], lw = 1, ymin = 0, ymax = plotdatmean.max(), linestyles = 'dashed')
ax.set_title('trial type contrasts at channel '+channel)
ax.set_ylabel('F-stat (AU)')
ax.set_xlabel('Time relative to feedback onset (s)')
ax.legend(loc = 'upper left')

for mask in masks:
    ax.hlines(y = -5e-6,
              xmin = np.min(clutimes[mask[1]]),
              xmax = np.max(clutimes[mask[1]]),
              lw=5, color = '#636363', alpha = .5) #plot significance timepoints for difference effect

        