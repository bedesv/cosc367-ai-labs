from csp import *
import itertools

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x:v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment


if __name__ == "__main__":
    simple_csp = CSP(
        var_domains={x: set(range(1, 5)) for x in 'abc'},
        constraints={
            lambda a, b: a < b,
            lambda b, c: b < c,
            })

    solutions = sorted(str(sorted(solution.items())) for solution 
                    in generate_and_test(simple_csp))
    print("\n".join(solutions))