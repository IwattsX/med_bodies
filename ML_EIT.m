%%%%% Generating the random geometry
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% Sep 2024, Sanwar Uddin Ahmad, sahmad@vsu.edu, VSU
%%%%% iwatt1874@students.edu, VSU
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Creating mesh and true sigma model
% Initialize
clear, close all
format long;
%%

body.rc = 0.15; %0.15; % radius of the circle (m)
body.el = 0.02;
% Create geometry of boundary
cr = 1; %rc;
gd=[4; 0.0; 0.0; cr; cr; 0.0];
dl=decsg(gd); % circular geometry

%%%%%%%%%% MAKE SURE (number of bdy nodes) >= 2*number of electrodes %%%%%%%%%%
hval = 0.15;%0.15; %0.03; %0.2; 0.1: works for 32 electrode
% i.e., since El=0.005m, the number of nodes should be greater than or 
% equal to 64 nodes on the boundary 

% Create mesh
[p,e,t]=initmesh(dl,'hmax',hval); % create the mesh

[p,e,t]=refinemesh(dl,p,e,t); % coarser mesh
nodes=length(p);
[p1,e1,t1]=refinemesh(dl,p,e,t); % finer mesh
% Values
p1=p1*body.rc;
p=p*body.rc;
body.NumSrc = 32;
body.npat = 31;
body.zl = 1.2;
nodes1=length(p1);
tris=length(t1);

sigTrue=ones(nodes,1); %sigma at coarse mesh 
% sig = ones(nodes,1) + i 0.001.*ones(nodes,1);
sigTrue1=ones(nodes1,1); % sigma at finer mesh

inArea= 0.3; %0.03; %resistive 1e-8; color values (random)
outArea= 0.07; %.007;

%% Conductivity distribution
N = 1000;
sig_data = zeros(N,nodes1);
%% sig_data_coarse = zeros(N, nodes1);

for i = 1:N
[sigTrue,sigTrue1] = random_geom(p,p1,inArea,outArea,body);
sig_data(i,:) = sigTrue1;
sig_data_coarse(i,:) = sigTrue;
% sig0_fine = outArea.*ones(nodes1,1); % homogeneous conductivity
% sig0_coarse = outArea.*ones(nodes,1); % homogeneous conductivity
% figure;pdeplot(p1,e1,t1,'xydata',sigTrue1,'mesh','off');colormap(jet);pause
% close all;
end
%%
figure;pdeplot(p1,e1,t1,'xydata',sigTrue1,'mesh','on');colormap(jet);
figure;pdeplot(p,e,t,'xydata',sigTrue,'mesh','on');colormap(jet);
%%
single_data.sig = sig_data_coarse;

save('data/sig_data.mat',"sig_data")
load('data/sig_data.mat')
%%

save("data/sig_data_course.mat","sig_data_coarse")
%%
voltage_data = zeros(N,992);
for i = 1:N
Ic = trig_current(body,0.2); % input current

sigTrue1 = sig_data(i,:);


[U,~,~] = fwd_solver_eit2D(p1,e1,t1,sigTrue1',Ic,body);
voltage_data(i, :) = U;
end
%%

%%
save("data/voltage_data.mat", "voltage_data");
%%