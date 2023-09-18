import numpy as np

test_array = np.array([70, 50, 90, 40, 30, 40, 500, 800])
media_value = np.mean(test_array)
max_value = np.max(test_array)
min_value = np.min(test_array)

print(media_value, max_value, min_value)