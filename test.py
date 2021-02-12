from anneal import SimAnneal
import time
import matplotlib.pyplot as plt
import random

coords = []
with open("coord.txt", "r") as f:
    for line in f.readlines():
        print(line)
        line = [float(x.replace("\n", "")) for x in line.split(" ")]
        coords.append([line[1], line[2]])

if __name__ == "__main__":
    # coords = [[random.uniform(-1000, 1000), random.uniform(-1000, 1000)] for i in range(100)]

    # for i in range(0,1000):
    #     print(i)
    start_millis = int(round(time.time() * 1000))
    sa = SimAnneal(coords, stopping_iter=5000)
    sa.anneal()
    time.time()
    final_millis = int(round(time.time()) * 1000)
    t = final_millis - start_millis
    if t < 0:
        t *= -1
    fi = open("times.csv", 'a')
    fi.write(str(t))
    fi.write('\n')
    fi.close()

    # new_locations = [locations[i] for i in new_order]
    # draw(new_locations)
    print('------------------------------')
