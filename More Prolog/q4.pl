base(c, g).
base(g, c).
base(a, t).
base(t, a).

dna([], []).
dna([X|L], [Y|R]):- base(X, Y), dna(L, R).

test_answer :- dna(X, [t, a, g, c]),
               writeln(X).