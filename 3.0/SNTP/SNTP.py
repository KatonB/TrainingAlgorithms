A = input()
B = input()
C = input()

h1, m1, s1 = map(int, A.split(':'))
h2, m2, s2 = map(int, C.split(':'))
h3, m3, s3 = map(int, B.split(':'))

sc = -1
mc = -1
hc = -1

if s2>=s1:
    sc = s2-s1
else:
    s2+=60
    m2-=1
    sc = s2-s1

if m2>=m1:
    mc = m2-m1
else:
    m2+=60
    h2-=1
    mc = m2-m1

if h2>=h1:
    hc = h2-h1
else:
    h2+=24
    hc = h2 - h1

temp = hc*3600+mc*60+sc
if temp%2 != 0:
    temp = temp//2+1
else:
    temp = temp // 2

while temp!=0:
    if temp>=3600:
        h3+=1
        temp-=3600
    if 3600>temp>=60:
        m3+=1
        temp-=60
    if 60>temp:
        s3+=temp
        temp = 0

    if s3>=60:
        coeff= s3//60
        m3 += coeff
        s3 -= 60*coeff
    if m3>=60:
        coeff= m3//60
        h3 += coeff
        m3 -= 60*coeff
    if h3>=24:
        h3 -= 24

h3, m3, s3 = str(h3), str(m3), str(s3)
if len(h3)==1:
    h3 = '0'+h3

if len(m3)==1:
    m3 = '0'+m3

if len(s3)==1:
    s3 = '0'+s3
print(h3 + ':' + m3 + ':' + s3)