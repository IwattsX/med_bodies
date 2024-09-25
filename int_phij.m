function [K,C,D] = int_phij(p,t,e,sig,body)
% Input:
% p: nodes
% t: elements
% sigma: conductivity vector at each nodes
% Output:
% K: Global stiffness matrix for sigma
% % % % % % % % % % % % % % % % % % % % % 
% Sanwar Ahmad, suahmad@colostate.edu
% Last update: Aug 2020

nl = body.NumSrc;
np = length(p(1,:));
K = zeros(np,np); % K(i,j) = int_omega sig grad phi . grad phi dx
C = zeros(np,nl);
D = zeros(nl,nl);
nt = length(t(1,:));
h = 0.0001;
zl = body.zl; % contact impedance

if length(sig) == np
    sig1 = pdeintrp(p,t,sig);
else
    sig1 = sig;
end
% Find the global stiffness matrix
ntype = length(t(:,1))-1; % number of nodes in the element
for m = 1:nt
    
    x = p(1,t(1:3,m));
    y = p(2,t(1:3,m));
    
    Klocal = gradij(sig1(m),x,y); % local stiffness matrix at m-th triangular element
    for i = 1:ntype
        for j = 1: ntype
            K(t(i,m),t(j,m)) = K(t(i,m),t(j,m))+ Klocal(i,j);
        end
    end
end
% Integrating over the nelements on electrodes using triangles
elecInd = elec_ind(body,p,e);
for k = 1:nl
    el = elecInd(k).ind; % linear elements on kth electrode
    nel = size(el,2)-1; % number of elements on kth electrode
    for i = 1:nel
%       Coordinates of the vertices of the ith element on kth electrode
        P1 = [p(1,el(i)) p(2,el(i))];
        P2 = [p(1,el(i+1)) p(2,el(i+1))];
        
        P3 = extrude(P1,P2,h,body);
    
        x = [p(1,el(i+1)) p(1,el(i)) P3(1)];
        y = [p(2,el(i+1)) p(2,el(i)) P3(2)];
        
        
        Y = gradij(zl,x,y);
        
        K([el(i),el(i+1)],[el(i),el(i+1)]) = K([el(i),el(i+1)],[el(i),el(i+1)])+ Y(1:2,1:2); % update the global stiffness matrix
        C([el(i),el(i+1)],k) = C([el(i),el(i+1)],k) + Y([1,2],3);
        D(k,k) = D(k,k) + Y(3,3);
    end
    
    
end