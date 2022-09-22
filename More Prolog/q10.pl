split_even([],[],[]).
split_even([X|Y], Z, [X|J]):- split_odd(Y, Z, J).
split_odd([],[],[]).
split_odd([X|Y], [X|Z], J):- split_even(Y, Z, J).
split_odd_even(X, Y, Z):- split_odd(X, Y, Z).

merge(X, [], X).
merge([], Y, Y).
merge([X|Y], [A|B], [X|Out]):- X < A,  merge(Y, [A|B], Out).
merge([X|Y], [A|B], [A|Out]):- A == X,  merge([X|Y], B, Out).
merge([X|Y], [A|B], [A|Out]):- A < X,  merge([X|Y], B, Out).

merge_sort([X], [X]).
merge_sort([], []).
merge_sort(X, Y):- split_odd_even(X, A, B), merge_sort(A, C), merge_sort(B, D), merge(C, D, Y).

test_answer :-
    merge_sort([4,3,1,2], L),
    writeln(L).