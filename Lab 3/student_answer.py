


def forward_deduce(knowledge_base):
    """
        takes the string of a knowledge base containing propositional definite clauses 
        and returns a (complete) set of atoms (strings) that can be derived (to be true) 
        from the knowledge base.
    """

    clauses_list = list(clauses(knowledge_base))
    

    true_atoms = [x[0] for x in clauses_list if x[1] == []]
    clauses_list = [x for x in clauses_list if x[1] != []]
    clause_selected = True
    while clause_selected:
        clause_selected = False
        for clause in clauses_list:
            if clause[0] not in true_atoms and all(x in true_atoms for x in clause[1]):
                clause_selected = True
                true_atoms.append(clause[0])
    return true_atoms


from search import *
import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        # return [x[0] for x in self.clauses if x[1] == []]
        return self.query
        
    def is_goal(self, node):
        " ** COMPLETE ** "
        return node == []

    def outgoing_arcs(self, tail_node):
        " ** COMPLETE ** "
        arcs = []
        for i in range(len(tail_node)):
            node = tail_node[i]
            parts = [x[1] for x in self.clauses if x[0] == node]

            for part in parts:
                new_body = (tail_node[:i] if tail_node[:i] != "" else []) + part + (tail_node[i+1:] if tail_node[i+1:] != "" else [])
                arcs.append(Arc(tail=tail_node, head=new_body, action=None, cost=None))

        return arcs

            


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration   # don't change this one
    

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a', 'b', 'd'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")

kb = """
all_tests_passed :- program_is_correct.
all_tests_passed.
"""

query = {'program_is_correct'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")


kb = """
a :- b.
"""

query = {'c'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")