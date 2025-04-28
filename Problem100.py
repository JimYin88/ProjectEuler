# Created on March 10, 2015
#
# @author: Jim Yin


import time
from fractions import Fraction


def probability(blue, red):
    return Fraction(blue * (blue - 1), (blue + red)*(blue -1 + red))


def guess_total_balls(total_balls_base):

    total_balls = total_balls_base
    while True:
        blue_balls = int(total_balls * 0.7071067811865476)
        red_balls = total_balls - blue_balls
        while probability(blue=blue_balls, red=red_balls) < Fraction(1, 2):
            blue_balls += 1
            red_balls -= 1
        if probability(blue=blue_balls, red=red_balls) == Fraction(1, 2):
            return blue_balls, blue_balls+red_balls
        else:
            total_balls += 1


def prob_100(limit=10**12):

    first_solution = guess_total_balls(4)
    second_solution = guess_total_balls(first_solution[1]+1)

    while second_solution[1] <= limit:
        first_solution, second_solution = second_solution, guess_total_balls(
            int(second_solution[1]**2/first_solution[1]))

    return second_solution[0]


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_100())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 756872327473
# Time taken = 0.002473900000040885 sec
