man(marcus).
pompeian(marcus).
roman(X):-pompeian(X).
ruler(caesar).
assasinate(marcus,caesar).
notloyalto(X,Y):-man(X),ruler(Y),assasinate(X,Y).
