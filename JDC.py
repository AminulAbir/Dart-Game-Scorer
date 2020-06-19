import random as rd
import numpy as np

# for choosing no. of players and their name
name_player = []
no_player = int(input("With how many players you want to practice?"))
for i in range(no_player):
    name_player.append(input(f"Enter Player {i + 1} Name: "))

# shows table for all player names
print("\nPLAYER NAMES")
for a in name_player:
    print(a)

# SHANGHAI 10-15
s1_total = [None] * no_player
s1_shots = np.arange(10, 16)
dict1 = {}

for j in range(no_player):
    sum_array = []
    print("""
    'S' for Single shots
    'D' for Double shots
    'T' for Triple shots
    Any key for for Missing shots
    """)
    print(f"\n{name_player[j]} turns: ")

    for k in range(len(s1_shots)):
        sums = 0
        print(f"Scoring for {s1_shots[k]}")

        d1 = input("Enter the 1st dart score: ").lower()
        if d1 == "s":
            sums += s1_shots[k]
        elif d1 == "d":
            sums += s1_shots[k] * 2
        elif d1 == "t":
            sums += s1_shots[k] * 3
        else:
            sums += 0

        d2 = input("Enter the 2nd dart score: ").lower()
        if d2 == "s":
            sums += s1_shots[k]
        elif d2 == "d":
            sums += s1_shots[k] * 2
        elif d2 == "t":
            sums += s1_shots[k] * 3
        else:
            sums += 0

        d3 = input("Enter the 3rd dart score: ").lower()
        if d3 == "s":
            sums += s1_shots[k]
        elif d3 == "d":
            sums += s1_shots[k] * 2
        elif d3 == "t":
            sums += s1_shots[k] * 3
        else:
            sums += 0

        if (d1 == "s" and d2 == "d" and d3 == "t") or (d1 == "s" and d2 == "t" and d3 == "d") or (
                d1 == "d" and d2 == "s" and d3 == "t") or (d1 == "d" and d2 == "t" and d3 == "s") or (
                d1 == "t" and d2 == "s" and d3 == "d") or (d1 == "t" and d2 == "d" and d3 == "s"):
            sums += 100

        sum_array.append(sums)

    dict1[j] = sum_array  # this is to printout each player scores individually
    s1_total[j] = sum(sum_array)

    # for creating table for each player if no of player is more than 1
    if no_player > 1:
        print()
        print(f"Name\t{s1_shots}\tTotal")
        print("---------------------------------------------")
        print(f"{name_player[j]}\t{dict1[j]}\t{s1_total[j]}")
        print()

# AROUND THE WORLD DOUBLES
s2_total = [None] * no_player
s2_shots = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 50)]
s2_shots_print = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, "BULL")]
dict2 = {}

for r in range(no_player):
    sum_array = []
    print("""
    'D' for Double shots + BULL shots    
    Any key for for Missing shots
    """)
    print(f"\n{name_player[r]} turns: ")

    for s in range(len(s2_shots)):
        sums = 0
        print(f"Scoring for {s2_shots[s]}")

        d1 = input("Enter the 1st dart score: ").lower()
        if d1 == "d":
            sums += 50
        else:
            sums += 0

        d2 = input("Enter the 2nd dart score: ").lower()
        if d2 == "d":
            sums += 50
        else:
            sums += 0

        if s == 6:
            d3 = input("Enter the 3rd dart score: (if you hit the BULL press 'D/d' else anything) ").lower()
            if d3 == "d":
                sums += 100
            else:
                sums += 0
        else:
            d3 = input("Enter the 3rd dart score: ").lower()
            if d3 == "d":
                sums += 50
            else:
                sums += 0

        sum_array.append(sums)

    dict2[r] = sum_array  # this is to printout each player scores individually
    s2_total[r] = sum(sum_array)

    # for creating table for each player if no of player is more than 1
    if no_player > 1:
        print()
        print(f"Name\t{s2_shots_print}\tTotal")
        print("---------------------------------------------")
        print(f"{name_player[r]}\t{dict2[r]}\t{s2_total[r]}")
        print()

# SHANGHAI 16-20
s3_total = [None] * no_player
s3_shots = np.arange(15, 21)
dict3 = {}

