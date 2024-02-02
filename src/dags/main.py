import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(sys.path)

from retreive_data.winamax import *

if __name__ == "__main__":
    print(winamax.division(6, 3))
