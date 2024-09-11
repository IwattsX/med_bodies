function [sigTrue,sigTrue1] = geom5(p,p1,inArea,outArea,body)
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
% Computes True conductivity distribution
% inside the daomain
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
nodes1=length(p1);
nodes=length(p);
rc = body.rc;
el = body.el;
% center1 = [-0.0508/1.4 0];center2 = [0.0508/1.4 0];

% center1 = [-0.0508/1.5 0];center2 = [0.0508/1.5 0];
% center1 = [0.03*cos(pi/3) 0.03*sin(pi/3)];
% center2 = [0.03*cos(pi+pi/4) 0.03*sin(pi+pi/4)];

center1 = [(rc-2.5*el)*cos(pi/3) (rc-2.5*el)*sin(pi/3)];
center2 = [(rc-2.5*el)*cos(pi+pi/4) (rc-2.5*el)*sin(pi+pi/4)];

% center1 = [0.115*cos(pi/3) 0.115*sin(pi/3)];
% center2 = [0.115*cos(pi+pi/4) 0.115*sin(pi+pi/4)];


% radius = 0.012;
radius = el/.95 % current experiment
% radius = 0.02;

for i=1:nodes1
    if norm(center1'-p1(:,i))<=radius
        sigTrue1(i)=inArea;
        
    elseif norm(center2'-p1(:,i))<=radius
        sigTrue1(i)= 0.02; %0.0005;
        
    else
        sigTrue1(i)=outArea; 
    end
end

for i=1:nodes
    if norm(center1'-p(:,i))<=radius
        sigTrue(i)=inArea;
        
    elseif norm(center2'-p(:,i))<=radius
        sigTrue(i)= 0.02; %0.0005;
        
    else
        sigTrue(i)=outArea; 
    end
end
