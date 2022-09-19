def f(s): return s[:len(s)//2].replace("n", "*") + s[len(s)//2:]
print(f(input()))
