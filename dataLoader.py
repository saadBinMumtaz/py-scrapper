import pandas as pd

def loadData(path):
    df = pd.read_csv(path)  
    df = df.dropna()  # remove missing value row
    cols = list(df.columns)
    rows = df.values.tolist()
    kinds = []
    for value in rows[0]:  # check which col text
        if isinstance(value, str):
            kinds.append("str")
        else:
            kinds.append("num")
    return cols, kinds, rows

def makeKey(v, kind):
    # lowercase 
    if kind == "str":
        return v.lower()
    return v

def toKey(text, kind):
    # text to key
    if kind == "num":
        return float(text)
    return text.lower()
    