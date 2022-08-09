mirror(leaf(X), leaf(Y)) :- X = Y.
mirror(tree(X, Y), tree(A, B)):- mirror(X, B), mirror(Y, A).
% All below cases are covered by these two rules as in order for them to
% be a mirror, they have to either both be a leaf, or both be a tree.

% mirror(tree(leaf(X), leaf(Y)), tree(leaf(A), leaf(B))):- X = B, Y = A.
% mirror(tree(X, leaf(Y)), tree(leaf(A), B)):- Y = A, mirror(X, B).
% mirror(tree(leaf(X), Y), tree(A, leaf(B))):- X = B, mirror(Y, A).


% Here we test that a single answer is found.

	
	
test_answer :-
    mirror(leaf(foo), leaf(foo)),
    write('OK').

test_answer :-
    write('Wrong answer!').