%% clear, close all;

load('/home/iwatts/Documents/med_bodies/data/e1.mat');
load('/home/iwatts/Documents/med_bodies/data/p1.mat');
load('/home/iwatts/Documents/med_bodies/data/t1.mat');

load('/home/iwatts/Documents/med_bodies/data/e.mat');
load('/home/iwatts/Documents/med_bodies/data/p.mat');
load('/home/iwatts/Documents/med_bodies/data/t.mat');

load('/home/iwatts/Documents/med_bodies/scripts/data/sig_data.mat');
load('/home/iwatts/Documents/med_bodies/scripts/predictions/sig_data_predict.mat');

figure;pdeplot(p,e,t,'xydata',predicted_output(1, :),'mesh','off');colormap(jet);
figure;pdeplot(p1,e1,t1,'xydata',sig_data(1,:),'mesh','off');colormap(jet);
