import pandas as pd
from types import GeneratorType

class NestedCV:
    def __init__(self, k):
        self.k = k

    def split(self, data, date_column):
        # Nested Cross Validation Code
        def GeneratorFunction():
            COUNT=1
            while COUNT<len(data):
                train=data[:COUNT]
                validate=data[COUNT:COUNT+1]
                COUNT+=1
                yield train,validate
        splits=GeneratorFunction()
        return splits     
if __name__ == "__main__":
    # load dataset
    data = pd.read_csv("sample1.csv")
    data["date"] = pd.to_datetime(data["date"])
    # resampling the data to make 'day' as its single time unit
    day_data=data.resample('D',on='date').sum()   

    # nested cv
    k = len(day_data)-1
    cv = NestedCV(k)
    splits = cv.split(day_data, "date")

    # check return type
    assert isinstance(splits, GeneratorType)

    # check return types, shapes, and data leaks
    count = 0
    for train, validate in splits:
        

        # types
        assert isinstance(train, pd.DataFrame)
        assert isinstance(validate, pd.DataFrame)

        # shape
        assert train.shape[1] == validate.shape[1]

        # data leak
        #assert train["date"].max() <= validate["date"].min()
        # Tere is no 'date' column. It is now the index of the data
        assert train.index.max()<=validate.index.min()
        count += 1

    # check number of splits returned
    assert count == k
