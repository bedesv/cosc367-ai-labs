remove(_, [], []).
remove(X, [X|T], L):- remove(X, T, L).
remove(X, [H|T], [H|L]):- remove(X, T, L).

test_answer :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').