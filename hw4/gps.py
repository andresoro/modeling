import numpy as np
import scipy

c = 1

t1 = 100.52487
t2 = 87.505714
t3 = 115.00000

a1 = 2
b1 = -100
c1 = 1

a2 = 0
b2 = 88
c2 = -1

a3 = 0
b3 = 0.5
c3 = -115



system = np.array(
    [((2*(a2-a1)), (2*(b2-b1)), (2*(c2-c1))),
    ((2*(a3-a1)), (2*(b3-b1)), (2*(c3-c1)))
    ]
)

r1 = t1**2 - a1**2 - t2**2 + a2**2
r2 = t1**2 - a1**2 - t3**2 + a3**2

equals = np.array([(r1), (r2)])

sol = np.linalg.lstsq(system, equals)
print(system)
print(equals)
print(sol)