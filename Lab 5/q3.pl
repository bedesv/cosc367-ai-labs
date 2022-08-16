listtran([], []).
listtran([X|Y], [A|B]):- tran(X, A), listtran(Y, B).

tran(tahi,one). 
tran(rua,two). 
tran(toru,three). 
tran(wha,four). 
tran(rima,five). 
tran(ono,six). 
tran(whitu,seven). 
tran(waru,eight). 
tran(iwa,nine).

test_answer :-
    listtran(X, [one, seven, six, two]),
    writeln(X).