/* Initial state */
on(c,table).
on(b,c).
on(a,b).

clear(table).

clear(Block):-not(on(X,Block)).

goalReached():-
  on(a,table),
  on(c,a),
  on(b,c),
  write("\nGoal Reached Hurray !!!\n").

status(Y):-
  on(X,Y),
  write("\n"),
  write(X),
  write(" is on top of "),
  write(Y),
  write("\n"),
  status(X),
  on(Y,Z),
  write(Y),
  write(" is on top of "),
  write(Z),
  status(Z).

:-dynamic on/2.

put_on(A,B):-
  A \== table,
  A \== B,
  clear(A),
  clear(B),
  on(A,X),
  retract(on(A,X)),
  assert(clear(X)),
  assert(on(A,B)),
  assert(clear(A)),
  retract(clear(B)),
  write("\n"),
  write(A),
  write(" removed from "),
  write(X),
  write(", placed on top of "),
  write(B).
