from sympy import *
from sympy import sympify
import sympy as sp
# import matplotlib.pyplot as plt
import numpy as np

function_question = input("""Select Function:
                            1) Cobb-Douglas
                            2) Linear
                            3) Max
                            4) Min
                            5) Quasilinear
                            6) Start with Marshallian demand
                            7) Start with Hicksian demand
                            8) Calculate variations and good type
                            9) Calculate effects {from} variations
                            """)


def cobbDouglas():
    x1, x2, p1, p2, m, u = sp.symbols('x1 x2 p1 p2 m u')
    text_function = input("""Please type function (Ex: x1^2 * x2^3): """)
    utility_function = sp.sympify(text_function)
    mux = utility_function.diff(x1)
    muy = utility_function.diff(x2)
    print("|RMS| = - %s / %s" % (mux, muy))
    eq1 = sp.Eq(mux / muy, p1 / p2)
    ans = sp.solve(eq1, x2)
    pres = p1 * x1 + x2 * p2
    # xGraph = np.linspace(-100, 100, 100)
    # yGraph = 2*xGraph
    pres = pres.subs(x2, ans[0])
    pres = sp.Eq(m, pres)
    xMarshall = sp.solve(pres, x1)
    print("x^m_1= %s" % xMarshall[0])
    yMarshall = ans[0].subs(x1, xMarshall[0])
    print("x^m_2= %s" % yMarshall)
    indirect_utility = utility_function.subs({x1: xMarshall, x2: yMarshall})
    print("v(p1,p2,m)= %s * Remember to substitute x1 with: %s *" % (indirect_utility, xMarshall))


    eq1 = sp.Eq(mux / muy, p1 / p2)
    ans = sp.solve(eq1, x2)
    utility_function = utility_function.subs(x2, ans[0])
    utility_function = sp.Eq(u, utility_function)
    xHicksian = sp.solve(utility_function, x1)
    print("h_1= %s" % xHicksian[0])
    yHicksian = ans[0].subs(x1, xHicksian[0])
    print("h_2= %s" % yHicksian)
    # the function, which is y = x^2 here

    # setting the axes at the centre
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.spines['left'].set_position('center')
    # ax.spines['bottom'].set_position('zero')
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')

    # plot the function
    # plt.plot(xGraph, yGraph, 'r')

    # show the plot
    # plt.show()


def linear():
    x1, x2, p1, p2, m = sp.symbols('x1 x2 p1 p2 m')
    text_function = input("""Please type function (Ex: 3*x1 + 2*x2): """)
    utility_function = sp.sympify(text_function)
    mux = utility_function.diff(x1)
    muy = utility_function.diff(x2)
    print("|RMS| = - %s / %s" % (mux, muy))
    if mux == 1 and muy == 1:
        print("A = [0;1]")
        print("""
            x^m_1 = {m/p_1          p_1<p_2
                    {m/p_1 * A      p_1=p_2
                    {0              p_1>p_2
            """)
        print("""
            x^m_2 = {0              p_1<p_2
                    {m/p_2 * (A-1)  p_1=p_2
                    {m/p_2          p_1>p_2
            """)
    else:
        print("A = [0;1]")
        print("""
            x^m_1 = {m/p_1          p_1/p_2 < %s / %s
                    {m/p_1 * A      p_1/p_2 = %s / %s
                    {0              p_1/p_2 > %s / %s
            """ % (mux, muy, mux, muy, mux, muy))
        print("""
            x^m_2 = {0              p_1/p_2 < %s / %s
                    {m/p_2 * (A-1)  p_1/p_2 = %s / %s
                    {m/p_2          p_1/p_2 > %s / %s
            """ % (mux, muy, mux, muy, mux, muy))
        print("""
            v =     {%sm/p_1                              p_1/p_2 < %s / %s
                    {%s(m/p_1 * A) - %s(m/p_2 * (A-1))    p_1/p_2 = %s / %s
                    {%sm/p_2                              p_1/p_2 > %s / %s
            """ % (mux, mux, muy, mux, muy, mux, muy, muy, mux, muy))

    next_step = input("""
                    1) Price relationship
                    99) Exit
                    """)
    if int(next_step) == 1:
        price_one = input("Whats the price of good one?   ")
        price_two = input("Whats the price of good two?   ")
        goods = int(mux) / int(muy)
        price = int(price_one) / int(price_two)
        if goods > price:
            print("Consumer buys everything of x1 and nothing of x2")
            print("%s > %s" % (goods, price))
        elif goods == price:
            print("Consumer is at indifference curve")
            print("%s = %s" % (goods, price))
        else:
            print("Consumer buys everything of x2 and nothing of x1")
            print("%s < %s" % (goods, price))
    else:
        exit()


