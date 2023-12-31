import itertools, copy
from csp import scope, satisfies, CSP


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in csp.var_domains}  # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]:  # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):  # COMPLETE
                    new_domain.add(xval)  # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime):  # COMPLETE
                        if x != z:  # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     # COMPLETE
    return csp


def generate_and_test(csp):
    """
        Takes a CSP object and returns an iterable (e.g. list, tuple, set, generator, ...) of solutions.
        A solution is a complete assignment that satisfies all the constraints.
    """
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = dict(zip(names, values))
        if all([satisfies(assignment, constraint) for constraint in csp.constraints]):
            yield assignment


domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1': {0, 1}, 'c2': {0, 1}, 'c3': {0, 1}})  # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda o, r, c1: o + o == r + 10 * c1,  # one of the constraints
        lambda w, u, c1, c2: w + w + c1 == u + 10 * c2,
        lambda t, o, c2, c3: t + t + c2 == o + 10 * c3,
        lambda f, c3: f == c3,
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == 6,  # length constraint
        lambda f: f != 0,
        lambda t: t != 0

    })


new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])
