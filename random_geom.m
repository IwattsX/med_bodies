function [sigTrue,sigTrue1] = random_geom(p,p1,inArea,outArea,body)
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

% center1 = [(rc-2.5*el)*cos(pi/3) (rc-2.5*el)*sin(pi/3)];

% center1 = randomize_circle_position(el,body.rc)

% center2 = [(rc-2.5*el)*cos(pi+pi/4) (rc-2.5*el)*sin(pi+pi/4)];

% center1 = [0.115*cos(pi/3) 0.115*sin(pi/3)];
% center2 = [0.115*cos(pi+pi/4) 0.115*sin(pi+pi/4)];
radius = rand*el/.95 % size of the inclusion


r = (0.5 + 0.5 * rand) * (rc - radius) * 0.9; % Random distance from the center, ensuring the small circle stays within the larger one
theta = (0.5 + 0.5 * rand) * 2 * pi; % Random angle
x_random = r * cos(theta); % X-coordinate of the random center
y_random = r * sin(theta); % Y-coordinate of the random center
center1 = [x_random, y_random];


% radius = 0.012;

% radius = 0.02;

for i=1:nodes1
    if norm(center1'-p1(:,i))<=radius
        sigTrue1(i)=inArea;

    % elseif norm(center2'-p1(:,i))<=radius
    %     sigTrue1(i)= 0.02; %0.0005;
    % 
    else
        sigTrue1(i)=outArea; 
    end
end

for i=1:nodes
    if norm(center1'-p(:,i))<=radius
        sigTrue(i)=inArea;

    % elseif norm(center2'-p(:,i))<=radius
    %     sigTrue(i)= 0.02; %0.0005;
    % 
    else
        sigTrue(i)=outArea; 
    end
end