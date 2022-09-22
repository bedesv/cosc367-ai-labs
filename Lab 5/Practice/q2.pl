swap12([X, Y|T], [Y, X|T]).

test_answer :-
    swap12(L, [b, a]),
    writeln(L).