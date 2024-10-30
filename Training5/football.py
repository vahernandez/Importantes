"""
Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. To simplify the situation he depicted it 
as a string consisting of zeroes and ones. A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing 
one after another, then the situation is considered dangerous. For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. 
Determine whether it is dangerous or not.

Input
The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at 
least one player from each team present on the field.

Output
Print "YES" if the situation is dangerous. Otherwise, print "NO".

input 001001  output NO,   input 1000000001 output YES


team = [int(a) for a in input()]
counter = 0
counter2 = 0
n=0
x=0
for i in range(len(team)-1):
    y=x+1
    print(team[x], team[y])
    if x==0:
        if team[x]==1 and team[y]==1:
            counter +=1
        elif team[x]==0 and team[y]==0:
            counter +=1
       
    else:
        if (team[x] + team[y]) ==2:
            counter +=1
        elif (team[x] + team[y])==0:
            counter +=1
        else:
            counter = 0
    x+=1
    if counter == 7:
        print("YES")
        counter2 = 1

if counter2 !=1:
    print("NO")

"""


team = [int(a) for a in input()]
counter = 1
n=0
x=0
for i in range(len(team)-1):
    y=x+1
    if (team[x] + team[y]) ==2 or (team[x] + team[y]) ==0:
        counter +=1
    else:
        counter = 1
    x+=1
    n+=1
    if counter == 7:
        print("YES")
        break
    if n == (len(team)-1):
        print("NO")

        
        

        


