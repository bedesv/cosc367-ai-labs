solution(V1,V2,V3,H1,H2,H3):- 
    word(V1,_,A2,_,A4,_,A6,_), 
    word(V2,_,B2,_,B4,_,B6,_),
    word(V3,_,C2,_,C4,_,C6,_),
    word(H1,_,D2,_,D4,_,D6,_),
    word(H2,_,E2,_,E4,_,E6,_),
    word(H3,_,F2,_,F4,_,F6,_), 
    A2 = D2,
    A4 = E2,
    A6 = F2,
    B2 = D4,
    B4 = E4,
    B6 = F4, 
    C2 = D6,
    C4 = E6,
    C6 = F6.

word(abalone,a,b,a,l,o,n,e). 
word(abandon,a,b,a,n,d,o,n). 
word(enhance,e,n,h,a,n,c,e). 
word(anagram,a,n,a,g,r,a,m). 
word(connect,c,o,n,n,e,c,t). 
word(elegant,e,l,e,g,a,n,t).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!').