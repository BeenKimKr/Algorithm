s = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in c:
    s = s.replace(i, 'x')
print(len(s))
