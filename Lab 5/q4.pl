twice([], []).
twice([X | Y], [X, X | Z]):- twice(Y, Z).

test_answer :-
    \+ twice(L, [a, a, b]),
    writeln('OK').