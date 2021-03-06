#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:55:47 2019

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
plt.ion()

#sys.path.insert(0, '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence_eegfmri/analysis_scripts')
sys.path.insert(0, '/home/sammirc/Desktop/DPhil/wmConfidence/analysis_scripts')
from wmConfidence_funcs import get_subject_info_wmConfidence

wd = '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence'; #laptop wd
wd = '/home/sammirc/Desktop/DPhil/wmConfidence' #workstation wd
os.chdir(wd)


subs = np.array([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
subs = np.array([        4, 5, 6, 7, 8, 9,     11, 12, 13, 14, 15, 16, 17, 18,     20, 21, 22,     24, 25])
subs = np.array([24,25])
subs = np.array([26])
for i in subs:
    sub = dict(loc = 'workstation', id = i)
    param = get_subject_info_wmConfidence(sub)
    
    print('\n\n - - - - - working on subject %d- - - - -\n\n'%(i))
    
    if i <= 2: #these subjects only have one session
        
        #we're going to read in the raw data, filter it, epoch it around the array/cue triggers and check to see if there are blinks nearby
        raw = mne.io.read_raw_eeglab(input_fname = param['rawset'], montage = 'easycap-M1', eog = ['VEOG', 'HEOG'], preload=True)
        raw.rename_channels({'PO6':'PO8'})
        raw.set_montage('easycap-M1')
        raw.filter(1,40)
        
        #epoching
        #here it's important to specify a dictionary that assigns each trigger to its own integer value
        #mne.events_from_annotations will assign each trigger to an ordered integer, so e.g. trig11 will be 2, but epoching 11 will include another trigger
        #this solves it
        event_id = {'1' : 1, '2':2,                 #array
                    '11':11,'12':12,'13':13,'14':14,#cue
                    '21':21,'22':22,'23':23,'24':24,#probe
                    '31':31,'32':32,'33':33,'34':34,#space
                    '41':41,'42':42,'43':43,'44':44,#click
                    '51':51,'52':52,'53':53,'54':54,#confprobe
                    '61':61,'62':62,'63':63,'64':64,#space
                    '71':71,'72':72,'73':73,'74':74,#click
                    '76':76,'77':77,'78':78,'79':79, #feedback
                    '254':254,'255':255}
        
        events_array = {'neutral':1, 'cued':2}
        events_cue = {'neutral/probeleft'  : 11,
                      'neutral/proberight' : 12,
                      'cued/probeleft'     : 13,
                      'cued/proberight'    : 14}
        events,_ = mne.events_from_annotations(raw, event_id = event_id)
        tmin, tmax = -0.25, 0.25
        baseline = (None,0)
        
        arraylocked = mne.Epochs(raw, events, events_array, tmin, tmax, baseline, reject_by_annotation=False, preload=True)
        cuelocked   = mne.Epochs(raw, events, events_cue, tmin, tmax, baseline, reject_by_annotation=False, preload=True)        
        bdata = pd.DataFrame.from_csv(path = param['behaviour'])
        arraylocked.metadata = bdata
        cuelocked.metadata   = bdata

        veog_array = np.squeeze(deepcopy(arraylocked).pick_channels(['VEOG']).get_data())
        veog_diffs_array = np.multiply(np.subtract(np.max(veog_array,1), np.min(veog_array,1)), 1e6)
        array_throws = np.add(np.squeeze(np.where(np.logical_and(sp.stats.zscore(veog_diffs_array)>=2,veog_diffs_array > 250))),1)
        
        veog_cue = np.squeeze(deepcopy(cuelocked).pick_channels(['VEOG']).get_data())
        veog_diffs_cue = np.multiply(np.subtract(np.max(veog_cue,1), np.min(veog_cue,1)), 1e6)
        cue_throws = np.add(np.squeeze(np.where(np.logical_and(sp.stats.zscore(veog_diffs_cue)>=2,veog_diffs_cue > 250))),1)


#        this is really for if you want to visually inspect every trial, which i've done in the past. the above section automates this though
#        arraylocked.plot(n_epochs=4, picks = ['eog'])
#        arraythrowouts = []
#        if len(arraylocked.metadata.trialnum) != len(bdata): #should be 320 trials in these datasets
#            for x,y in np.ndenumerate(bdata.trialnum): #loop over every trial id in the behavioural data
#                if y not in arraylocked.metadata.trialnum.tolist(): #check if the trial ids in behavioural data are in the eeg metadata
#                    arraythrowouts.append(y) #if not, this trial was discarded, so note down that this trial was discarded
#                    
#        cuelocked.plot(n_epochs=4, picks = ['eog'])
#        cuethrowouts = []
#        if len(cuelocked.metadata.trialnum) != len(bdata):
#            for x,y in np.ndenumerate(bdata.trialnum):
#                if y not in cuelocked.metadata.trialnum.tolist():
#                    cuethrowouts.append(y)
        
#        discards = np.concatenate([arraythrowouts, cuethrowouts]).astype(int)
#        discards = np.unique(discards) #take only uniques, in case a trial had a blink at both array and cue so we don't double it here
#        discards = np.subtract(discards, 1) #these values were trial numbers, but we need indices for 0-indexing issues here...
#        discard  = np.zeros(max(bdata.trialnum)).astype(int)
#        discard[discards] = 1 #mark trials that should be thrown out with a 1
        
        discards = np.append(array_throws, cue_throws)
        discards = np.unique(discards) #these are the actual trial ids, not the indices of the data. 
        discards = np.subtract(discards, 1) #so we subtract 1
        discard  = np.zeros(max(bdata.trialnum), dtype='int')
        discard[discards]=1

        print('%d trial(s) had blinks near to the array or cue being presented'%discard.sum())
        
        #save the behavioural data back to csv, with column for if there was a blink by the array or cue presentation
        bdata.to_csv(param['behaviour_blinkchecked'], index=False) 
        
    elif i in [3, 10, 19]: #subject 3 has one session of 8 blocks because of time constraints - s10 didn't want to do 2nd block
        
        #we're going to r 19, 20, 2ead in the raw data, filter it, epoch it around the array/cue triggers and check to see if there are blinks nearby
        raw = mne.io.read_raw_eeglab(input_fname = param['rawset_sess1'], montage = 'easycap-M1', eog = ['VEOG', 'HEOG'], preload=True)
        raw.set_montage('easycap-M1')
#        raw.filter(1,40, picks='eog')
        
        #epoching
        #here it's important to specify a dictionary that assigns each trigger to its own integer value
        #mne.events_from_annotations will assign each trigger to an ordered integer, so e.g. trig11 will be 2, but epoching 11 will include another trigger
        #this solves it
        event_id = {'1' : 1, '2':2,                 #array
                    '11':11,'12':12,'13':13,'14':14,#cue
                    '21':21,'22':22,'23':23,'24':24,#probe
                    '31':31,'32':32,'33':33,'34':34,#space
                    '41':41,'42':42,'43':43,'44':44,#click
                    '51':51,'52':52,'53':53,'54':54,#confprobe
                    '61':61,'62':62,'63':63,'64':64,#space
                    '71':71,'72':72,'73':73,'74':74,#click
                    '76':76,'77':77,'78':78,'79':79, #feedback
                    '254':254,'255':255}
        
        events_array = {'neutral':1, 'cued':2}
        events_cue = {'neutral/probeleft'  : 11,
                      'neutral/proberight' : 12,
                      'cued/probeleft'     : 13,
                      'cued/proberight'    : 14}
        events,_ = mne.events_from_annotations(raw, event_id = event_id)
        tmin, tmax = -0.25, 0.25
        baseline = (None,0)
        
        arraylocked = mne.Epochs(raw, events, events_array, tmin, tmax, baseline, reject_by_annotation=False, preload=True)
        cuelocked   = mne.Epochs(raw, events, events_cue, tmin, tmax, baseline, reject_by_annotation=False, preload=True)        
        bdata = pd.DataFrame.from_csv(path = param['behaviour_sess1'])
        arraylocked.metadata = bdata
        cuelocked.metadata   = bdata

        veog_array = np.squeeze(deepcopy(arraylocked).pick_channels(['VEOG']).get_data())
        veog_diffs_array = np.multiply(np.subtract(np.max(veog_array,1), np.min(veog_array,1)), 1e6)
        array_throws = np.add(np.squeeze(np.where(np.logical_and(sp.stats.zscore(veog_diffs_array)>=2,veog_diffs_array > 250))),1)
        
        veog_cue = np.squeeze(deepcopy(cuelocked).pick_channels(['VEOG']).get_data())
        veog_diffs_cue = np.multiply(np.subtract(np.max(veog_cue,1), np.min(veog_cue,1)), 1e6)
        cue_throws = np.add(np.squeeze(np.where(np.logical_and(sp.stats.zscore(veog_diffs_cue)>=2,veog_diffs_cue > 250))),1)


#        this is really for if you want to visually inspect every trial, which i've done in the past. the above section automates this though
#        arraylocked.plot(n_epochs=4, picks = ['eog'])
#        arraythrowouts = []
#        if len(arraylocked.metadata.trialnum) != len(bdata): #should be 320 trials in these datasets
#            for x,y in np.ndenumerate(bdata.trialnum): #loop over every trial id in the behavioural data
#                if y not in arraylocked.metadata.trialnum.tolist(): #check if the trial ids in behavioural data are in the eeg metadata
#                    arraythrowouts.append(y) #if not, this trial was discarded, so note down that this trial was discarded
#                    
#        cuelocked.plot(n_epochs=4, picks = ['eog'])
#        cuethrowouts = []
#        if len(cuelocked.metadata.trialnum) != len(bdata):
#            for x,y in np.ndenumerate(bdata.trialnum):
#                if y not in cuelocked.metadata.trialnum.tolist():
#                    cuethrowouts.append(y)
        
#        discards = np.concatenate([arraythrowouts, cuethrowouts]).astype(int)
#        discards = np.unique(discards) #take only uniques, in case a trial had a blink at both array and cue so we don't double it here
#        discards = np.subtract(discards, 1) #these values were trial numbers, but we need indices for 0-indexing issues here...
#        discard  = np.zeros(max(bdata.trialnum)).astype(int)
#        discard[discards] = 1 #mark trials that should be thrown out with a 1
        
        discards = np.append(array_throws, cue_throws)
        discards = np.unique(discards) #these are the actual trial ids, not the indices of the data. 
        discards = np.subtract(discards, 1) #so we subtract 1
        discard  = np.zeros(max(bdata.trialnum), dtype='int')
        discard[discards]=1

        print('%d trial(s) had blinks near to the array or cue being presented'%discard.sum())

        bdata['arraycueblink'] = discard
        
        #save the behavioural data back to csv, with column for if there was a blink by the array or cue presentation
        if i == 19:
            bdata.to_csv(param['behaviour_blinkchecked1'], index = False)
        else:
            bdata.to_csv(param['behaviour_blinkchecked'], index=False) 
        
    else: #subjects 4 onwards, with two sessions per participant
        for part in ['a', 'b']:
            if part == 'a':
                session = '1'
            if part == 'b':
                session = '2'
                
            print('- - - - - working on part %d- - - - -\n\n'%(int(session)))

                
            #we're going to read in the raw data, filter it, epoch it around the array/cue triggers and check to see if there are blinks nearby
            raw = mne.io.read_raw_eeglab(
                input_fname=param['rawset_sess'+str(session)],
                #montage = 'easycap-M1',
                eog=['VEOG', 'HEOG'], preload = True)
            raw.set_channel_types(mapping = dict(RM = 'misc'))
            chnames = np.asarray(raw.ch_names)
            chnamemapping = {}
            for x in range(len(chnames)):
                chnamemapping[chnames[x]] = chnames[x].replace('Z', 'z').replace('FP', 'Fp')
                
            raw.rename_channels(chnamemapping)
            if i == 26:
                raw.rename_channels(mapping = {'VEOG':'HEO', 'HEOG':'VEO'})
                raw.rename_channels(mapping = dict(HEO='HEOG', VEO = 'VEOG')) #in this subject, they were put in the wrong order!
            raw.set_montage('easycap-M1')
            #mont=mne.channels.read_montage('easycap-M1')
#            raw.set_eeg_reference(ref_channels=['RM'])
            raw.filter(1,40, picks='eog')
            
            #epoching
            #here it's important to specify a dictionary that assigns each trigger to its own integer value
            #mne.events_from_annotations will assign each trigger to an ordered integer, so e.g. trig11 will be 2, but epoching 11 will include another trigger
            #this solves it
            event_id = {'1' : 1, '2':2,                 #array
                        '11':11,'12':12,'13':13,'14':14,#cue
                        '21':21,'22':22,'23':23,'24':24,#probe
                        '31':31,'32':32,'33':33,'34':34,#space
                        '41':41,'42':42,'43':43,'44':44,#click
                        '51':51,'52':52,'53':53,'54':54,#confprobe
                        '61':61,'62':62,'63':63,'64':64,#space
                        '71':71,'72':72,'73':73,'74':74,#click
                        '76':76,'77':77,'78':78,'79':79, #feedback
                        '254':254,'255':255}
            
            #if you want to check instances of a trigger ...
            print(np.unique(raw.annotations.description))
            np.isin(raw.annotations.description, ['100007']).sum() #counts how many of them there are
            np.isin(raw.annotations.description, ['100008']).sum()
            np.isin(raw.annotations.description, np.array([1,2], dtype='str')).sum()
            np.isin(raw.annotations.description, np.add(np.array([11,12,13,14]),65).astype('str')).sum()
            
            if i == 12 or np.logical_and(i==13, part=='b') or i==15 or i == 16 or i == 17 or i == 20 or i == 21 or i == 22 or i == 26: #in these sessions, one of the 255 (100007) triggers was read as 100008 in each session, so lets rename
                trig2change = np.squeeze(np.where(raw.annotations.description=='100008'))
                raw.annotations.description[trig2change] = '100007'
            
            if i >= 11:
                #for some reason 255 trigger was read as '100007' in these subjects
                event_id = {'1' : 1, '2':2,'11':11,'12':12,'13':13,'14':14,'21':21,'22':22,'23':23,'24':24,
                            '31':31,'32':32,'33':33,'34':34,'41':41,'42':42,'43':43,'44':44,'51':51,'52':52,'53':53,'54':54,
                            '61':61,'62':62,'63':63,'64':64,'71':71,'72':72,'73':73,'74':74,'76':76,'77':77,'78':78,'79':79,'254':254,'100007':255}
                #this just relabels this 100007 trigger as 255 so it's aligned with other subjects
            events_array = {'neutral':1, 'cued':2}
            events_cue = {'neutral/probeleft'  : 11,
                          'neutral/proberight' : 12,
                          'cued/probeleft'     : 13,
                          'cued/proberight'    : 14}
            events,_ = mne.events_from_annotations(raw, event_id = event_id)
            tmin, tmax = -0.1, 0.25
            baseline = (None,0)
            
            arraylocked = mne.Epochs(raw, events, events_array, tmin, tmax, baseline, reject_by_annotation=False, preload=True)
            cuelocked   = mne.Epochs(raw, events, events_cue, tmin, tmax, baseline, reject_by_annotation=False, preload=True)        
            bdata = pd.DataFrame.from_csv(path = param['behaviour_sess'+session])
            arraylocked.metadata = bdata
            cuelocked.metadata   = bdata
            
            
            
            veog_array = np.squeeze(deepcopy(arraylocked).pick_channels(['VEOG']).get_data())
            veog_diffs_array = np.multiply(np.subtract(np.max(veog_array,1), np.min(veog_array,1)), 1e6)
            array_throws = np.asarray(np.add(np.squeeze(np.where(np.logical_and(sp.stats.zscore(veog_diffs_array)>=2,veog_diffs_array > 250))),1))
            
            veog_cue = np.squeeze(deepcopy(cuelocked).pick_channels(['VEOG']).get_data())
            veog_diffs_cue = np.multiply(np.subtract(np.max(veog_cue,1), np.min(veog_cue,1)), 1e6)
            cue_throws = np.asarray(np.add(np.squeeze(np.where(np.logical_and(sp.stats.zscore(veog_diffs_cue)>=2,veog_diffs_cue > 250))),1))
    
    
    #        this is really for if you want to visually inspect every trial, which i've done in the past. the above section automates this though
    #        arraylocked.plot(n_epochs=4, picks = ['eog'])
    #        arraythrowouts = []
    #        if len(arraylocked.metadata.trialnum) != len(bdata): #should be 320 trials in these datasets
    #            for x,y in np.ndenumerate(bdata.trialnum): #loop over every trial id in the behavioural data
    #                if y not in arraylocked.metadata.trialnum.tolist(): #check if the trial ids in behavioural data are in the eeg metadata
    #                    arraythrowouts.append(y) #if not, this trial was discarded, so note down that this trial was discarded
    #                    
    #        cuelocked.plot(n_epochs=4, picks = ['eog'])
    #        cuethrowouts = []
    #        if len(cuelocked.metadata.trialnum) != len(bdata):
    #            for x,y in np.ndenumerate(bdata.trialnum):
    #                if y not in cuelocked.metadata.trialnum.tolist():
    #                    cuethrowouts.append(y)
            
    #        discards = np.concatenate([arraythrowouts, cuethrowouts]).astype(int)
    #        discards = np.unique(discards) #take only uniques, in case a trial had a blink at both array and cue so we don't double it here
    #        discards = np.subtract(discards, 1) #these values were trial numbers, but we need indices for 0-indexing issues here...
    #        discard  = np.zeros(max(bdata.trialnum)).astype(int)
    #        discard[discards] = 1 #mark trials that should be thrown out with a 1
            
            discards = np.append(array_throws, cue_throws)
            discards = np.unique(discards) #these are the actual trial ids, not the indices of the data. 
            discards = np.subtract(discards, 1) #so we subtract 1
            discard  = np.zeros(max(bdata.trialnum), dtype='int')
            discard[discards]=1
    
            print('%d trial(s) had blinks near to the array or cue being presented'%discard.sum())
            
            bdata['arraycueblink'] = discard
            
            #save the behavioural data back to csv, with column for if there was a blink by the array or cue presentation
            bdata.to_csv(param['behaviour_blinkchecked'+session], index=False) 
       