for x in range(no_player):
    sum_array = []
    print("""
    'S' for Single shots
    'D' for Double shots
    'T' for Triple shots
    Any key for for Missing shots
    """)
    print(f"\n{name_player[x]} turns: ")

    for y in range(len(s3_shots)):
        sums = 0
        print(f"Scoring for {s3_shots[y]}")

        d1 = input("Enter the 1st dart score: ").lower()
        if d1 == "s":
            sums += s3_shots[y]
        elif d1 == "d":
            sums += s3_shots[y] * 2
        elif d1 == "t":
            sums += s3_shots[y] * 3
        else:
            sums += 0

        d2 = input("Enter the 2nd dart score: ").lower()
        if d2 == "s":
            sums += s3_shots[y]
        elif d2 == "d":
            sums += s3_shots[y] * 2
        elif d2 == "t":
            sums += s3_shots[y] * 3
        else:
            sums += 0

        d3 = input("Enter the 3rd dart score: ").lower()
        if d3 == "s":
            sums += s3_shots[y]
        elif d3 == "d":
            sums += s3_shots[y] * 2
        elif d3 == "t":
            sums += s3_shots[y] * 3
        else:
            sums += 0

        if (d1 == "s" and d2 == "d" and d3 == "t") or (d1 == "s" and d2 == "t" and d3 == "d") or (
                d1 == "d" and d2 == "s" and d3 == "t") or (d1 == "d" and d2 == "t" and d3 == "s") or (
                d1 == "t" and d2 == "s" and d3 == "d") or (d1 == "t" and d2 == "d" and d3 == "s"):
            sums += 100

        sum_array.append(sums)

    dict3[x] = sum_array  # this is to printout each player scores individually
    s3_total[x] = sum(sum_array)

    # for creating table for each player if no of player is more than 1
    if no_player > 1:
        print()
        print(f"Name\t{s3_shots}\tTotal")
        print("---------------------------------------------")
        print(f"{name_player[x]}\t{dict3[x]}\t{s3_total[x]}")
        print()

# for creating table of all the player "SHANGHAI 10-15"
print()
print("SHANGHAI 10-15")
print(f"Name\t{s1_shots}\tTotal")
print("---------------------------------------------")
for m in range(no_player):
    print(f"{name_player[m]}\t{dict1[m]}\t{s1_total[m]}")

# for creating table of all the player "AROUND THE WORLD DOUBLES"
print()
print("AROUND THE WORLD DOUBLES")
print(f"Name\t{s2_shots_print}\tTotal")
print("-------------------------------------------------------------------------------------------------------------")
for n in range(no_player):
    print(f"{name_player[n]}\t{dict2[n]}\t\t\t\t\t\t\t\t\t{s2_total[n]}")

# for creating table of all the player "SHANGHAI 15-20"
print()
print("SHANGHAI 15-20")
print(f"Name\t{s3_shots}\tTotal")
print("---------------------------------------------")
for p in range(no_player):
    print(f"{name_player[p]}\t{dict3[p]}\t{s3_total[p]}")

# Overall Totals
st_total = []
print()
print("OVERALL TOTALS")
print("Name\t10-15\tATW\t15-20\tTotal")
print("---------------------------------------------")
for q in range(no_player):
    st_total.append(s1_total[q] + s2_total[q] + s3_total[q])
    print(f"{name_player[q]}\t{s1_total[q]}\t{s2_total[q]}\t{s3_total[q]}\t{st_total[q]}")

# Average Score Indicator
print()
print("AVERAGE SCORE INDICATOR")
print("""
Beginner = 0-300 pts
Improver = 301-450 pts
League Standard = 451-600 pts
League Division 1 Standard = 601-700 pts
Super League Standard = 701-850 pts
Country Standard = 851 pts +
""")
print()
print("Name\tPosition")
for z in range(no_player):
    if 0 <= st_total[z] <= 300:
        print(f"{name_player[z]}\tBeginner")
    elif 301 <= st_total[z] <= 450:
        print(f"{name_player[z]}\tImprover")
    elif 451 <= st_total[z] <= 600:
        print(f"{name_player[z]}\tLeague Standard")
    elif 601 <= st_total[z] <= 700:
        print(f"{name_player[z]}\tLeague Division 1 Standard")
    elif 701 <= st_total[z] <= 850:
        print(f"{name_player[z]}\tSuper League Standard")
    else:
        print(f"{name_player[z]}\tCountry Standard")