from sympy import *
init_printing()
nvar = 1

class Variables_init:
    def __init__(self):
        errores = []
        variables = []
        parametros = []
        var = input('Variable {}: '.format(nvar))
        while var != '' :
            dvar = float(input('Error de la variable {}: '.format(var)))
            j = symbols(var)
            exec('%s = j' % var)
            variables.append(var)
            errores.append(dvar)
            nvar += 1
            var = input('Variable {}: '.format(nvar))

        nvar -= 1
        self.variables = variables
        self.errores = errores
        self.nvar = nvar

g = symbols('g', cls = Function)

try:
    g = eval(input('\nIntroduce relación entre dichas variables: '))
except:
    g = eval(input('\nParece que te has equivocado: '))

dgsquared = symbols('dg2')
dgsquared = 0

for i in range(nvar):
    dgsquared += (diff(g, variables[i])*errores[i])**2

pprint(sqrt(dgsquared))
valor_variables = ()


g = lambdify(variables, g)

for i in range(nvar):
    valor_variables += (float(input('Valor de la variable {}: '.format(variables[i]))), )
dg = lambdify(variables, dgsquared)

print('Tu magnitud es:', g(*valor_variables), '\nEl error de tu magnitud es:', sqrt(dg(*valor_variables)))
