def featureScaling(arr):
    import numpy as np
    if arr == None:
        return None
    else:
        arr = np.array(arr)
        maxVal = np.nanmax(arr)
        minVal = np.nanmin(arr)
        arr = (arr - minVal) / float(maxVal- minVal)
        return arr

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
