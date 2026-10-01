def bin_srch(a, i, l, x):
    # Base case: if the search range has only one element
    if l == i:
        if x == a[i]:
            return i
        else:
            return 0
    else:
        # Divide into smaller subproblem
        mid = (i + l) // 2

        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return bin_srch(a, i, mid - 1, x)
        else:
            return bin_srch(a, mid + 1, l, x)

if __name__ == "__main__":
    # Taking size of the array
    n = int(input("Give N: "))

    # Taking sorted elements (added 0 at index 0 to maintain 1-based indexing as per algorithm)
    print("Give sorted elements separated by space:")
    a = [0] + list(map(int, input().split()))

    # Value to search
    x = int(input("Give x: "))

    i = 1  # Starting index
    l = n  # Ending index

    result = bin_srch(a, i, l, x)

    if result != 0:
        print(f"{x} Found at Index: {result}")
    else:
        print(f"{x} Not Found.")