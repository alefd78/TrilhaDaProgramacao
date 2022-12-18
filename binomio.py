

n = int(input("Infome um número N : "))
k = int(input("Infome um número K (Menor ou igual a N): "))
if(k <= n):

    def fatorial(n):

        fat = 1
        idx = 1

        while(idx <= n):
            fat = idx * fat
            idx = idx + 1
        return (fat)

    def numeroBinomial(n, k):

        return fatorial(n)//((fatorial(k) * (fatorial(n - k))))

    b = numeroBinomial(n, k)
    print(b)
else: print("K precisa ser menor ou igual a N")