donessc(siddh).
donehsc(siddh).
hadmathshsc(siddh).

lbscitadmission(X):-((donessc(X),donehsc(X)),hadmathshsc(X)).
rbscitadmission(X):-(donessc(X),(donehsc(X),hadmathshsc(X))).
