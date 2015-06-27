a = ['armi','goli','jug']
b = a.index('armi')
c = a.index('goli')
a[b],a[c] = a[c],a[b]

print a
