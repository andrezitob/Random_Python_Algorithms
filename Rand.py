#1
%reset -f
#mínimo divisor comum algoritmo do livro: THE ART OF COMPUTER PROGRAMMING
b = 1
aa = b
bb = 0
a = bb
m = 45
n = 10
d = n
c = m
while(True):
  q = c // d
  r = c % d
  if r == 0:
    break
  c = d
  d = r
  t = aa
  aa = a
  a = t - q * a
  t = bb
  bb = b
  b = t - q * b
print(d)#mínimo divisor comum
print(a * m + b * n)#prova do mínimo divisor comum: se for igual a d, funciona

#1
%reset -f
#?(Euler Project)
#menor divisor comun
m = int(input())
n = int(input())
print(m%n)
r = 6699666
while(True):
  r = m % n
  if r != 0:
    m = n
    n = r
  else:
    break;
print(n)

#1
#verificação de CPF
%reset -f
print("Diga-me seu numero de CPF XXXXXXXXX-XX")
cpf = input()
i = 1
j = 10
j2 = 11
lcpf = []
soma = 0
soma2 = 0
valido = False
if len(cpf) != 12:
  print('CPF invalido "qtd digitos errado"')
else:
  for x in cpf:  
    if x == '-' and i != 10:
      print('CPF invalido "-"')
      break
    else:
      try:
        if i < 10:
          soma = soma + int(x) * j
          soma2 = soma2 + int(x) * j2
        elif i == 11:
          D = 11 - (soma % 11)
          
          if D > 9:
            D = 0
          if D == int(x):#check se o resultado confere com o digito verificador (10) dado pelo user
            print('digito 1 ok')
            soma2 = soma2 + D * 2
          else:
            print('CPF invalido "digito verificador errado"')
            break
        elif i == 12:
          D = 11 - (soma2 % 11)
          if D > 9:
            D = 0
          if D == int(x):#check se o resultado confere com o digito verificador (11) dado pelo user
            print('digito 2 ok')
            valido = True
          else:
            print('CPF invalido "digito 2 verificador errado"')
            break       
      except:
        print('CPF invalido "n composto totalmente de digitos"')
        break
    i = i + 1
    j = j - 1
    j2 = j2 - 1
if valido:
  print('CPF valido')
print("fim da execução")

#1
%reset -f
#sorting/arrumanado array/lista de menor a maior ¨¨desempenho¨¨
#modelo 1
#quantidade de loops depende dos itens do array "non stable"
#complexidade computacional ~= n^2/2.2
array = [1,2,3,4,5,6,7,8,9,10]
print(array)
lenn = len(array) - 2
tru = True
loops = 0
while tru:
  i = -1
  farse1 = True
  farse2 = True
  while i < lenn:
    loops = loops + 1#
    i = i + 2
    if array[i] < array[i - 1]:
      farse1 = False
      v = array[i]
      del array [i]
      array.insert(i - 1, v)
  i = 0
  while i < lenn:
    loops = loops + 1#
    i = i + 2
    if array[i] < array[i - 1]:
      farse2 = False
      v = array[i]
      del array [i]
      array.insert(i - 1, v)
  if farse1 and farse2:
    tru = False
print(array)
print('feito em',loops,'loops')

#1
%reset -f
#sorting array modelo 2
#esse modelo que de certa forma seguem um modelo decrescente mas "aleatorio" ex: 20, 16, 19, 12, 4, 13, 12, 10, 11, 7, 2, 6
#comparado ao modelo a cima, mesmo que a quantidade de loops seja parecida, a quantidade de instruções são um tiquinho menores aqui
#esse modelo tem uma quantidade de loops constante "stable"
import random as rd
%reset -f
#funcção array aleatório
def RandList(listalen,btwnminor,btwnmajor):#tamanho da lista, menor e maior numero possivel gerado aleatoriamente
  lista = []
  x = 0
  while x < listalen:
    r = rd.randint(btwnminor,btwnmajor)
    lista.append(r)
    x = x + 1
  return lista
