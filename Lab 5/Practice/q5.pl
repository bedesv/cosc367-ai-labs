remove(_, [], []).
remove(X, [X|T], Q) :- remove(X, T, Q).
remove(X, [R|T], [R|Q]) :- \+ R=X, remove(X, T, Q).

test_answer :-
    \+ remove(a, [a,a,a], [a,a,a]),
    writeln('OK'). 