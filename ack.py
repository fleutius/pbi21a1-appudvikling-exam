def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))

#print(ack(3,4))



def A(m, n, s ="% s"): 
    print(s % ("A(% d, % d)" % (m, n))) 
    if m == 0: 
        return n + 1
    if n == 0: 
        return A(m - 1, 1, s) 
    n2 = A(m, n - 1, s % ("A(% d, %% s)" % (m - 1))) 
    return A(m - 1, n2, s) 
  
print("\nResult = {}".format( A(3, 4)))