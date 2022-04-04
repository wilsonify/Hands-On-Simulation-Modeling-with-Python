import numpy as np

a = 2
c = 4
m = 5
x = 3

if __name__ == "__main__":

    for i in range(1, 17):
        x = np.mod((a * x + c), m)
        print(x)
