def list_of_squares(n):
    d = {0: 0}
    for i in range(1,n+1):
        d[i]=i*i
    return d