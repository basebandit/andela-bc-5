def super_sum(*args):
    ''' Sums up the arguments
    '''
    total = 0
    for i in args:
        if isinstance(i, int):
            total += i
        else:
            total += super_sum(*i)

    return total

print(super_sum([10, 20, 30, 40], [100, 20]))
