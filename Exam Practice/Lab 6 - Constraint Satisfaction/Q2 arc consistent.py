from csp import CSP

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'across1': set("bus has".split()),
        'across3': set("lane year".split()),
        'across4': set("ant car".split()),
        # read down:
        'down1': set("buys hold".split()),
        'down2': set("search syntax".split()),
        },
    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
        })


from csp import CSP

csp_instance = CSP(
   var_domains = {
    'a':{1,2},
    'b':{1,2},
    'c':{3,4},
    'd':{1,2,3,4},

    },
   constraints = {
      lambda a, b: a >= b,
      lambda a, b: b >= a,
      lambda a, b, c: c > a + b,
      lambda d: d <= d,
   }
)

csp_instance = CSP(
   var_domains = {
    'a':{1,2,3,4},
    'b':{1,2},
    'c':{2,3,4},
    'd':{2,3,4},

    },
   constraints = {
      lambda b, c: b < c,
      lambda b, c, d: b * c == d,
   }
)