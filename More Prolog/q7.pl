postorder(leaf(X), [X]).
postorder(tree(X, Y, Z), T):- postorder(Y, G), postorder(Z, F), append(G, F, K), append(K, [X], T).

test_answer :- postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).