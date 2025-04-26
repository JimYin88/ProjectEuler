# Created on April 20, 2025
#
# @author: Jim Yin


import time
from collections import Counter


ranking_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

hands_ranking = {'Straight Flush': 10,
                 'Four-of-a-kind': 9,
                 'Full House': 8,
                 'Flush': 7,
                 'Straight': 6,
                 'Three-of-a-kind': 5,
                 'Two Pairs': 4,
                 'One Pair': 3,
                 'High Card': 2}


def check_hand(hand):
    rank = []
    suit = []
    for i in hand:
        suit.append(i[1])
        rank.append(ranking_map[i[0]])

    suit_counter = Counter(suit)
    rank_counter = dict(Counter(rank))
    sorted_rank = sorted(rank_counter.items(), key=lambda item: (item[1], item[0]), reverse=True)

    ranking = []
    order = []
    for i in sorted_rank:
        ranking.append(i[1])
        counter = 0
        while counter < i[1]:
            order.append(i[0])
            counter += 1

    if set(ranking) == {2, 3, 4, 5, 14} and max(suit_counter.values()) == 5:
        return 'Straight Flush', [5, 4, 3, 2, 1]
    elif (max(rank_counter) - min(rank_counter) == 4) and max(rank_counter.values()) == 1 \
            and max(suit_counter.values()) == 5:
        return 'Straight Flush', order
    elif ranking == [4, 1]:
        return 'Four-of-a-kind', order
    elif ranking == [3, 2]:
        return 'Full House', order
    elif max(suit_counter.values()) == 5:
        return 'Flush', order
    elif set(ranking) == {2, 3, 4, 5, 14}:
        return 'Straight', [5, 4, 3, 2, 1]
    elif (max(rank_counter) - min(rank_counter) == 4) and max(rank_counter.values()) == 1:
        return 'Straight', order
    elif ranking == [3, 1, 1]:
        return 'Three-of-a-kind', order
    elif ranking == [2, 2, 1]:
        return 'Two Pairs', order
    elif ranking == [2, 1, 1, 1]:
        return 'One Pair', order
    else:
        return 'High Card', order


def prob_054():

    result = 0

    with (open("0054_poker.txt", "r") as file):
        for line in file:
            cards = line.split(' ')
            hand1 = cards[0:5]
            hand2 = cards[5:]

            left_hand = check_hand(hand1)
            right_hand = check_hand(hand2)

            if hands_ranking[left_hand[0]] > hands_ranking[right_hand[0]]:
                result += 1
            elif hands_ranking[left_hand[0]] == hands_ranking[right_hand[0]]:
                for i in range(5):
                    if left_hand[1][i] > right_hand[1][i]:
                        result += 1
                        break
                    elif left_hand[1][i] == right_hand[1][i]:
                        continue
                    else:
                        break

    return result


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_054())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 376
# Time taken = 0.0307226000004448 sec
