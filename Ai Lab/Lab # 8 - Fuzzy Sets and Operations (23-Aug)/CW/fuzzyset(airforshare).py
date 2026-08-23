A = [0.1, 0.4, 0.8]
B = [0.2, 0.3, 0.9]

# UNION
UNION = []

for i in range(len(A)):
    print(f"A={A[i]} B={B[i]} Max={max(A[i], B[i])}")
    UNION.append(max(A[i], B[i]))
    print("Union (A U B):", UNION)


# INTERSECTION
intersection = []

for i in range(len(A)):
    print(f"A{i}={A[i]} B{i}={B[i]} Min={min(A[i], B[i])}")
    intersection.append(min(A[i], B[i]))
    print("INTERSECTION (A ∩ B):", intersection)


# COMPLEMENT OF A
complement_A = []

for i in range(len(A)):
    print(f"A{i}={A[i]} complement={round(1 - A[i], 2)}")
    complement_A.append(round(1 - A[i], 2))
    print("Complement (A'):", complement_A)


# COMPLEMENT OF B
complement_B = []

for i in range(len(B)):
    complement_B.append(round(1 - B[i], 2))

print("Complement (B'):", complement_B)


# DIFFERENCE A - B
difference = []

for i in range(len(A)):
    value = min(A[i], 1 - B[i])
    difference.append(value)
    print(
        f"A{i}={A[i]} B{i}={B[i]} "
        f"1-B{i}={round(1 - B[i], 2)} "
        f"Difference={value}"
    )

print("Difference (A - B):", difference)