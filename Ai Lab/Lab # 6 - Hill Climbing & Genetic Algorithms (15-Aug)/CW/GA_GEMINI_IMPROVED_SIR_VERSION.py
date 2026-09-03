# Short answer: 
# Agar aap sir ke bataye hue fixed numbers [10, 0, 8, 29] use kar rahe hain, toh sir wala code bilkul best hai kyunke wo pehli dafa mein hi answer le aayega. Lekin agar aap har dafa completely random numbers use karna chahte hain, toh mera wala code use karein taake code infinite loop mein na phase.





# Yahan main 3 differences hain:

# Initial Numbers (Step 1):

# Sir ka code: Fixed numbers use kar raha hai [10, 0, 8, 29].

# Mera code: Har dafa new random numbers banata hai.

# Best Number Dhoondna (Step 2):

# Sir ka code: reverse=True use karta hai, yani jo sab se bara number hoga (jaise 29) wo usko best manega.

# Mera code: abs(goal - x) use karta hai, yani jo number 30 ke sab se zyada qareeb hoga usko best manega.

# Mutation (Step 4):

# Sir ka code: child ^= 1 use karta hai, jo sirf number ki aakhri (last) bit ko change karta hai.

# Mera code: 1 << random_bit use karta hai, jo paancho (5) bits mein se kisi ko bhi randomly change kar sakta hai.

import random

# Step 1: Create initial population
population = [random.randint(0, 31) for _ in range(4)]
goal = 30

print("Initial population:", population)

generation = 0

while True:
    generation += 1

    # Step 2: Sort based on fitness (Jo number 30 ke sab se qareeb ho wo best hai)
    population.sort(key=lambda x: abs(goal - x))
    parent1, parent2 = population[0], population[1]

    # Step 3: Crossover (mix bits)
    child = (parent1 & 0b111100) | (parent2 & 0b000011)

    # Step 4: Better Mutation (Koi bhi random bit flip kare, sirf last wali nahi)
    if random.random() < 0.3:
        random_bit = random.randint(0, 4) # 5-bit number ke liye 0 se 4 tak koi bit select karein
        child ^= (1 << random_bit)

    # Step 5: Replace worst number
    population[-1] = child

    print(f"Gen {generation}: {population}")

    # Stop if we find 30
    if goal in population:
        print(f"Solution found in Generation {generation}!")
        break