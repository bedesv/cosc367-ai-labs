new_append([], A, A).
new_append([A|B], C, [A|AB]):- new_append(B, C, AB).

test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).