#fim função


#nums = RandList(13,0,1000)
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
i = 0
j = 0
loops = 0
changed = False
while i < len(nums) - 1:
  a = nums[i]
  menor = a
  j = i + 1
  while j < len(nums):
    loops = loops + 1
    b = nums[j]
    if b < menor:
      menor = b
      posmenor = j
      changed = True
    j = j + 1
  if changed:
    nums[i] = menor
    nums[posmenor] = a
    changed = False
  i = i + 1
print('feito em',loops,'loops')

#1
%reset -f
import numpy as np
#multiplicação de várias matrizes ¨¨desempenho¨¨
#Ctrl + ENTER : run cell
#notas: para que duas matrizes sejam multiplicáveis, o n de colunas(j) da primeira deve ser igual ao numero de linhas(i) da segunda
#notas: as dimensões da matriz multiplicada será o n de linhas da primeira(i) pelo n de colunas da segunda(j) ex: 7X5 . 5X18 = 7X18
#A.B.C =  (A.B).C   ou   A.(B.C)
#notas: o numero de multiplicações que serão realizadas se dá pelo n de linhas x n colunas (i.j) da prim matriz x n de colunas da segunda (i1 x j1 x j2)
#        105 + 70   vs   30 + 42
 
*/A =  [[2,4,3],#7x3
      [5,1,1],
      [7,6,8],
      [7,4,6],
      [2,3,10],
      [1,3,13],
      [4,5,1]]
 
B = [[3,1,4,1,5],#3x5
     [9,2,6,5,3],
     [5,8,9,7,9]]
 
C = [[2,7],#5x2
     [1,8],
     [2,8],
     [1,8],
     [2,8]]
 
iA = len(A)
jA = len(A[0])
 
iB = len(B)
jB = len(B[0])
 
iC = len(C)
jC = len(C[0])
 
abc1 = iA * jA * jB + iA * jB * jC
abc2 = iB * jB * jC + iA * jA * jC
print('n de multiplicações AB.C',abc1)
print('n de multiplicações A.BC',abc2)
 
def MultMatrix(m1,m2):#matriz 1, matriz 2
  i1 = len(m1)
  j1i2 = len(m2) #ou len(m1[0]), pois são iguais
  j2 = len(m2[0])
  k = 0
  M = []
  p = 0
  q = 0
  r = 0
  soma = 0
  nmul = 0
  while p < i1:
    M.append([])
    while q < j2:
      while r < j1i2:
        soma = soma + m1[p][r] * m2[r][q]
        nmul = nmul + 1
        r = r + 1
      r = 0
      M[p].append(soma)
      soma = 0
      q = q + 1
    q = 0
    p = p + 1
  print('Multiplicações realizadas',nmul) 
  return M
 
#AB = MultMatrix(A,B)
#ABC = MultMatrix(AB,C)
#print('Resultado Mult A.B.C',ABC)
if jA == iB and jB == iC:
  if abc1 < abc2:
    AB = MultMatrix(A,B)
    ABC = MultMatrix(AB,C)
  else:
    BC = MultMatrix(B,C)
    ABC = MultMatrix(A,BC)
  print('Resultado Mult A.B.C',ABC)
else:
  print('Matrizes não compativeis para multiplicação')

#1
%reset -f
#soma de todos os primos entre 1 e 4000000 (essa é braba pro PC)(Euler Project)
x = 1
y = 1
z = 0
i = 0
sum = 0
while i < 4000000:
  x = y
  y = z
  z = x + y
  if z % 2 != 0:
    sum = sum + z
  i = i + 1
print(sum)

#1
%reset -f
#lista de todos os numeros primos entre 0 e 10001 (Euler Project)
nprimos = []
i = 1
j = 2
while i <= 10000:
  tru = True#tru dos tru
  while j < i and tru:
    if i % j == 0:
      tru = False
    else:      
      j = j + 1
  j = 2
  if tru:
    nprimos.append(i)
  i = i + 1
print(nprimos)
