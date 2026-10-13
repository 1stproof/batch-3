import sympy as sp, mpmath as mp, cmath, math
t,w,z=sp.symbols('t w z')
b=(t**2+t-1)/(1-t); c=t*(1-2*t)/(1-t)
f=1+b/z+c/z**2
print('cycle', [sp.simplify(e) for e in [f.subs(z,1)-t, sp.together(t**2*f.subs(z,t))]])
v=sp.simplify(1-b**2/(4*c))
print('v', sp.factor(v), sp.factor(v-1), sp.factor(v-t))
print('id', sp.expand((t**2+t-1)**2-(t**2-3*t+1)**2-4*t*(1-t)*(1-2*t)))
print('id2', sp.expand(9*t**4-18*t**3+15*t**2-6*t+1-(3*t**2-3*t+1)**2), sp.expand((t**2-3*t+1)**2+4*t**2*(1-t)*(1-2*t)))
q=sp.Rational(1,4)
print('t=1/4', b.subs(t,q), c.subs(t,q), -2*c.subs(t,q)/b.subs(t,q), v.subs(t,q))
V=-(((w-1)**2-t)**2)/(4*w*(w-1)*(w+t-1))
print('V_t(t)-v', sp.simplify(V.subs(w,t)-v))
print('num at 1-t', sp.factor((((w-1)**2-t)**2).subs(w,1-t)))
# deck
Vq=V.subs(t,q)
for g in [(w-sp.Rational(3,4))/(w-1), sp.Rational(3,4)/w]:
    print('deck', sp.simplify(Vq.subs(w,g)-Vq))
print('V(sqrt3/2)', sp.simplify(Vq.subs(w,sp.sqrt(3)/2)), sp.simplify(Vq.subs(w,-sp.sqrt(3)/2)))
print('crit', sp.factor(sp.numer(sp.together(sp.diff(Vq,w)))))
# Lemma 3.1 random check: build F= v'+z^2 etc
import random
for _ in range(3):
    tt=complex(random.random(),random.random()); vv=complex(random.random(),random.random())
    s2=cmath.sqrt(1-vv); s3=cmath.sqrt(tt-vv); s0=cmath.sqrt(-vv)
    ww=(s3-s2)/(s0-s2)
    Vn=complex(V.subs({t:tt,w:ww}).evalf())
    print('L3.1', abs(Vn-vv))
