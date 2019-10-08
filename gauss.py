from sympy import *
from numpy import sqrt
init_printing()

nvar = 1

errores = []
variables = []

var = input('Variable {}: '.format(nvar))
while var != '':
    dvar = float(input('Error de la variable {}: '.format(nvar)))
    j = symbols(var)
    exec('%s = j' % var)
    variables.append(var)
    errores.append(dvar)
    nvar += 1
    var = input('Variable {}: '.format(nvar))

nvar -= 1
g = symbols('g', cls = Function)

g = eval(input('\nIntroduce relación entre dichas variables'))

dgsquared = symbols('dg2')
dgsquared = 0

for i in range(nvar):
    dgsquared += (diff(g, variables[i])*errores[i])**2

print(dgsquared)
if input('Quieres evaluar el error?[s/n] ') == 's':
    valor_variables = ()
    for i in range(nvar):
        valor_variables += (float(input('Valor de la variable {}: '.format(variables[i]))), )
    dg = lambdify(variables, dgsquared)
    print(sqrt(dg(*valor_variables)))