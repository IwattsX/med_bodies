%
clear, close all
format long;
%

%
idx = 100
load("scripts/dataCourseCSV/sig_data_predict.mat", "predicted_output")
figure;pdeplot(p,e,t,'xydata',predicted_output(idx, :),'mesh','on');colormap(jet);
%

%
load("dataSigCourse/sig_data_course.mat","sig_data_coarse")
figure;pdeplot(p,e,t,'xydata',sig_data_coarse(idx,:),'mesh','on');colormap(jet);
%