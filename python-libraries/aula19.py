import random

r_range = random.randrange(10, 20, 2)
print(r_range)
r_int = random.randint(10, 20)
print(r_int)
r_uniform = random.uniform(10, 20)
print(r_uniform)
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']



novos_nomes = random.sample(nomes, k=3)


novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)


print(random.choice(nomes))