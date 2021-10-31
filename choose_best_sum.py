"""
Find the best fit to lookup value                       (ref_val)
By calculating the sum of n number                      (size) 
From combination of list of integer provided            (ls)
"""

from random import randrange
from itertools import combinations

def choose_best_sum(ref_val, size, ls)->int:
    """
    :param:  -> int     - (ref_val)
    :param:  -> int     - (size)
    :param:  -> list    - (ls)
    :return: -> int     - the nearest at most of int ref_val
    """

    comb, res = [], 0

    for check_combination in combinations(ls, size):
        check = sum(check_combination)

        if check < ref_val and check > res:
            comb, res = check_combination, check

        elif check == ref_val:
            return check_combination, check

    return comb, res if res else None


if __name__ == "__main__":
    print("Testing for " + __file__)

    TEST = 3
    SIZE = 20
    CASE = 50

    result = lambda t,s,ls,rls,x: f"RESULT FOR `{t}` FOR SIZE `{s}` FROM LIST `{ls}` IS: \n\t => {rls} = `{x}`"

    for i in range(TEST):
        t, s = randrange(CASE), randrange(1,SIZE//4)
        ref_ls = [randrange(1, CASE//2) for i in range(randrange(3, SIZE))]
        print(result(t, s, ref_ls, *choose_best_sum(t, s, ref_ls)), '\n')
