function Ic = trig_current(body,c)
% c: Amplitude of the current

nl = body.NumSrc; % number of source
npat = nl-1; % number of pattern
Ic = zeros(nl,npat);
theta = 2*pi/nl.*(1:nl); % electrode positions
% c = sqrt(2/nl);
% c = 0.005;

if mod(nl,2) == 1 % odd number of electrodes
    ns = nl-1;
else
    ns = nl;
end

for i = 1:ns/2
    Ic(:,i) = c*cos(i*theta);
end
% Ic(:,nl/2) = sqrt(1/nl)*cos(nl/2.*theta);
Ic(:,ns/2) = c*cos(nl/2*theta);
for i = (ns/2+1):npat
    Ic(:,i) = c*sin((i-ns/2)*theta);
%     Ic(:,i) = c*sin((nl-i)*theta);
end

%% For rearranging as low frequencies first, uncomment this block
% Use the low frequencies first cos, sin, cos2, sin2,..., sin15,cos16.
% temp = Ic;
% for i = 1:(nl/2)-1
%     Ic(:,2*i-1) = temp(:,i); 
%     Ic(:,2*i) = temp(:,(nl/2+i));
% end
% Ic(:,end) = temp(:,nl/2);
