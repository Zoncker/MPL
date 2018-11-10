import random
import redis
import os
import re


def main():

    phrase = input("Enter a phrase to search for:")
    keys = phrase.split()
    print(keys)
    text_keys_relevancy(keys)

    # res = spiral_matr(5, 4)
    # print(res)
    # nums = [4, 1, 6, 3, 2, 7, 8]
    # r = q_sort(nums)
    # print(r)
    # re = qsort(nums)
    # print(re)


def spiral_matr(n, m):
    count = 0
    res = [[0 for i in range(m)] for j in range(n)]
    k = 1
    for i in range(n * m):

        for j in range(k - 1, m - k + 1):
            count += 1
            res[k - 1][j] = count
            i += 1

        for j in range(k, n - k + 1):
            count += 1
            res[j][m - k] = count
            i += 1

        for j in reversed(range(k - 1, m - k)):
            count += 1
            res[n - k][j] = count
            i += 1

        for j in reversed(range(k, n - k)):
            count += 1
            res[j][k - 1] = count
            i += 1

        k += 1

    return res


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


def text_keys_relevancy(phrase, file_dir='/home/fvoyager/test'):
    reds = redis.StrictRedis('localhost')
    for subdir, dirs, files in os.walk(file_dir):
        for file in files:
            res = {file: {}}
            if file.endswith(".txt"):
                f = open(os.path.join(file_dir, file), 'r')
                lines = f.read()
                total = 0
                res[file]["result"] = []
                for key in phrase:
                    pos = [m.start() for m in re.finditer(key, lines)]
                    total += len(pos)
                    res_k = {"key": key, "indeces": pos, "count": len(pos)}
                    res[file]["result"].append(res_k)
                res[file]["total"] = total
            print(res)
            reds.hmset("pythonDict", res)
    print(reds.hgetall("pythonDict"))


if __name__ == '__main__':
    main()

