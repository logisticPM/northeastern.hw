def BuildMatrix(R, n):
    M = [[0 for y in range(n)] for x in range(n)]
    for x in range(n):
        for y in range(n):
            M[x][y] = R(x, y)
    return M


# R1 is reflexive, symmetric, transitive
def R1(x, y):
    if (x - y) % 2 == 0:
        return 1
    else:
        return 0


# R2 is reflexive, symmetric, not transitive
def R2(x, y):
    if abs(x - y) <= 1:
        return 1
    else:
        return 0


# R3 is reflexive, not symmetric, transitive
def R3(x, y):
    if x == y or x > y:
        return 1
    else:
        return 0


# R4 is reflexive, not symmetric, not transitive
def R4(x, y):
    if x == y or (x > y and x % 2 == 0):
        return 1
    else:
        return 0


# R5 is not reflexive, symmetric, transitive
def R5(x, y):
    if x != 0 and y != 0 and x == y:
        return 1
    else:
        return 0


# R6 is not reflexive, symmetric, not transitive
def R6(x, y):
    if x != y and abs(x - y) == 2:
        return 1
    else:
        return 0


# R7 is not reflexive, not symmetric, transitive
def R7(x, y):
    if x > y:
        return 1
    else:
        return 0


# R8 is not reflexive, not symmetric, not transitive
def R8(x, y):
    if x > y and x % 2 == 0:
        return 1
    else:
        return 0


def EquivalenceTest(R, n):
    """
    Test if relation R is an equivalence relation.
    
    parameters:
        R: relation function
        n: size of domain to test
    """
    M = BuildMatrix(R, n)
    
    # Test reflexivity: check if M[x][x] = 1 for all x
    reflexive = True
    for x in range(n):
        if M[x][x] != 1:
            reflexive = False
            break
    
    # Test symmetry: check if M[x][y] = M[y][x] for all x,y
    symmetric = True
    for x in range(n):
        for y in range(n):
            if M[x][y] != M[y][x]:
                symmetric = False
                break
        if not symmetric:
            break
    
    # Test transitivity: if M[x][y]=1 and M[y][z]=1 then M[x][z]=1
    transitive = True
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if M[x][y] == 1 and M[y][z] == 1 and M[x][z] != 1:
                    transitive = False
                    break
            if not transitive:
                break
        if not transitive:
            break
    
    # Print results
    print("This relation is" + (" " if reflexive else " not ") + "reflexive")
    print("This relation is" + (" " if symmetric else " not ") + "symmetric")
    print("This relation is" + (" " if transitive else " not ") + "transitive")
    
    # If it's an equivalence relation, count equivalence classes
    if reflexive and symmetric and transitive:
        # Each row represents how an element relates to all others
        # Elements in same class have identical rows
        unique_rows = []
        for x in range(n):
            row = M[x]
            if row not in unique_rows:
                unique_rows.append(row)
        
        print("This relation is an equivalence relation and has",
              len(unique_rows), "equivalence classes.")
    else:
        print("This relation is not an equivalence relation.")


# Test the function
if __name__ == "__main__":
    print("\nTesting R1:")
    EquivalenceTest(R1, 10)