from sympy import *
from sympy import sympify
import sympy as sp

function_question = input("""Select Function:
                            1) Cobb-Douglas
                            2) Max
                            3) Min
                            4) Quasi-Lineales
                            7) Start with Marshalls demand
                            6) Start with Hicksians demand
                            """)

def cobbDouglas():
    x1, x2, p1, p2, m = sp.symbols('x1 x2 p1 p2 m')
    text_function = input("""Please type function: """)
    utility_function = sp.sympify(text_function)
    # utility_function = x1**1*x2**1
    mux = utility_function.diff(x1)
    muy = utility_function.diff(x2)
    eq1 = sp.Eq(mux/muy, p1/p2)
    ans = sp.solve(eq1, x2)
    pres = p1*x1+x2*p2
    pres = pres.subs(x2, ans[0])
    pres = sp.Eq(m, pres)
    xMarshall = sp.solve(pres, x1)
    print("x^m_1= %s" % xMarshall[0])
    yMarshall = ans[0].subs(x1, xMarshall[0])
    print("x^m_2= %s" % yMarshall)


if int(function_question) == 1:
    cobbDouglas()