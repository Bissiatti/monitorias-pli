from pulp import *

# problema
# maximizar o lucro 3A + 2B
# sujeito a
# Q: 2A + B <= 2
# R: A + 2B <= 2
# S: 3A + 3B <= 4

# cria um problema de otimização

prob = LpProblem("Questão 3.2", LpMaximize)

# cria as variáveis de decisão

A = LpVariable("A", 0, None)
B = LpVariable("B", 0, None)

# define a função objetivo

prob += 3 * A + 2 * B, "Lucro"

# define as restrições

prob += 2 * A + B <= 2, "Q"

prob += A + 2 * B <= 2, "R"

prob += 3 * A + 3 * B <= 4, "S"

# resolve o problema

prob.solve()

# exibe o status da solução

print("Status:", LpStatus[prob.status])

# exibe o valor ótimo

print("Lucro ótimo = ", value(prob.objective))

# exibe a solução ótima

for v in prob.variables():
    print(v.name, "=", v.varValue)

