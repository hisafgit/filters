def filter_comb(n):
    flag = 0
    if n == 0:
        return [()]
    lst = []
    for i in [0,1]: # This list can be changed, e.g. [0,1,2]. Since it is a filter in my case, I did not use the list as an input to the function.
        if not flag:
            rl = filter_comb(n-1)
            flag = 1
        for j in rl:
            j += (i,)
            lst.append(j)
    return lst


