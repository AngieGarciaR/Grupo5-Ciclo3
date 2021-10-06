# # -*- coding: utf-8 -*-
# """
# Sumatoria
# """
# while True:
#     n = int(input("Digite el primer numero entero: "))
#     m = int(input("Digite el segundo numero entero, mayor que el anterior: "))
#     acum = 0
#     if m > n:
#         for i in range(n, m+1):
#             acum = acum + i
#         break
#     else:
#         print("El valor del segundo numero debe ser mayor al primero, intente nuevamente!")

# print('El valor de la sumatoria desde ', n, ' hasta ', m, 'es ', acum)

def suamtoria(n: int, m: int) -> int:
    acum = 0
    for i in range(n, m+1):
        acum += i
    return acum


n = int(input("Digite el primer numero entero: "))
m = int(input("Digite el segundo numero entero, mayor que el anterior: "))
x = suamtoria(n, m)
print(f'El valor de la sumatoria desde {n} hasta {m} es {x}')
