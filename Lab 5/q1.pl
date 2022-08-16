second([_,X|_], X).

test_answer :-
    second(L, X),
    writeln('OK').