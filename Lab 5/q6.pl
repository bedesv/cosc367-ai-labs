even([], [], []).
even([H|T], [H|A], B):- odd(T, A, B).

odd([], [], []).
odd([H|T], A, [H|B]):- even(T, A, B).

split_odd_even(T, A, B):- even(T, A, B).



test_answer :-
    split_odd_even([], A, B),
    write(A),
    writeln(B).