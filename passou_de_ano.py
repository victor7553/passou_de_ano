# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

materia1 = 4
materia2 = 5
materia3 = 7


if materia1 >= 7 and materia2 >= 7 and materia3 >= 7:
  print('você passou')
else:
  print('você não passou')   