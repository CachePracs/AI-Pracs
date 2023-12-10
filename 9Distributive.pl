isMale(jash).
isMale(jash).
isMale(jash).

isDoctor(jash).
isEngineer(jash).
isEngineer(jash).

lgetMarried(X):-(isMale(X),(isDoctor(X);isEngineer(X))).
rgetMarried(X):-((isMale(X),isDoctor(X));(isMale(X),isEngineer(X))).

