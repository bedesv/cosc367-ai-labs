merge(X, [], X).
merge([], Y, Y).
merge([X|Y], [A|B], [X|Out]):- X < A,  merge(Y, [A|B], Out).
merge([X|Y], [A|B], [A|Out]):- A == X,  merge([X|Y], B, Out).
merge([X|Y], [A|B], [A|Out]):- A < X,  merge([X|Y], B, Out).

test_answer :-
    merge([3, 6, 7], [], L),
    writeln(L).