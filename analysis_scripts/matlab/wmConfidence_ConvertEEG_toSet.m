clear all
close all
restoredefaultpath;
clc

%%
eeglabpath = '/home/sammirc/eeglab14_1_1b';

wd = '/home/sammirc/Desktop/DPhil/wmConfidence';
chdir(wd);

addpath(genpath(eeglabpath));
addpath([ '/home/sammirc/Desktop/DPhil/wmConfidence/analysis_scripts/toolbox' ]);
%%

subs = [1 2 3 4 5 6 7];


for i = 1:length(subs)
    sub = subs(i);
    param = getSubjectInfo_wmConf(sub);
    %convert first session of data
    d = pop_loadcurry([param.path, param.rawdata]);
    pop_saveset(d, 'filename', param.rawset, 'filepath', param.path);
    clear d;
    if sub > 3; %most subjects have second session of data, so convert these too
        d = pop_loadcurry([param.path, param.rawdata2]);
        pop_saveset(d, 'filename', param.rawset2, 'filepath', param.path)
        clear d;
    end
end
