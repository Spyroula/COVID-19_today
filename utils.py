from datetime import datetime 
import pandas as pd
import numpy as np


def insight_dataframe(dataframe, dataframe_name):
    print("The {} dataframe has {} rows and {} columns.".format(dataframe_name, dataframe.shape[0], dataframe.shape[1]))
    print(80*("*"))
    print("The {} dataframe appears:".format(dataframe_name))
    return dataframe.head(5)


def fix_dates(dataframe):
    try:
        dataframe.columns = list(dataframe.columns[:4]) + [datetime.strptime(d, "%m/%d/%y").date().strftime("%Y-%m-%d") for d in dataframe.columns[4:]]
    except:
        print('An error occured!')
        raise


def missing_values_stats(dataframe, dataframe_name):
    try:
        columns_with_nan = dataframe.columns[dataframe.isnull().any()].tolist()
        if columns_with_nan == []:
            print("There is no miising value in the {} dataframe".format(dataframe_name))
        for column_name in columns_with_nan:
            number_nan = dataframe[column_name].isnull().sum()
            print("The {} column in the {} dataframe has {} missing values.".format(column_name, dataframe_name, number_nan))
    except:
        print('An error occured!')
        raise


def negative_values_stats(dataframe, dataframe_name):
    try:
        columns_with_negative = []
        for column_name in dataframe.columns:
            if dataframe[column_name].dtype == 'object':
                continue
            if (dataframe[column_name]<0).any() == True:
                columns_with_negative.append(column_name)
        if columns_with_negative == []:
            print("There is no negative value in the {} dataframe".format(dataframe_name))
        else:
            for column_name in columns_with_negative:
            
                number_negatives = np.sum((dataframe[column_name] < 0).values.ravel()) 
                print("The {} column in the {} dataframe has {} negative values.".format(column_name, dataframe_name, number_negatives))
    except:
        print('An error occured!')
        raise