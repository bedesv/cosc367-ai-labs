/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(Recommend, Age, Astigmatic, Rate):- young(Age), normal_tear_rate(Rate), Astigmatic = 'no', Recommend = 'soft_lenses'.
diagnosis(Recommend, Age, Astigmatic, Rate):- young(Age), normal_tear_rate(Rate), Astigmatic = 'yes', Recommend = 'hard_lenses'.
diagnosis(Recommend, Age, Astigmatic, Rate):- low_tear_rate(Rate), Recommend = 'no_lenses'.

test_answer :-
    diagnosis(X, 45, no, 4),
    writeln(X).