import math

if __name__ == '__main__':
    print(f"%s" % "Hour", "%20s" % "Bacterial Number")

    for counter in range(4):
        print(f"%4d" % (5 * counter), "%16d" % (200 * int(math.pow(2, 5 * counter))))

