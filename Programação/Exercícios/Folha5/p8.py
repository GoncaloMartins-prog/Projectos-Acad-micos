n = int(input("nº inteiro >0: "))
def ehDivisor(n, num):
   """Determina se o primeiro número é divisor do segundo.

   Requires: n, num sejam int e n, num > 0
   Ensures: um bool que é True caso n seja divisor de num, False
   caso contrário.
   """
   return num % n == 0
def somaDivisoresProprios(n):
   """Soma dos divisores próprios de um número dado

   Requires: num seja int e num > 0
   Ensures: um int correspondente à soma dos divisores
   de num que sejam maiores que 1 e menores que num
   """
   s = 0
   i = 2
   for i in range (2, n):
       if ehDivisor(i, n):
           s += i
   return (s)

print("A soma dos seus divisores é: ", somaDivisoresProprios(n))
