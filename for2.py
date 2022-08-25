import copy as cp

def linearProgramming(y1):
    ylag = cp.deepcopy(y1)
    y, x = __mergeSort(ylag, [i for i in range(len(ylag))])
    maxi = -1
    for i in y:
        lag = len(str(i).split(".")[1])
        if maxi < lag:
            maxi = lag
    p = []
    for i in y:
        p.append(round(i * (10 ** maxi)))
    n = len(p)
    z = sum(p) // 2 + 1
    mat1 = [[0 for j in range(n)] for i in range(z)]
    mat2 = [[0 for j in range(n)] for i in range(z)]
    for i in range(p[0], z):
        mat1[i][0] = p[0]
    for i in range(1, z):
        for j in range(1, n):
            if i - p[j] >= 0:
                if mat1[i][j - 1] <= (mat1[i - p[j]][j - 1] + p[j]):
                    mat1[i][j] = mat1[i - p[j]][j - 1] + p[j]
                    mat2[i][j] = j
                else:
                    mat1[i][j] = mat1[i][j - 1]
                    mat2[i][j] = mat2[i][j - 1]
            else:
                mat1[i][j] = mat1[i][j - 1]
                mat2[i][j] = mat2[i][j - 1]
    s = mat2[z - 1][n - 1]
    i = mat1[z - 1][n - 1]
    print(sum(p))
    print(i)
    print(z-i)
    v = [s]
    while i - p[s] > 0:
        i = i - p[s]
        s = mat2[i][s - 1]
        v.append(s)
    for i in range(len(v)):
        v[i] = x[v[i]]
    e = [v, []]
    for i in range(n):
        if i not in v:
            e[1].append(i)
    return e


def __mergeSort(y, x):
    if len(y) > 1:
        mid = len(y) // 2
        lefty = y[:mid]
        righty = y[mid:]
        leftx = x[:mid]
        rightx = x[mid:]

        # Recursive call on each half
        __mergeSort(lefty, leftx)
        __mergeSort(righty, rightx)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(lefty) and j < len(righty):
            if lefty[i] <= righty[j]:
                # The value from the left half has been used
                y[k] = lefty[i]
                x[k] = leftx[i]
                # Move the iterator forward
                i += 1
            else:
                y[k] = righty[j]
                x[k] = rightx[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(lefty):
            y[k] = lefty[i]
            x[k] = leftx[i]
            i += 1
            k += 1

        while j < len(righty):
            y[k] = righty[j]
            x[k] = rightx[j]
            j += 1
            k += 1
    return y, x
