"""
The distance function d for a given race duration r is a parametric function of (r,t) where t is the time waited between 0 and r

d(t,x) = (t - x) * x = tx - x^2
Plotting d vs. x we see this is a quadratic with roots x = 0, t
which means by symmetric the maxima is at x=t/2.

Or by calculus, maxima is where d(t,x) differentiated wrt x is 0
I.e. d'(t,x) = t - 2x  = 0
-> t = 2x
-> x = t/2

We are concerned with values of x, for a given t, for which d(t,x) > z (the previous record).

┌──────────────────────────────────────────────────────────────────┐
│   d(t,x)                                                         │
│    │                                                             │
│    │                                                             │
│    │                       maxima                                │
│    │                                                             │
│    │                      xxx xxx                                │
│    │                  xxxxx  │  xxxx                             │
│    │               xxxx             xx                           │
│    │            xxxx         │        xx                         │
│    │          xxx                      xx                        │
│    │        xxx              │          xxxx                     │
│  z ├ - - - - - - - - - - - - - -  - - - - - - - - - - d(t,x) = z │
│    │     xxx                               xx                    │
│    │   xxx                   │              xx                   │
│    │  xx                                     xx                  │
│    │ xx                      │                xx                 │
│    │xx                                         xx                │
│    │x                        │                  xx               │
│    │                                             x               │
├────│─────────────────────────┼───────────────────│──── x         │
│    0                        t/2                  t               │
└──────────────────────────────────────────────────────────────────┘

(Solving for x)
=>  z = tx - x^2
=>  x^2 - tx + z = 0
  { quadratic formula with a=1, b=-t, c=z}
=> x = 1/2 * t +/- sqrt(t^2 - 4z)

We care only about the number of values N between t/2 and t that are > z (times two, by symmetry !)
I.e. the integer value of x - t/2 for x at z

=>  N = 2 * (1/2 * (t + sqrt(t^2 - 4z)) - t/2)
=>  N = t + sqrt(t^2 - 4z) - t
=>  N = sqrt(t^2 - 4z)

"""
import math
import numpy as np


def solve(time, record):
    return math.floor(math.sqrt(time ** 2 - 4 * record))


if __name__ == '__main__':
    # part 1
    print(np.prod([solve(t, r) for t, r in [(62, 644), (73, 1023), (75, 1240), (65, 1023)]]))
    # part 2
    print(solve(62737565, 644102312401023))
