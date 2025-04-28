# Created on March 2, 2015
#
# @author: Jim Yin


import time


def numbers_to_words(n):

    if n == 1000:
        return 'one thousand'
    elif n == 20:
        return 'twenty'
    elif n == 30:
        return 'thirty'
    elif n == 40:
        return 'forty'
    elif n == 50:
        return 'fifty'
    elif n == 60:
        return 'sixty'
    elif n == 70:
        return 'seventy'
    elif n == 80:
        return 'eighty'
    elif n == 90:
        return 'ninety'
    elif n == 0:
        return ''
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n >= 100:
        hundred = int(n/100)
        hundred_word = numbers_to_words(hundred)
        two_digit = n % 100
        two_digit_word = numbers_to_words(two_digit)
        if hundred == 1 and two_digit == 0:
            return f'{hundred_word} hundred'
        elif hundred == 1 and two_digit > 0:
            return f'{hundred_word} hundred and {two_digit_word}'
        elif hundred > 1 and two_digit == 0:
            return f'{hundred_word} hundred'
        else:
            return f'{hundred_word} hundred and {two_digit_word}'
    elif n >= 20:
        ten_digit = int(n/10)
        ten_digit_word = numbers_to_words(ten_digit*10)
        one_digit = n % 10
        one_digit_word = numbers_to_words(one_digit)
        return f'{ten_digit_word}-{one_digit_word}'


def count_letters(w):

    counter = 0
    for l in w:
        if l.isalpha():
            counter += 1
    return counter


def prob_017():

    total = 0
    for i in range(1, 1001):
        total += count_letters(numbers_to_words(i))

    return total


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_017())
    end_time = time.perf_counter()
    print(f'Time taken = {round(end_time - start_time, 4)} sec')


# 21124
# Time taken = 0.0047 sec
