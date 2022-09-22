listtran([], []).
listtran([X|T], [Y|Q]):- tran(X, Y), listtran(T, Q).

test_answer :-
    listtran([], []),
    writeln('OK').