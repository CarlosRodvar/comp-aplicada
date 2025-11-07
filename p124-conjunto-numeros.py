# p124-conjunto-numeros.py
print ('\033[H\033[J')
print("--- Operaciones con Conjuntos de Números ---\n")

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

fmt = lambda s: "{ " + ", ".join(str(x) for x in sorted(s)) + " }"
vf  = lambda b: "Verdadero" if b else "Falso"

print("A =", fmt(A))
print("B =", fmt(B))
print("C =", fmt(C))

print("A | B =", fmt(A | B))
print("B | C =", fmt(B | C))
print("A - C =", fmt(A - C))
print("B ^ C =", fmt(B ^ C))
print("B & C =", fmt(B & C))

print("¿A ⊆ B? ->", vf(A.issubset(B)))
print("¿C ⊆ A? ->", vf(C.issubset(A)))
print("¿100 ∈ A? ->", vf(100 in A))
print("¿60 ∈ A, B y C? ->", vf(60 in A and 60 in B and 60 in C))
print("¿900 ∉ C? ->", vf(900 not in C))
