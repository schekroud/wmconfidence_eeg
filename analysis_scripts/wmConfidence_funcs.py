#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:25:35 2019

@author: sammi
"""

#functions that are going to be useful in analysis of eeg data in python
import os.path as op

def get_subject_info_wmConfidence(subject):
    
    param = {}
    
    if subject['loc']   == 'workstation':
        param['path']   = '/home/sammirc/Desktop/DPhil/wmConfidence/data'
    elif subject['loc'] == 'laptop': 
        param['path']   = '/Users/sammi/Desktop/Experiments/DPhil/wmConfidence/data'
    
    if subject['id'] == 1:
        param['subid']                  = 's01'
        param['behaviour']              = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S01_allData_preprocessed.csv')
        param['rawdata']                = op.join(param['path'], 'eeg/s01/wmConfidence_s01_12062019.cdt')
        param['rawset']                 = op.join(param['path'], 'eeg/s01/wmConfidence_s01_12062019.set')
        param['rawcleaned']             = op.join(param['path'], 'eeg/s01/wmConfidence_s01_icacleaned_raw.fif')
        param['raweyes']                = op.join(param['path'], 'eyes/s01/WMCS01.asc')
        param['cleanedeyes']            = op.join(param['path'], 'eyes/s01/wmConfidence_s01_preprocessed.pickle')
        param['behaviour_blinkchecked'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S01_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 2:
        param['subid']                  = 's02'
        param['behaviour']              = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S02_allData_preprocessed.csv')
        param['rawdata']                = op.join(param['path'], 'eeg/s02/wmConfidence_s02_12062019.cdt')
        param['rawset']                 = op.join(param['path'], 'eeg/s02/wmConfidence_s02_12062019.set')
        param['rawcleaned']             = op.join(param['path'], 'eeg/s02/wmConfidence_s02_icacleaned_raw.fif')
        param['raweyes']                = op.join(param['path'], 'eyes/s02/WMCS02.asc')
        param['cleanedeyes']            = op.join(param['path'], 'eyes/s02/wmConfidence_s02_preprocessed.pickle')
        param['behaviour_blinkchecked'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S02_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 3:
        param['subid']                  = 's03'
        param['behaviour_sess1']        = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S03_allData_preprocessed.csv')
        param['rawdata_sess1']          = op.join(param['path'], 'eeg/s03/wmConfidence_s03a_24062019.cdt')
        param['rawset_sess1']           = op.join(param['path'], 'eeg/s03/wmConfidence_s03a_24062019.set')
        param['rawcleaned_sess1']       = op.join(param['path'], 'eeg/s03/wmConfidence_s03a_icacleaned_raw.fif')
        param['raweyes_sess1']          = op.join(param['path'], 'eyes/s03/WMCS03a.asc')
        param['cleanedeyes_sess1']      = op.join(param['path'], 'eyes/s03/wmConfidence_s03a_preprocessed.pickle')
        param['behaviour_blinkchecked'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S03_blinkchecked_preprocessed.csv')
        
    
    if subject['id'] == 4:
        param['subid']                   = 's04'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S04a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg/s04/wmConfidence_s04a_24062019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg/s04/wmConfidence_s04a_24062019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg/s04/wmConfidence_s04a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes/s04/WMCS04a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes/s04/wmConfidence_s04a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S04a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S04b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg/s04/wmConfidence_s04b_24062019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg/s04/wmConfidence_s04b_24062019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg/s04/wmConfidence_s04b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes/s04/WMCS04b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes/s04/wmConfidence_s04b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S04b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 5:
        param['subid']                   = 's05'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S05a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg/s05/wmConfidence_s05a_25062019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg/s05/wmConfidence_s05a_25062019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg/s05/wmConfidence_s05a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes/s05/WMCS05a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes/s05/wmConfidence_s05a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S05a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S05b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg/s05/wmConfidence_s05b_25062019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg/s05/wmConfidence_s05b_25062019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg/s05/wmConfidence_s05b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes/s05/WMCS05b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes/s05/wmConfidence_s05b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S05b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 6:
        param['subid']                   = 's06'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S06a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg/s06/wmConfidence_s06a_26062019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg/s06/wmConfidence_s06a_26062019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg/s06/wmConfidence_s06a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes/s06/WMCS06a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes/s06/wmConfidence_s06a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S06a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S06b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg/s06/wmConfidence_s06b_26062019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg/s06/wmConfidence_s06b_26062019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg/s06/wmConfidence_s06b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes/s06/WMCS06b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes/s06/wmConfidence_s06b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S06b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 7:
        param['subid']                   = 's07'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S07a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg/s07/wmConfidence_s07a_26062019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg/s07/wmConfidence_s07a_26062019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg/s07/wmConfidence_s07a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes/s07/WMCS07a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes/s07/wmConfidence_s07a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S07a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S07b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg/s07/wmConfidence_s07b_26062019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg/s07/wmConfidence_s07b_26062019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg/s07/wmConfidence_s07b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes/s07/WMCS07b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes/s07/wmConfidence_s07b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S07b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 8:
        param['subid']                   = 's08'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S08a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s08a_17072019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s08a_17072019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s08a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS08a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s08a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S08a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S08b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s08b_17072019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s08b_17072019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s08b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS08b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s08b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S08b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 9:
        param['subid']                   = 's09'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S09a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s09a_18072019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s09a_18072019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s09a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS09a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s09a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S09a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S09b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s09b_18072019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s09b_18072019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s09b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS09b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s09b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S09b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 10:
        param['subid']                   = 's10'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S10_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s10a_18072019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s10a_18072019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s10a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS10a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s10a_preprocessed.pickle')
        param['behaviour_blinkchecked'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S10_blinkchecked_preprocessed.csv')
      
    if subject['id'] == 11:
        param['subid']                   = 's11'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S11a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s11a_02092019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s11a_02092019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s11a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS11a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s11a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S11a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S11b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s11b_02092019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s11b_02092019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s11b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS11b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s11b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S11b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 12:
        param['subid']                   = 's12'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S12a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s12a_03092019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s12a_03092019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s12a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS12a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s12a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S12a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S12b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s12b_03092019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s12b_03092019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s12b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS12b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s12b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S12b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 13:
        param['subid']                   = 's13'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S13a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s13a_04092019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s13a_04092019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s13a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS13a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s13a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S13a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S13b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s13b_04092019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s13b_04092019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s13b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS13b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s13b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S13b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 14:
        param['subid']                   = 's14'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S14a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s14a_04092019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s14a_04092019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s14a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS14a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s14a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S14a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S14b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s14b_04092019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s14b_04092019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s14b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS14b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s14b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S14b_blinkchecked_preprocessed.csv')
        
    if subject['id'] == 15:
        param['subid']                   = 's15'
        param['behaviour_sess1']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S15a_allData_preprocessed.csv')
        param['rawdata_sess1']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s15a_09092019.cdt')
        param['rawset_sess1']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s15a_09092019.set')
        param['rawcleaned_sess1']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s15a_icacleaned_raw.fif')
        param['raweyes_sess1']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS15a.asc')
        param['cleanedeyes_sess1']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s15a_preprocessed.pickle')
        param['behaviour_blinkchecked1'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S15a_blinkchecked_preprocessed.csv')

        param['behaviour_sess2']         = op.join(param['path'], 'datafiles/preprocessed_data/wmConfidence_S15b_allData_preprocessed.csv')
        param['rawdata_sess2']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s15b_09092019.cdt')
        param['rawset_sess2']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s15b_09092019.set')
        param['rawcleaned_sess2']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_s15b_icacleaned_raw.fif')
        param['raweyes_sess2']           = op.join(param['path'], 'eyes', param['subid'], 'WMCS15b.asc')
        param['cleanedeyes_sess2']       = op.join(param['path'], 'eyes', param['subid'], 'wmConfidence_s15b_preprocessed.pickle')
        param['behaviour_blinkchecked2'] = op.join(param['path'], 'datafiles/blinkchecked/wmConfidence_S15b_blinkchecked_preprocessed.csv')
        
        
    #these are coded in a way that we don't have to vary across ppts (it's consistent) so we don't need to repeat per subject
    param['arraylocked']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_arraylocked-epo.fif')
    param['arraylocked_tfr']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_arraylocked-tfr.h5')
    param['arraylocked_tfr_meta']   = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_arraylocked_metadata.csv')
    param['cuelocked']              = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_cuelocked-epo.fif')
    param['cuelocked_tfr']          = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_cuelocked-tfr.h5')
    param['cuelocked_tfr_meta']     = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_cuelocked_metadata.csv')
    param['probelocked']            = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_probelocked-epo.fif')
    param['probelocked_tfr']        = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_probelocked-tfr.h5')
    param['probelocked_tfr_meta']   = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_probelocked_metadata.csv')
    param['resplocked']             = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_resplocked-epo.fif')
    param['resplocked_tfr']         = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_resplocked-tfr.h5')
    param['resplocked_tfr_meta']    = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_resplocked_metadata.csv')
    param['fblocked']               = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_fblocked-epo.fif')
    param['fblocked_tfr']           = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_fblocked-tfr.h5')
    param['fblocked_tfr_meta']      = op.join(param['path'], 'eeg', param['subid'], 'wmConfidence_'+param['subid']+'_fblocked_metadata.csv')

    
    return param

def gesd(x, alpha = .05, p_out = .1, outlier_side = 0):
    import numpy as np
    import scipy.stats
    import copy
    
    '''
    Detect outliers using Generalizes ESD test
    based on the code from Romesh Abeysuriya implementation for OSL
      
    Inputs:
    - x : Data set containing outliers - should be a np.array 
    - alpha : Significance level to detect at (default = .05)
    - p_out : percent of max number of outliers to detect (default = 10% of data set)
    - outlier_side : Specify sidedness of the test
        - outlier_side = -1 -> outliers are all smaller
        - outlier_side = 0 -> outliers could be small/negative or large/positive (default)
        - outlier_side = 1 -> outliers are all larger
        
    Outputs
    - idx : Logicial array with True wherever a sample is an outlier
    - x2 : input array with outliers removed
    
    For details about the method, see
    B. Rosner (1983). Percentage Points for a Generalized ESD Many-outlier Procedure, Technometrics 25(2), pp. 165-172.
    http://www.jstor.org/stable/1268549?seq=1
    '''

    if outlier_side == 0:
        alpha = alpha/2
    
    
    if type(x) != np.ndarray:
        x = np.asarray(x)

    n_out = int(np.ceil(len(x)*p_out))

    if any(~np.isfinite(x)):
        #Need to find outliers only in non-finite x
        y = np.where(np.isfinite(x))[0] # these are the indexes of x that are finite
        idx1, x2 = gesd(x[np.isfinite(x)], alpha, n_out, outlier_side)
        # idx1 has the indexes of y which were marked as outliers
        # the value of y contains the corresponding indexes of x that are outliers
        idx = [False] * len(x)
        idx[y[idx1]] = True

    n      = len(x)
    temp   = x
    R      = np.zeros((1, n_out))[0]
    rm_idx = copy.deepcopy(R)
    lam    = copy.deepcopy(R)

    for j in range(0,int(n_out)):
        i = j+1
        if outlier_side == -1:
            rm_idx[j] = np.nanargmin(temp)
            sample    = np.nanmin(temp)
            R[j]      = np.nanmean(temp) - sample
        elif outlier_side == 0:
            rm_idx[j] = int(np.nanargmax(abs(temp-np.nanmean(temp))))
            R[j]      = np.nanmax(abs(temp-np.nanmean(temp)))
        elif outlier_side == 1: 
            rm_idx[j] = np.nanargmax(temp)
            sample    = np.nanmax(temp)
            R[j]      = sample - np.nanmean(temp)
        
        R[j] = R[j] / np.nanstd(temp)
        temp[int(rm_idx[j])] = np.nan
        
        p = 1-alpha/(n-i+1)
        t = scipy.stats.t.ppf(p,n-i-1)
        lam[j] = ((n-i) * t) / (np.sqrt((n-i-1+t**2)*(n-i+1)))
    
    #And return a logical array of outliers
    idx = np.zeros((1,n))[0]
    idx[np.asarray(rm_idx[range(0,np.max(np.where(R>lam))+1)],int)] = np.nan
    idx = ~np.isfinite(idx)
    
    x2 = x[~idx]

        
    return idx, x2 


def plot_AR(epochs, method = 'gesd', zthreshold = 1.5, p_out = .1, alpha = .05, outlier_side = 1):
    import seaborn as sns
    import pandas as pd
    import numpy as np
    import scipy.stats
    from matplotlib import pyplot as plt

    #Get data, variance, number of trials, and number of channels
    dat     = epochs.get_data()
    var     = np.var(dat, 2)
    ntrials = np.shape(dat)[0]
    nchan   = len(epochs.ch_names)

    #set up the axis for the plots
    x_epos  = range(1,ntrials+1)
    y_epos  = np.mean(var,1)
    y_chans = range(1,nchan+1)
    x_chans = np.mean(var,0)

    #scale the variances
    y_epos  = [x * 10**6 for x in y_epos]
    x_chans = [x * 10**6 for x in x_chans]

    #Get the zScore
    zVar = scipy.stats.zscore(y_epos)

    #save everything in the dataFrame
    df_epos           = pd.DataFrame({'var': y_epos, 'epochs': x_epos, 'zVar': zVar})
    df_chans          = pd.DataFrame({'var': x_chans, 'chans': y_chans})
    
    # Apply the artefact rejection method
    if method == 'gesd':
        idx,x2            = gesd(y_epos, p_out=p_out, alpha=alpha, outlier_side=outlier_side) #use the gesd to find outliers (idx is the index of the outlier trials)
        keepTrials        = np.ones((1,ntrials))[0]
        keepTrials[idx]   = 0
        title = 'Generalized ESD test (alpha=' + str(alpha) + ', p_out=' + str(p_out) + ', outlier_side=' + str(outlier_side) + ')'
    elif method == 'zScore':
        keepTrials        = np.where(df_epos['zVar'] > zthreshold, 0, 1)
        title = 'ZVarience threshold of ' + str(zthreshold)
    elif method == 'none':
        title = 'no additional artefact rejection '
        keepTrials        = np.ones((1,ntrials))[0]
    
    df_epos['keepTrial'] = keepTrials
    df_keeps = df_epos[df_epos['keepTrial'] == 1]
    print(str(ntrials - len(df_keeps)) + ' trials discarded')
    
    # get the clean data
    keep_idx    = np.asarray(np.where(keepTrials),int)
    clean_dat    = np.squeeze(dat[keep_idx])
    
    #recalculate the var for chan
    clean_var    = np.var(clean_dat, 2)
    x_chans_c    = np.mean(clean_var,0)
    x_chans_c    = [x * 10**6 for x in x_chans_c]

    df_chans_c   = pd.DataFrame({'var': x_chans_c, 'chans': y_chans})
    
    
    # Plot everything
    fig, axis = plt.subplots(2, 2, figsize=(12, 12))
    axis[0,0].set_ylim([0, max(y_epos) + min(y_epos)*2])
    axis[0,1].set_xlim([0, max(x_chans)+ min(x_chans)*2])
    axis[1,0].set_ylim([0, max(df_keeps['var'])+ min(df_keeps['var'])*2])
    axis[1,1].set_xlim([0, max(x_chans_c)+ min(x_chans_c)*2])

    axis[0,0].set_title(title)
    sns.scatterplot(x = 'epochs', y = 'var', hue = 'keepTrial', hue_order = [1,0], ax = axis[0,0], data = df_epos)
    sns.scatterplot(x = 'var', y = 'chans', ax = axis[0,1], data = df_chans)
    sns.scatterplot(x = 'epochs', y = 'var', ax = axis[1,0], data =df_keeps)
    sns.scatterplot(x = 'var', y = 'chans', ax = axis[1,1], data = df_chans_c)
    
    
    
    return axis, keep_idx 


def toverparam(alldata):
    import scipy as sp
    import numpy as np
    from scipy import stats
    '''
    function to conduct a t-test over all samples of multiple subject data, prevents repeating the same thing over and over again
    
    input data is a list of individual subject objects
    
    NB this doesn't really care whether it's betas or tstats, it just does shit
    
    output = the t stats over the parameter given (i..e goes from having a dimension of length nsubs to not having it as it runs across subs)
    '''
    
    ndata = np.array(len(alldata))
    indiv_data_shape = np.array(alldata[0].data.shape)
    newshape = np.append(ndata, indiv_data_shape)
    tmp = np.empty(shape = newshape)

    for i in range(ndata):
        tmp[i] = alldata[i].data
    toverparam = sp.stats.ttest_1samp(tmp, popmean = 0, axis = 0)
    
    return toverparam[0]


def smooth(signal, twin , method = 'boxcar'):
    '''
    
    function to smooth a signal. defaults to a 50ms boxcar smoothing (so quite small), just smooths out some of the tremor in the trace signals to clean it a bit
    can change the following parameters:
        
    twin    -- number of samples (if 1KHz sampling rate, then ms) for the window
    method  -- type of smoothing (defaults to a boxcar smoothing) - defaults to a boxcar    
    '''
    import scipy as sp
    from scipy import signal
    import numpy as np
    
    
    if method == 'boxcar':
        #set up the boxcar
        filt = sp.signal.windows.boxcar(twin)
    
    #smooth the signal
    if method == 'boxcar':
        smoothed_signal = np.convolve(filt/filt.sum(), signal, mode = 'same')
    
    return smoothed_signal