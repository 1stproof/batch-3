import cmath, math, mpmath as mp
v=-25/96
def V(w): return -(((w-1)**2-0.25)**2)/(4*w*(w-1)*(w-0.75))
def dV(w,h=1e-7): return (V(w+h)-V(w-h))/(2*h)
pts=[]
c1=(v+2)/2; r1=(2-v)/2
for k in range(1,4001): th=math.pi+math.pi*k/4000; pts.append(c1+r1*cmath.exp(1j*th))  # lower: from v (angle pi) through angle 3pi/2 to 2
c2=(2+1/8)/2; r2=(2-1/8)/2
for k in range(1,4001): th=math.pi*k/4000; pts.append(c2+r2*cmath.exp(1j*th)) # upper from 2 to 1/8
c3=0; r3=1/8
for k in range(1,4001): th=-math.pi*k/4000; pts.append(r3*cmath.exp(1j*th)) # from 1/8 lower to -1/8
for k in range(1,20001): y=math.tan(math.pi/2*k/20001*0.999999); pts.append(-1/8+1j*y)
# check order of crossings
w=0.25+0j; prev=v; ws=[w]
# initial step: near critical? V'(1/4)!=0
for z in pts:
    for sub in range(1,6):
        zz=prev+(z-prev)*sub/5
        for _ in range(30):
            w=w-(V(w)-zz)/dV(w)
        ws.append(w)
    prev=z
print('end w',ws[-1], 'last z', pts[-1])
def wind(path,a):
    tot=0
    for i in range(len(path)-1):
        tot+=cmath.phase((path[i+1]-a)/(path[i]-a))
    return tot/(2*math.pi)
loop=ws+[ws[-1]+(0.25-ws[-1])*k/100 for k in range(1,101)]
print('wind 0',wind(loop,0),'wind 1',wind(loop,1), 'max|w|',max(abs(x) for x in ws))
# simplicity crude check: min distance between non-adjacent points
import itertools
P=pts[::40]
md=min(abs(P[i]-P[j]) for i in range(len(P)) for j in range(i+3,len(P)) if abs(P[i])<50 and abs(P[j])<50)
print('min nonadjacent dist (subsampled)',md)
# lambda continuation
mp.mp.dps=20
def lam(tau):
    q=mp.exp(1j*mp.pi*tau); return (mp.jtheta(2,0,q)/mp.jtheta(3,0,q))**4
y0=mp.findroot(lambda y: lam(1j*y)-0.25, 1.28)
print('y0',y0)
tau=1j*y0; wsub=ws[::25]+[ws[-1]]
# stop slightly before end (w->0.75 fine, lambda regular there)
for x in wsub[1:]:
    for _ in range(20):
        h=mp.mpf('1e-8'); d=(lam(tau+h)-lam(tau-h))/(2*h)
        tau=tau-(lam(tau)-x)/d
print('tau end',tau,' expected', -2+1j/y0)
# 3/0 split: lift alpha through f from c2=4/11 along both branches
def f(z): return 1-11/(12*z)+1/(6*z*z)
def df(z): return 11/(12*z*z)-1/(3*z**3)
branches=[]
for sgn in [1,-1]:
    # start near c2: f-v ~ (f''/2)(z-c2)^2 ; step off along correct direction
    c2=4/11; z0=pts[0]
    f2=(df(c2+1e-6)-df(c2-1e-6))/2e-6
    z=c2+sgn*cmath.sqrt(2*(z0-v)/f2); path=[z]; prev=z0
    for zt in pts[1:]:
        for sub in range(1,6):
            zz=prev+(zt-prev)*sub/5
            for _ in range(30): z=z-(f(z)-zz)/df(z)
            path.append(z)
        prev=zt
    branches.append(path)
print('ends',branches[0][-1],branches[1][-1])
closed=branches[0]+branches[1][::-1]
for a in [1,0.25,4/11+0.0001]:
    print('wind about',a,wind(closed+[closed[0]],a))
