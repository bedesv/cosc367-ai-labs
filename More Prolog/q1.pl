reversed([], []).
reversed([X|T], J):- reversed(T, K), append(K, [X], J).

test_answer :- 
    reversed(L, [d, c, b, a]),
    writeln(L).