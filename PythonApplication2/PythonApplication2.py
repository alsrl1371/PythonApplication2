
def Fibo(n):
    cnt[n]+=1
    if n==0: return 0
    elif n==1: return 1
    else:
        return Fibo(n-1)+Fibo(n-2)
    n=3
    cnt=[0,0,0,0,0]
    Fibonacci(n)
    for i in range(n,0,-1):


        print('Fibo(',i,')=',cnt[i])