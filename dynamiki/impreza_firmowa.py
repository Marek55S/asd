# problem imprezy firmowej
# ma byc najbardziej zabawowa impreza, ale nie mozna zaprosic jednoczescie przelozonego
# i jego bezposrednich podwladnych


class employee:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1


def f(v):
    if v.f >= 0:
        return v.f
    x = g(v)
    y = v.fun
    for u in v.emp:
        y += g(u)
    v.f = max(x, y)
    return v.f


def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g


v = employee(50)
w = employee(30)
x = employee(23)
v.emp.append(w)
v.emp.append(x)

print(f(v))
