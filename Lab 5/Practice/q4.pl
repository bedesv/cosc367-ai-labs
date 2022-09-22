twice([], []).
twice([X|T], [X, X|Q]):- twice(T, Q).

test_answer :-
    twice([], []),
    writeln('OK').