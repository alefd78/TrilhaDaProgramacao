n = int(input("Infome um número: "))

fat = 1
idx = 1

while(idx <= n):
    fat = idx * fat
    idx = idx + 1

print(fat)