from itertools import permutations, combinations

names = ["Maricon", "Mavrick", "Geane"]
scores = [88, 72, 95]

# 1. ZIP(): combines each name with possible score
print("\n1. ZIP FUNCTION: -----------------------------------")
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# -----------------------------------------------------------

# 2. ANY() and ALL(): checks pass/fail conditions
passing_score = 75
print("\n2. ANY()/ALL() FUNCTION: ---------------------------")
print("Did anyone score below 75?      ", any(s < passing_score for s in scores))
print("Did everyone score at least 75? ", all(s >= passing_score for s in scores))

# -----------------------------------------------------------

# 3. ITERTOOLS: generate permutation and combination
print("\n3. ITERTOOLS MODULE: -------------------------------")
print("PERMUTATIONS: possible presentation orders")
for order in permutations(names):
    print(order)

print("\nCOMBINATIONS: possible 2-person study groups")
for group in combinations(names, 2):
    print(group)
