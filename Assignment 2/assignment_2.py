# def is_val(o, f, l): return len(o) == 3 and o[0] in f and is_val(o[1], f, l) and is_val(o[2], f, l) if isinstance(o, list) else isinstance(o, int) or o in l 

# def depth(e): return 1 + max(depth(e[1]), depth(e[2])) if isinstance(e, list) else 0

# def ev(e, b): return e if isinstance(e, int) else (b[e] if isinstance(e, str) else b[e[0]](ev(e[1], b), ev(e[2], b)))

# def re(f, l, m): return l[__import__('random').randint(0, len(l) - 1)] if __import__('random').randint(0, 1) or m == 0 else [f[__import__('random').randint(0, len(f) - 1)], re(f, l, m-1), re(f, l, m-1)]
    
# def gr(i, e, l): b={'i': len(i),'x': i[-2],'y': i[-1],'*': lambda x, y: x * y,'-': lambda x, y: x - y,'+': lambda x, y: x + y};return [] if l <= 0 else ([ev(e, b)] if l == 1 else [ev(e, b)] + gr(i + [ev(e, b)], e, l-1))

# exec("def predict_rest(s):\n    while True:\n       e = re(['*','-','+'],  list(range(-2, 3)) + ['x', 'y', 'i'], 3)\n       if gr(s[:3], e, len(s) - 3) == s[3:]: return gr(s, e, 5)\n")
            

exec("def is_val(o, f, l): return len(o) == 3 and o[0] in f and is_val(o[1], f, l) and is_val(o[2], f, l) if isinstance(o, list) else isinstance(o, int) or o in l \ndef depth(e): return 1 + max(depth(e[1]), depth(e[2])) if isinstance(e, list) else 0\ndef ev(e, b): return e if isinstance(e, int) else (b[e] if isinstance(e, str) else b[e[0]](ev(e[1], b), ev(e[2], b)))\ndef re(f, l, m): return l[__import__('random').randint(0, len(l) - 1)] if __import__('random').randint(0, 1) or m == 0 else [f[__import__('random').randint(0, len(f) - 1)], re(f, l, m-1), re(f, l, m-1)]\ndef gr(i, e, l): b={'i': len(i),'x': i[-2],'y': i[-1],'*': lambda x, y: x * y,'-': lambda x, y: x - y,'+': lambda x, y: x + y};return [] if l <= 0 else ([ev(e, b)] if l == 1 else [ev(e, b)] + gr(i + [ev(e, b)], e, l-1))\ndef predict_rest(s):\n    while True:\n       e = re(['*','-','+'],  list(range(-2, 3)) + ['x', 'y', 'i'], 3)\n       if gr(s[:3], e, len(s) - 3) == s[3:]: return gr(s, e, 5)\n")

sequence = [31, 29, 27, 25, 23, 21]
print(predict_rest(sequence))
sequence = [0, 1, 4, 9, 16, 25, 36, 49]
print(predict_rest(sequence))
sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print(predict_rest(sequence))
sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
print(predict_rest(sequence))
sequence = [0, -1, 1, 0, 1, -1, 2, -1]
print(predict_rest(sequence))
sequence = [1, 3, -5, 13, -31, 75, -181, 437]
print(predict_rest(sequence))