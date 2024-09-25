function [U,alpha,KK] = fwd_solver_eit2D(p,e,t,sigma,Ic,body)

% Computes the solution of the 2D forward EIT problem
% Sanwar Ahmad, suahmad@colostate.edu, Aug 2020
% INPUT
% p,t: mesh information, nodes and elements
% e: node on the boudary
% sigma: conductivity distribution at each nodes
% Ic: Input current
% body: structure, it contains information about source, CP, current
% vector, contact impedance, electrode length etc.
% OUTPUT
% alpha: potential distribution at p
% U or Vpred: simulated/computed voltages
% KK: Stiffness matrix
% % % % % % % % % % % % % % % % % % % % % % 

np = length(p(1,:));
nelec = body.NumSrc; % number of electrodes
npat = body.npat; % number of current patterns
% elecInd = elec_ind(body,p,e); % Find the electrode indices for the mesh p,t
U = zeros(nelec,npat); % inital voltage vector
%% Global Stiffness Matrix Assembly 
% ref: Ph.D. thesis, "ITERATIVE IMAGE RECONSTRUCTION FOR ELECTRICAL IMPEDANCE TOMOGRAPHY USING ADAPTIVE TECHNIQUES"
% by Taoran Li (2014) for more information


[K,C,D] = int_phij(p,t,e,sigma,body);
% injected current, must satisfy conservation of charge since
% no current is being injected into interior, F = 0
% Ic = body.current;

KK = [K C;C' D];% zeros(1,np) ones(1,nelec)]; % Block matrix

% Setting ground node
ng = reference(p); % index of the reference point near the center of the body
KK(ng,:) = 0; KK(:,ng) = 0; KK(ng,ng) = 1;


% Computing FEM solution
Fn = [zeros(np,npat); Ic];% zeros(1,npat)];

sol = KK\Fn;


alpha = sol(1:np,:);
beta = sol(np+1:end,:);
U = beta; % measured voltages

S = sum(U)/nelec;
adjust = zeros(nelec,npat);
for i = 1:nelec
    adjust(i,:) = S;
end
U = U - adjust;
U = reshape(U,nelec*npat,1);
end
