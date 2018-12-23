import redis
import os
import re


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
            print("file", res)
            reds.hmset("pythonDict", res)
    print("saved into hashmaps in Redis", reds.hgetall("pythonDict"))


def main():

    phrase = input("Enter a phrase to search for:")
    direc = input("and directory to search (optional):")
    keys = phrase.split()
    print(keys)
    if not direc:
        text_keys_relevancy(keys)
    else:
        text_keys_relevancy(keys, direc)


if __name__ == '__main__':
    main()

