function m = reference(p)
% Find the index of the reference point near the center of the body
center = [0;0];
m=1;
d = norm(p(:,m) - center,2);
n = size(p,2);
for i = 2:n
    d1 = norm(p(:,i) - center,2);
    if d1 < d
        m = i;
        d = d1;
    end
end