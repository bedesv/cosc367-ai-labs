mirror(tree(X, Y), tree(V, Z)) :- mirror(X, Z), mirror(Y, V).
mirror(leaf(X), leaf(X)).

test_answer :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T).

test_answer :-
    write('Wrong answer!').
               