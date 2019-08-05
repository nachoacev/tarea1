import numpy as np
import math
import matplotlib.pyplot as plt

t = 1.258  # punto a estimar
h = np.logspace(-1,-15,15,base=10.0)

diff_simple = []
diff_mejor = []