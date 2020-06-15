import random as rd


def recommend_func3(score):
    if score <= 40 and score % 2 == 0:
        print(f'{int(score / 2)}D')
    elif score <= 60 and score % 3 == 0:
        print(f'{int(score / 3)}T')
    elif score <= 20:
        print(score)
    elif score == 50:
        print('Bull')
    elif score == 25:
        print(score)


def recommend_func2(score):
    a = rd.randint(1, 61)
    b = rd.randint(1, 61)

    def randomized_number(a, b):

        if a <= 40 and a % 2 == 0:
            print(f'{int(a / 2)}D')
        elif a <= 60 and a % 3 == 0:
            print(f'{int(a / 3)}T')
        elif a == 50:
            print('Bull')
        else:
            print(a)

        if b <= 40 and b % 2 == 0:
            print(f'{int(b / 2)}D')
        elif b <= 60 and b % 3 == 0:
            print(f'{int(b / 3)}T')
        elif b == 50:
            print('Bull')
        else:
            print(b)

    if score <= 40 and score % 2 == 0:
        print(f'{int(score / 2)}D')
    elif score <= 60 and score % 3 == 0:
        print(f'{int(score / 3)}T')
    elif score <= 20:
        print(score)
    elif score == 50:
        print('Bull')
    elif score == 25:
        print(score)
    else:
        while True:
            if ((a + b == score) and (((((40 < a <= 60) and a % 3 == 0) or a == 50) and (
                    ((40 < b <= 60) and b % 3 == 0) or b == 50)) or ((
                                                                             a == 1 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 25 or (
                                                                             (
                                                                                     0 < a <= 40) and (
                                                                                     a % 2 == 0 or a % 3 == 0))) and (
                                                                             b == 1 or b == 5 or b == 7 or b == 11 or b == 13 or b == 17 or b == 19 or b == 25 or (
                                                                             (0 < b <= 40) and (
                                                                             b % 2 == 0 or b % 3 == 0))))) and (
                    a <= 60 and b <= 60)):
                randomized_number(a, b)
                break
            else:
                a = rd.randint(1, 61)
                b = rd.randint(1, 61)


def recommend_func(score):
    if score > 60:
        a = rd.randint(1, 61)
        b = rd.randint(1, 61)
        c = rd.randint(1, 61)
    else:
        a = rd.randint(1, score + 1)
        b = rd.randint(1, score + 1)
        c = rd.randint(1, score + 1)

    def randomized_number(a, b, c):

        if a <= 40 and a % 2 == 0:
            print(f'{int(a / 2)}D')
        elif a <= 60 and a % 3 == 0:
            print(f'{int(a / 3)}T')
        elif a == 50:
            print('Bull')
        else:
            print(a)

        if b <= 40 and b % 2 == 0:
            print(f'{int(b / 2)}D')
        elif b <= 60 and b % 3 == 0:
            print(f'{int(b / 3)}T')
        elif b == 50:
            print('Bull')
        else:
            print(b)

        if c <= 40 and c % 2 == 0:
            print(f'{int(c / 2)}D')
        elif c <= 60 and c % 3 == 0:
            print(f'{int(c / 3)}T')
        elif c == 50:
            print('Bull')
        else:
            print(c)

    if score <= 40 and score % 2 == 0:
        print(f'{int(score / 2)}D')
    elif score <= 60 and score % 3 == 0:
        print(f'{int(score / 3)}T')
    elif score <= 20:
        print(score)
    elif score == 50:
        print('Bull')
    elif score == 25:
        print(score)
    else:
        while True:
            if ((a + b + c == score) and (((((40 < a <= 60) and a % 3 == 0) or a == 50) and (
                    ((40 < b <= 60) and b % 3 == 0) or b == 50) and (
                                                   ((40 < c <= 60) and c % 3 == 0) or c == 50)) or ((
                                                                                                            a == 1 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 25 or (
                                                                                                                                                      (
                                                                                                                                                              0 < a <= 40) and (
                                                                                                                    a % 2 == 0 or a % 3 == 0))) and (
                                                                                                            b == 1 or b == 5 or b == 7 or b == 11 or b == 13 or b == 17 or b == 19 or b == 25 or (
                    (
                            0 < b <= 40) and (
                                                                                                                    b % 2 == 0 or b % 3 == 0))) and (
                                                                                                            c == 1 or c == 5 or c == 7 or c == 11 or c == 13 or c == 17 or c == 19 or c == 25 or (
                                                                                                            (
                                                                                                                    c > 0 and c <= 40) and (
                                                                                                                    c % 2 == 0 or c % 3 == 0))))) and (
                    a <= 60 and b <= 60 and c <= 60)):
                randomized_number(a, b, c)
                break
            else:
                if score > 60:
                    a = rd.randint(1, 61)
                    b = rd.randint(1, 61)
                    c = rd.randint(1, 61)
                else:
                    a = rd.randint(1, score + 1)
                    b = rd.randint(1, score + 1)
                    c = rd.randint(1, score + 1)


