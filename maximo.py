def maximo(n1,n2,n3):
    if(n1 >= n2 and n2 >= n3):
        return(n1)

    elif (n1 <= n2 and n2 <= n3):
        return(n3)

    else:
        return(n2)

