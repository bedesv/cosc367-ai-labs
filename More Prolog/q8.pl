unique(X, X).
unique([X|T], [X|Y]):- not(member(X, T)), unique(T, Y).
unique([X|T], Y):- member(X, T), unique(T, Y).

test_answer :-
    unique([8,8],[8]),
    writeln('OK').