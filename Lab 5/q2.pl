swap12([X, Y | Tail], [Y, X | Tail]).
test_answer :-
    swap12(L1, L2),
    writeln('OK').