#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random as rd


# In[ ]:


player1 = str(input('Insert the name of player 1: '))
player2 = str(input('Insert the name of player 2: '))

legs = int(input('No. of Legs to win: '))

total1 = 501
total2 = 501
total3 = 1000
total4 = 1000
tails1 = 0
tails2 = 0

print(f'\nWelcome {player1} and {player2} in Darts World.')
print("Let's begin our play\n")

print(f"{player1}'s initial required score = {total1} and Legs = {tails1}")
print(f"{player2}'s initial required score = {total2} and Legs = {tails2}")

while True:
    print(f'\nFIRST TO {legs}')
    print(f"\n{player1}'s turn:")
    print('Required Score = ', total1)
    print('Legs = ', tails1)

    while(True):            
        d1 = int(input('\n1st dart score: '))
        if d1<=60:
            if (d1>20 and d1<41) and d1%2 == 0:
                total1 = total1-d1
                
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d1
                    total3 = total1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d1>20 and d1<61) and d1%3 == 0:
                total1 = total1-d1
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d1
                    total3 = total1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d1<=20):
                total1 = total1-d1
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d1
                    total3 = total1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d1 == 50 or d1 ==25):
                total1 = total1-d1
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d1
                    total3 = total1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            else:
                print('Wrong number you have selected. Please try again')
                pass 
        
        else:
            print('Wrong number you have selected. Please try again')
            pass

    while(True):
        if (total3-d1)<0:
            total3 = total1
            break
            
        if total1 == 0:
            break
            
        d2 = int(input('\n2nd dart score: '))
    
        if d2<=60:
            if (d2>20 and d2<41) and d2%2 == 0:
                total1 = total1-d2
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d2
                    total3 = total1
                    total1 = total1+d1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d2>20 and d2<61) and d2%3 == 0:
                total1 = total1-d2
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d2
                    total3 = total1
                    total1 = total1+d1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d2<21):
                total1 = total1-d2
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d2
                    total3 = total1
                    total1 = total1+d1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif d2 == 50 or d2 ==25:
                total1 = total1-d2
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+d2
                    total3 = total1
                    total1 = total1+d1
                    break
                else:
                    print('Required Score: ', total1)
                    break
            else:
                print('Wrong number you have selected. Please try again')
                pass
        
        else:
            print('Wrong number you have selected. Please try again')
            pass

    while(True):
        if (((total3-d1)<0) or ((total3-d2)<0)):
            total3 = total1
            break
        
        if total1 == 0:
            break
            
        d3 = int(input('\n3rd dart score: '))
    
        if d3<=60:
            if (d3>20 and d3<41) and d3%2 == 0:
                total1 = total1-d3
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d3>20 and d3<61) and d3%3 == 0:
                total1 = total1-d3
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif (d3<21):
                total1 = total1-d3
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total1)
                    break
            elif d3 == 50 or d3 ==25:
                total1 = total1-d3
                if total1<0:
                    print('\nYou can not score more than required!\n')
                    total1 = total1+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total1)
                    break
            else:
                print('Wrong number you have selected. Please try again')
                pass
        
        else:
            print('Wrong number you have selected. Please try again')
            pass
        
    
    if total1 == 0:
        tails1 = tails1+1
        total1 = 501
        total2 = 501
        total3 = 1000
        total4 = 1000
        print(f"\n{player1}'s Legs are {tails1}")
        print(f"All the player's required score is reset to {total1}")
       
    if tails1 == legs:
        print(f'\n{player1} wins')
        break
                
    print(f'\nFIRST TO {legs}')    
    print(f"\n{player2}'s turn:")
    print('Required Score = ', total2)
    print('Legs = ', tails2)

    while(True):            
        d1 = int(input('\n1st dart score: '))
        if d1<=60:
            if (d1>20 and d1<41) and d1%2 == 0:
                total2 = total2-d1
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d1
                    total4 = total2
                    break
                else:
                    print('Required Score: ', total2)                
                    break
            elif (d1>20 and d1<61) and d1%3 == 0:
                total2 = total2-d1
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d1
                    total4 = total2
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif (d1<21):
                total2 = total2-d1
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d1
                    total4 = total2
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif d1 == 50 or d1 ==25:
                total2 = total2-d1
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d1
                    total4 = total2
                    break
                else:
                    print('Required Score: ', total2)
                    break
            else:
                print('Wrong number you have selected. Please try again')
                pass 
        
        else:
            print('Wrong number you have selected. Please try again')
            pass

    while(True):
        if (total4-d1)<0:
            total4 = total2
            break
        
        if total2 == 0:
            break
            
        d2 = int(input('\n2nd dart score: '))
    
        if d2<=60:
            if (d2>20 and d2<41) and d2%2 == 0:
                total2 = total2-d2
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d2
                    total4 = total2
                    total2 = total2+d1
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif (d2>20 and d2<61) and d2%3 == 0:
                total2 = total2-d2
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d2
                    total4 = total2
                    total2 = total2+d1
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif (d2<21):
                total2 = total2-d2
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d2
                    total4 = total2
                    total2 = total2+d1
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif d2 == 50 or d2 ==25:
                total2 = total2-d2
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+d2
                    total4 = total2
                    total2 = total2+d1
                    break
                else:
                    print('Required Score: ', total2)
                    break
            else:
                print('Wrong number you have selected. Please try again')
                pass
        
        else:
            print('Wrong number you have selected. Please try again')
            pass

    while(True):
        if (((total4-d1)<0) or ((total4-d2)<0)):
            total4 = total2
            break
        
        if total2 == 0:
            break
            
        d3 = int(input('\n3rd dart score: '))
    
        if d3<=60:
            if (d3>20 and d3<41) and d3%2 == 0:
                total2 = total2-d3
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif (d3>20 and d3<61) and d3%3 == 0:
                total2 = total2-d3
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif (d3<21):
                total2 = total2-d3
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total2)
                    break
            elif d3 == 50 or d3 ==25:
                total2 = total2-d3
                if total2<0:
                    print('\nYou can not score more than required!\n')
                    total2 = total2+(d1+d2+d3)
                    break
                else:
                    print('Required Score: ', total2)
                    break
            else:
                print('Wrong number you have selected. Please try again')
                pass
        
        else:
            print('Wrong number you have selected. Please try again')
            pass
        
        
    if total2 == 0:
        tails2 = tails2+1
        total1 = 501
        total2 = 501
        total3 = 1000
        total4 = 1000
        print(f"\n{player2}'s Legs are {tails2}")
        print(f"All the player's required score is reset to {total2}")
            
    if tails2 == legs:
        print(f'\n{player2} wins')
        break