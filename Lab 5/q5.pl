remove(_, [], []).
remove(X, [X|T], L):- remove(X, T, L).
remove(X, [X|T], [X|L]):- \+ remove(X, T, L).
remove(X, [H|T], [H|L]):- remove(X, T, L).

test_answer :-
    \+ remove(a, [a,a,a], [a,a,a]),
    write('OK').
