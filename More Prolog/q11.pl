cartesian_helper(_, [], []).
cartesian_helper(X, [Y|T], [(X, Y) | Out]):- cartesian_helper(X, T, Out).
cartesian_product([], _, []).
cartesian_product([X|T], Y, Out):- cartesian_helper(X, Y, Temp), cartesian_product(T, Y, Temp2), append(Temp, Temp2, Out).

test_answer :- cartesian_product([a, b], X, 
                                 [(a,1), (a,2), (b,1), (b,2)]),
               writeln(X).