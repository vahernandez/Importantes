# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given n numbers differs from 
# the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a 
# program that among the given n numbers finds one that is different in evenness.

# Input
# The first line contains integer n (3 ≤ n ≤ 100) — amount of numbers in the task. The second line contains n space-separated natural numbers, not exceeding 100. It is guaranteed, that exactly one of these numbers differs from the others in evenness.

# Output
# Output index of number that differs from the others in evenness. Numbers are numbered from 1 in the input order.

num = int(input())
numeros = [int(a) for a in input().split(" ")]
par = 0
impar = 0

for i in numeros:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
cont = 1
if par > impar:
    for k in numeros:
        if k % 2 != 0:
            print(cont)
            break
        else:
            cont +=1
else:
    for j in numeros:
        if j % 2 == 0:
            print(cont)
            break
        else:
            cont += 1

            
    