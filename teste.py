'''
x'(t) = x(t)(B1 − A1,1x(t) − A1,2y(t) − A1,3z(t))
y'(t) = y(t)(B2 − A2,1x(t) − A2,2y(t) − A2,3z(t))
z'(t) = z(t)(B3 − A3,1x(t) − A3,2y(t))

A =[[0.0010, 0.0010, 0.0150],[0.0015, 0.0010, 0.0010],[−α, −0.0005, 0.0000]]
B = [1,1,−1]

com 0.001 ≤ α ≤ 0.0055.

Analise o comportamento do retrato de fase do modelo com relação ao parâmetro α, escolhendo os
valores 0.001, 0.002, 0.0033, 0.0036, 0.005 e 0.0055. Inicie com 500 coelhos, 500 lebres e 10 raposas.
Nos dois primeiros casos, use tf = 100, nos dois seguintes tf = 500 e nos dois últimos tf = 2000.
Determine os casos em que há órbitas periódicas, equilíbrios estáveis ou instáveis.
'''

'''
### Método de Euler ###
Seja
x'(t) = f(t,x(t))

Discretização do problema:
x[i+1] = x[i] + h[i] * f(t,x(t))

Dicretização do domínio:
h = (tf-ti)/n
t[i+1] = t[i] + h
t[0] = ti
ou
t[i+1] = ti + h * i
'''

'''
### Método de Runge-Kutta Fehlberg 45 ###
Seja
x'(t) = f(t,x(t))

Discretização do problema
x_de_quarta_ordem[i+1] = x[i] + (25/216) * k1 + (1408/2565) * k3 + (2197/4104) * k4 − (1/5) * k5
x_de_quinta_ordem[i+1] = x[i] + (16/135) * k1 + (6656/12825) * k3 + (28561/56430) * k4 − (9/50) * k5 + (2/55) * k6

k1 = h * f(t[i], x[i])
k2 = h * f(t[i] + h/4, x[i] + k1 * 1/4)
k3 = h * f(t[i] + 3 * h/8, x[i] + k1 * 3/32  + k2 * 9/32)
k4 = h * f(t[i] + 12 * h/13, x[i] + k1 * 1932/2197 − k2 * 7200/2197 + k3 * 7296/2197)
k5 = h * f(t[i] + h, x[i] + k1 * 439/216 − k2 * 8 + k3 * 3680/513 − k4 * 845/4104)
k6 = h * f(t[i] + h/2, x[i] − k1 * 8/27 + k2 * 2 − k3 * 3544/2565 + k4 * 1859/4104 − k5 * 11/40)

Dicretização do domínio:
h = (tf-ti)/n
t[i+1] = t[i] + h, com i variando de 0 a n-1
t[0] = ti
ou
t[i+1] = ti + h * i, com i variando de 0 a n-1
'''

coelhos = 500
lebres = 500
raposas = 10

ti = 0
tf = 100
alfa = 0.001
#h=(tf-ti)/n
t[0] = ti