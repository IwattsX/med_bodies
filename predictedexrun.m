clear, close all;

load('/home/iwatts/Documents/med_bodies/data/e1.mat')
load('/home/iwatts/Documents/med_bodies/data/p1.mat')
load('/home/iwatts/Documents/med_bodies/data/t1.mat')
load('/home/iwatts/Documents/med_bodies/scripts/sig_data.mat')
load('/home/iwatts/Documents/med_bodies/scripts/prediction_column_0.mat')

figure;pdeplot(p1,e1,t1,'xydata',predicted_output,'mesh','off');colormap(jet);
figure;pdeplot(p1,e1,t1,'xydata',sig_data(1,:),'mesh','off');colormap(jet);
