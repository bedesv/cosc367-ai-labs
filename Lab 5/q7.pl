preorder(leaf(A), [A]).

preorder(tree(Root, Left, Right), Traversal):- preorder(Left, LeftTraversal), preorder(Right, RightTraversal), append([Root|LeftTraversal], RightTraversal, Traversal).

test_answer :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T), 
               writeln(T).