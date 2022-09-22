import re
from search import *

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


def forward_deduce(kb):
    """
        Takes the string of a knowledge base containing propositional definite 
        clauses and returns a (complete) set of atoms (strings) that can be 
        derived (to be true) from the knowledge base.
    """
    result = []
    kb_clauses = list(clauses(kb))
    exhausted = False
    while not exhausted:
        exhausted = True
        for clause in kb_clauses:
            if clause[0] not in result:
                all_atoms = True
                for atom in clause[1]:
                    if atom not in result:
                        all_atoms = False
                if all_atoms:
                    result.append(clause[0])
                    exhausted = False
    return result


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return [x[1] for x in self.clauses if x[0] in self.query]
        
    def is_goal(self, node):
        " ** COMPLETE ** "
        return node == []

    def outgoing_arcs(self, tail_node):
        " ** COMPLETE ** "
        arcs = []
        for i in range(len(tail_node)):
            possible_replacements = [x[1] for x in self.clauses if x[0] == tail_node[i]]
            for replacement in possible_replacements:
                head = tail_node[:i] + list(replacement) + tail_node[i+1:]
                arcs.append(Arc(tail_node, head, None, None))
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


def main():

    kb = """
    a :- b.
    """

    query = {'c'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")


if __name__ == "__main__":
    main()