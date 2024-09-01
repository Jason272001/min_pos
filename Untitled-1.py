A=[{'a': 2, 'b': 3},{'a': 4, 'b': 5},{'b': 2,'c': 10,'d':8,'e': 9}]
B={'a':2,'b':3,'c':1,'d':8,'e':4}

result = [{k: B.get(k, 0)*v for k, v in i.items() } for i in A]
print(result)