"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
def isPalindrome(x):
    med = str(x)
    num= list(med)
    pal = []
    dist = len(num)
    for i in num:
        pal.append(num[dist-1])
        dist -=1
    cuenta = 0
    y=0
    for i in num:
        for j in pal:
            if num[y]==pal[y]:
                cuenta+=0
            else:
                cuenta+=1
        y+=1   
    if cuenta == 0:
        return print("true")
    else:
        return print("false")
isPalindrome(121)