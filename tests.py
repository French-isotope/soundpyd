import numpy as np
import numpy.ma as ma

a = np.array([[1,2,3,4],
              [5,6,7,8]])
sample_size = 3

mask_list = [True] * sample_size + [False] * (a.size - sample_size) # [True, True, True, False, False, False, False, False]

mask = np.array(mask_list)
np.random.shuffle(mask)

mask.reshape(a.shape)
sample = ma.masked_array(a, mask=mask)

print(sample)


