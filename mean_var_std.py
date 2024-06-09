import numpy as np

def calculate(inputList):
    
    if len(inputList) != 9:
        raise ValueError("List must contain nine numbers.")

    # converting list to array
    arr = np.array(inputList)

    arrReShaped = arr.reshape(3,3)

    meanList = [arrReShaped.mean(axis=0).tolist(), arrReShaped.mean(axis=1).tolist(), arrReShaped.mean().tolist()]
    varList = [arrReShaped.var(axis=0).tolist(), arrReShaped.var(axis=1).tolist(), arrReShaped.var().tolist()]
    stdList = [arrReShaped.std (axis=0).tolist(), arrReShaped.std(axis=1).tolist(), arrReShaped.std().tolist()]
    maxList = [arrReShaped.max (axis=0).tolist(), arrReShaped.max(axis=1).tolist(), arrReShaped.max().tolist()]
    minList = [arrReShaped.min (axis=0).tolist(), arrReShaped.min(axis=1).tolist(), arrReShaped.min().tolist()]
    sumList = [arrReShaped.sum (axis=0).tolist(), arrReShaped.sum(axis=1).tolist(), arrReShaped.sum().tolist()]

    outputDic = { "mean": meanList, "variance": varList, "standard deviation": stdList, "max": maxList, "min": minList, "sum": sumList }

    return outputDic