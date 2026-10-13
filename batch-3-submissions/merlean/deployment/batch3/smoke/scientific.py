import numpy as np, scipy.integrate, sympy as sp, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import fitz,pypdf
assert np.allclose(np.linalg.solve([[2.,0.],[0.,3.]],[4.,9.]),[2.,3.])
assert abs(scipy.integrate.quad(lambda x:x*x,0,1)[0]-1/3)<1e-12
x=sp.symbols('x');assert sp.expand((x+1)**2)==x*x+2*x+1
plt.plot([0,1],[0,1]);plt.savefig('/tmp/scientific-smoke.pdf')
assert len(pypdf.PdfReader('/tmp/scientific-smoke.pdf').pages)==1
with fitz.open('/tmp/scientific-smoke.pdf') as doc: assert len(doc[0].get_pixmap().samples)>0
print('SCIENTIFIC_PYTHON_PASS')
