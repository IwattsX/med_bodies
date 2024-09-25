function Klocal = gradij(sig,x,y)
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
% Computing \int_Tm sig (grad phi_i) (grad phi_j) dx, over the mth tetrahedral
% element with conductivity sig

% x: x co-ordinates of the vetices of m-th element
% y: y co-ordinates of the vetices of m-th element
% Author: Sanwar Ahmad, suahmad@colostate.edu, July, 2020
% % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % 
h = 0.016; % height of saline water

b1 = -det([1 y(2);1 y(3)]);
b2 = det([1 y(1);1 y(3)]);
b3 = -det([1 y(1);1 y(2)]);

g1 = det([1 x(2);1 x(3)]);
g2 = -det([1 x(1);1 x(3)]);
g3 = det([1 x(1);1 x(2)]);


gradi = [b1 b2 b3;g1 g2 g3];
A = h*abs(det([1 x(1) y(1);1 x(2) y(2);1 x(3) y(3)]))/2;

Klocal = sig/(4 * A).*(gradi'*gradi);
end


