# Two fuzzy sets (membership values)
A = [0.1, 0.4, 0.8]
B = [0.2, 0.3, 0.9]


# 1. Union: μA∪B(x) = max(μA(x), μB(x))
union = []

for i in range(len(A)):
    print(f"A[{i}]={A[i]}  B[{i}]={B[i]}  Max={max(A[i], B[i])}")
    union.append(max(A[i], B[i]))

print("Union (A ∪ B):", union)


# 2. Intersection: μA∩B(x) = min(μA(x), μB(x))
intersection = []

for i in range(len(A)):
    print(f"A[{i}]={A[i]}  B[{i}]={B[i]}  Min={min(A[i], B[i])}")
    intersection.append(min(A[i], B[i]))

print("Intersection (A ∩ B):", intersection)


# 3. Complement of A
complement_A = []

for value in A:
    complement_A.append(round(1 - value, 2))

print("Complement (A'):", complement_A)


# 4. Complement of B
complement_B = []

for value in B:
    complement_B.append(round(1 - value, 2))

print("Complement (B'):", complement_B)


# 5. Difference (A - B)
# A - B = min(A, 1 - B)
difference = []

for i in range(len(A)):
    difference.append(round(min(A[i], 1 - B[i]), 2))

print("Difference (A - B):", difference)


# 6. Algebraic Product (A * B)
algebraic_product = []

for i in range(len(A)):
    algebraic_product.append(round(A[i] * B[i], 2))

print("Algebraic Product (A * B):", algebraic_product)


# 7. Algebraic Sum (A + B)
algebraic_sum = []

for i in range(len(A)):
    algebraic_sum.append(
        round(A[i] + B[i] - (A[i] * B[i]), 2)
    )

print("Algebraic Sum (A + B):", algebraic_sum)


# 8. Bounded Sum (A ⊕ B)
bounded_sum = []

for i in range(len(A)):
    bounded_sum.append(round
        (min(1, A[i] + B[i],2))
    )

print("Bounded Sum (A ⊕ B):", bounded_sum)


# 9. Bounded Difference (A ⊖ B)
bounded_difference = []

for i in range(len(A)):
    bounded_difference.append(
         max(0, A[i] - B[i],))
    

print("Bounded Difference (A ⊖ B):", bounded_difference)