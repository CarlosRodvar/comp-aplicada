# p123-conjunto-personas.py
# Operaciones con conjuntos de personas
print ('\033[H\033[J')
print("--- Operaciones con Conjuntos de Personas ---\n")
lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)

def fmt(s):
    return "{ " + ", ".join(sorted(s)) + " }"

def vf(x):
    return "Verdadero" if x else "Falso"

print("A =", fmt(A))
print("B =", fmt(B))

print("Unión (A | B) =", fmt(A | B))
print("Intersección (A & B) =", fmt(A & B))
print("Diferencia (A - B) =", fmt(A - B))
print("Diferencia Simétrica (A ^ B) =", fmt(A ^ B))

print("{Pablo, Mateo} ⊆ B ->", vf({"Pablo", "Mateo"}.issubset(B)))
print("A ⊇ {Reynaldo, Angelica} ->", vf(A.issuperset({"Reynaldo", "Angelica"})))
print('"Pedro" ∈ A ->', vf("Pedro" in A))
print('"Lilia" ∉ B ->', vf("Lilia" not in B))
