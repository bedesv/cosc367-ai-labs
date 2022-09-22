binary_number_part([]).
binary_number([A,B|T]):- A = 0, B = 'b', \+ T = [], binary_number_part(T).
binary_number_part([0|T]):- binary_number_part(T).
binary_number_part([1|T]):- binary_number_part(T).

test_answer :- binary_number([0, b]),
               writeln('Wrong'), halt.
test_answer :- writeln('OK').