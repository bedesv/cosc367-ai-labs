inorder(leaf(X), [X]).
inorder(tree(Root, Left, Right), Traversal):- inorder(Left, LeftTraversal), 
    append(LeftTraversal, [Root], TempTraversal), 
    inorder(Right, RightTraversal), 
    append(TempTraversal, RightTraversal, Traversal).

test_answer :- inorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
               writeln(T).