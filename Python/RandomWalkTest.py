import numpy as np
import matplotlib.pyplot as plt

steps = 1000
origin = 0

step_set = np.array([-1, 1])
random_step = np.random.choice(step_set, size=steps)

path = np.concatenate([[origin], np.cumsum(random_step)])

plt.figure(figsize=(10, 4))
plt.plot(path, color='red', linewidth=1)
plt.title("1D Random Walk")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.grid(True, alpha=0.3)
plt.show()