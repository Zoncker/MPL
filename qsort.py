import random
import time


def q_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return q_sort(l_nums) + e_nums + q_sort(b_nums)


def qsort(l):
    if l:
        return qsort([x for x in l if x < l[0]]) + [x for x in l if x == l[0]] + qsort([x for x in l if x > l[0]])
    return []


def main():
    num = list(map(int, input("enter the set of numbers to sort:").split()))
    tic = time.clock()
    res1 = q_sort(num)
    toc = time.clock()
    ti1 = toc - tic
    tic1 = time.clock()
    res2 = qsort(num)
    toc1 = time.clock()
    ti2 = toc1 - tic1
    print('random-wise approach {0} and time res: {1}'.format(res1, ti1))
    print('list comprehension approach {0} and time res: {1}'.format(res2, ti2))


main()
