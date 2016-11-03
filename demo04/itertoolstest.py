import itertools
na = itertools.repeat('A', 10)
for n in na:
    print n,

print '\n'
for c in itertools.chain('ABC', 'DEF'):
    print c,

print '\n'
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)
