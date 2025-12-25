# Pattern 1: Right-angled triangle
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# Pattern 2: Inverted triangle
for k in range(4):
    for l in range(4 - k):
        print("*", end=" ")
    print()
