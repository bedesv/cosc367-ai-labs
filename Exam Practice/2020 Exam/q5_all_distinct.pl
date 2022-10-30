all_distinct([]).
all_distinct([_]).
all_distinct([X|T]):- \+member(X, T), all_distinct(T).

test_answer :- 
    \+all_distinct([a,b,c,b]),
    writeln("Wrong!").