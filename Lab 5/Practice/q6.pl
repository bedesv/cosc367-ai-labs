split_even([],[],[]).
split_even([X|Y], Z, [X|J]):- split_odd(Y, Z, J).
split_odd([],[],[]).
split_odd([X|Y], [X|Z], J):- split_even(Y, Z, J).
split_odd_even(X, Y, Z):- split_odd(X, Y, Z).

test_answer :-
    split_odd_even([], A, B),
    write(A),
    writeln(B).