if __name__ == "__main__":
    player1 = str(input('Insert the name of player 1: '))

    total1 = 501
    total3 = 1000
    total4 = 1000
    counts = 0

    print(f'\nWelcome {player1} in Darts World.')
    print("Let's begin our play\n")

    while True:
        print('\nRequired Score = ', total1)
        print(f"Attempts = {counts}")

        if total1 <= 180:
            print('\nRecommended Shots: \n')
            recommend_func(total1)

        while True:
            d1 = int(input('\n1st dart score: '))
            if d1 <= 60:
                if (20 < d1 < 41) and d1 % 2 == 0:
                    total1 = total1 - d1

                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d1
                        total3 = total1
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif (20 < d1 < 61) and d1 % 3 == 0:
                    total1 = total1 - d1
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d1
                        total3 = total1
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif d1 <= 20:
                    total1 = total1 - d1
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d1
                        total3 = total1
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif d1 == 50 or d1 == 25:
                    total1 = total1 - d1
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d1
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

        if ((total1 <= 120) and (total1 >= 1)) and ((total3 - d1) > 0):
            print('\nRecommended Shots: \n')
            recommend_func2(total1)

        while True:
            if (total3 - d1) < 0:
                total3 = total1
                break

            if total1 == 0:
                break

            d2 = int(input('\n2nd dart score: '))

            if d2 <= 60:
                if (20 < d2 < 41) and d2 % 2 == 0:
                    total1 = total1 - d2
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d2
                        total3 = total1
                        total1 = total1 + d1
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif (20 < d2 < 61) and d2 % 3 == 0:
                    total1 = total1 - d2
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d2
                        total3 = total1
                        total1 = total1 + d1
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif d2 < 21:
                    total1 = total1 - d2
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d2
                        total3 = total1
                        total1 = total1 + d1
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif d2 == 50 or d2 == 25:
                    total1 = total1 - d2
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + d2
                        total3 = total1
                        total1 = total1 + d1
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

        if ((total1 <= 60) and (total1 >= 1)) and (((total3 - d1) > 0) and ((total3 - d2) > 0)):
            print('\nRecommended Shots: \n')
            recommend_func3(total1)

        while True:
            if ((total3 - d1) < 0) or ((total3 - d2) < 0):
                total3 = total1
                break

            if total1 == 0:
                break

            d3 = int(input('\n3rd dart score: '))

            if d3 <= 60:
                if (20 < d3 < 41) and d3 % 2 == 0:
                    total1 = total1 - d3
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + (d1 + d2 + d3)
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif (20 < d3 < 61) and d3 % 3 == 0:
                    total1 = total1 - d3
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + (d1 + d2 + d3)
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif d3 < 21:
                    total1 = total1 - d3
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + (d1 + d2 + d3)
                        break
                    else:
                        print('Required Score: ', total1)
                        break
                elif d3 == 50 or d3 == 25:
                    total1 = total1 - d3
                    if total1 < 0:
                        print('\nYou can not score more than required!\n')
                        total1 = total1 + (d1 + d2 + d3)
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

        counts += 1
        total3 = 1000
        total4 = 1000

        if total1 == 0:
            print(f'\n{player1} scores 501 in {counts} attempts!!!')
            break
