import pickle

t = [1, 2, 3]
pickle.dumps(t)
t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print t2
