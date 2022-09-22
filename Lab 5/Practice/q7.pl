preorder(leaf(X), [X]).
preorder(tree(X, Y, Z), T) :- preorder(Y, J), append([X], J, K), preorder(Z, R), append(K, R, T).

test_answer :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T), 
               writeln(T).