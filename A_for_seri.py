n = int(input("Jep n: "))
shuma = 0
faktoriel = 1

for i in range(1, n + 1):
    shuma += i
    faktoriel *= i

if n == 0:
    faktoriel = 1  # 0! = 1

print("Shuma 1..n:", shuma)
print("Faktorieli i n:", faktoriel)