def max():
    print("max")


def min():
    print("min")


def quasilinear():
    x1, x2, p1, p2, m = sp.symbols('x1 x2 p1 p2 m')
    text_function = input("""Please type function (Ex: ln(x1) + x2): """)
    utility_function = sp.sympify(text_function)
    mux = utility_function.diff(x1)
    muy = utility_function.diff(x2)
    print("|RMS| = - %s / %s" % (mux, muy))
    eq1 = sp.Eq(mux / muy, p1 / p2)
    ans = sp.solve(eq1, x2)
    print(ans[0])
    pres = p1 * x1 + x2 * p2
    pres = pres.subs(x2, ans[0])
    pres = sp.simplify(pres)
    xTwoMarshall = sp.Eq(pres, m)
    xTwoMarshall = sp.solve(xTwoMarshall, x1)
    print(xTwoMarshall)
    for i in text_function.split():
        if i == "ln(x1)":
            print("""
                x^m_1 = {m/p_1          p_1/p_2 < %s / %s
                        {m/p_1 * A      p_1/p_2 = %s / %s
                        {0              p_1/p_2 > %s / %s
                """ % (mux, muy, mux, muy, mux, muy))
            print("""
                x^m_2 = {0              p_1/p_2 < %s / %s
                        {m/p_2 * (A-1)  p_1/p_2 = %s / %s
                        {m/p_2          p_1/p_2 > %s / %s
                """ % (mux, muy, mux, muy, mux, muy))
            print("""
                v =     {%sm/p_1                              p_1/p_2 < %s / %s
                        {%s(m/p_1 * A) - %s(m/p_2 * (A-1))    p_1/p_2 = %s / %s
                        {%sm/p_2                              p_1/p_2 > %s / %s
                """ % (mux, mux, muy, mux, muy, mux, muy, muy, mux, muy))
        elif i == "ln(x2)":
            print("""
                x^m_1 = {m/p_1          p_1/p_2 < %s / %s
                        {m/p_1 * A      p_1/p_2 = %s / %s
                        {0              p_1/p_2 > %s / %s
                """ % (mux, muy, mux, muy, mux, muy))
            print("""
                x^m_2 = {0              p_1/p_2 < %s / %s
                        {m/p_2 * (A-1)  p_1/p_2 = %s / %s
                        {m/p_2          p_1/p_2 > %s / %s
                """ % (mux, muy, mux, muy, mux, muy))
            print("""
                v =     {%sm/p_1                              p_1/p_2 < %s / %s
                        {%s(m/p_1 * A) - %s(m/p_2 * (A-1))    p_1/p_2 = %s / %s
                        {%sm/p_2                              p_1/p_2 > %s / %s
                """ % (mux, mux, muy, mux, muy, mux, muy, muy, mux, muy))



if int(function_question) == 1:
    cobbDouglas()
elif int(function_question) == 2:
    linear()
elif int(function_question) == 3:
    max()
elif int(function_question) == 4:
    min()
elif int(function_question) == 5:
    quasilinear()
