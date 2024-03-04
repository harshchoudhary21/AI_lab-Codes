import numpy as np
def statistcs(data):
    dict={
        'Minimum':np.amin(data),
        'Maximum':np.amax(data),
        'Mean':np.mean(data)

    }
    return dict
array = [1,2,34,5,6,7]
data = np.array(array)
dicti = statistcs(data)
print(dicti)