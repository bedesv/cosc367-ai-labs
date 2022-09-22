max(A, B, C):- A > B, C=A; B > A, C=B.
max([], _).
max([X], X).
max([X|L], M):- max(L, N), max(X, N, M).

test_answer :- 
    max([], M),
    writeln("Max of an empty list is undefined!").