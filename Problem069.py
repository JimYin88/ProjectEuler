# Created on Jun 21, 2022
#
# @author: Jim Yin

import time
from tqdm import tqdm
import numpy as np
import pandas as pd


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a


def prob_069():
    upperlimit = 1000000
    numbers = pd.Series(np.arange(1,upperlimit+1))

    df_totient = pd.DataFrame([1 for i in range(1, upperlimit+1)], columns = ['Totient'])
    df_totient['Number'] = numbers
    df_totient = df_totient[df_totient['Number'] % 2310 == 0]

    df_totient = df_totient.reset_index()
    df_totient.drop(['index'], axis=1, inplace=True)

    for q in tqdm(range(2, df_totient['Number'].max())):
        adder = pd.Series([1 if q < i  and gcd(i, q) == 1 else 0 for i in df_totient['Number']])
        df_totient['Totient'] += adder
  
    df_totient['ratio'] = df_totient['Number']/df_totient['Totient']

    print(int(df_totient.iloc[df_totient['ratio'].idxmax()]['Number']))
    
    
if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_069()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    
    
# 510510
# Time taken = 687.9228618 sec
    