from csp import CSP

csp_instance = CSP(
   var_domains = {var:{1,1,3,4} for var in 'abcd'},
   constraints = {
      lambda a, b: a >= b,
      lambda a, b: b >= a,
      lambda a, b, c: c > a + b,
      lambda d: d <= d,
   }
)




if __name__ == "__main__":

    assert type(csp_instance) is CSP
    print(sorted(csp_instance.var_domains.keys()))
    print(len(csp_instance.constraints))