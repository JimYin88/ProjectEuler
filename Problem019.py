# Created on March 22, 2025
#
# @author: Jim Yin


import time
import pandas as pd


def prob_019():
    # Create a datetime series with every day from 1 Jan 1901 to 31 Dec 2000
    dates = pd.date_range(start='1901-01-01', end='2000-12-31', freq='D')

    # Print the series
    df = pd.DataFrame(data=dates, columns=['date'])

    df['day'] = df['date'].dt.day
    df['weekday'] = df['date'].dt.weekday

    return len(df[(df['day'] == 1) & (df['weekday'] == 6)])


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_019())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 171
# Time taken = 0.013422499992884696 sec
