def arithgeo(arr):
    diff = arr[1] - arr[0]
    mult = arr[1] / arr[0]
    arithmetic = True
    for i in range(0, len(arr) - 1):
        if diff != (arr[i + 1] - arr[i]):
            arithmetic = False
            break
    if arithmetic:
        return "Arithmetic"
    for i in range(0, len(arr) - 1):
        if mult != (arr[i + 1] / arr[i]):
            return -1
    return "Geometric"
