from operation import*

a = 2
b = 4
c = 5
d = 6
e = 7
f = 9
g = 10
h = 12
i = 34

j = kali(b,d)
k = kurang(a, b)
l = jumlah(j, k)
print('a.',a, '+', b, 'x', d, '-', b,'=', l)
print('b.(',b, '+', e, ')x(', d, '-', f,')=', kali(jumlah(b, e),kurang(d, f)))
m = bagi(jumlah(g, a),jumlah(e, c))
n = bagi(m,kurang(h, i))
print('c.(',g, '+', a, ')/(', e, '+', c,')/(', h, '-', i, ')=', n)

