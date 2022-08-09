eats(X, Y) :- likes(X, Y).
eats(X, Y) :- hungry(X), edible(Y).

likes(alice, rock).
likes(alice, jazz).
edible(pizza).
hungry(bob).

test_answer :- eats(alice, rock),
               writeln('Alice eats rock!').