function P = extrude(P1,P2,h,body)
% Translate midpoint of P1-P2 to P
% h: thickness

rc = body.rc;
th1 = atan2(P1(2),P1(1));
th2 = atan2(P2(2),P2(1));
th = (th1+th2)/2;

P = [(rc+h)*cos(th) (rc+h)*sin(th)];
end