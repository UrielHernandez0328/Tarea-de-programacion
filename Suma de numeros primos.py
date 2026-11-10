
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

suma = 0
num = 2

for num in range(2, 2000000):
     if es_primo(num):
         suma += num
    

print("la suma de los numeros primos es: ", suma)   







