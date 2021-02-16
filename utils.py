from datetime import datetime 
import pandas as pd
import numpy as np


def insight_dataframe(dataframe, dataframe_name):
    """Summary of the shape of a dataframe and view of the first 5 rows of the dataframe 

    Parameters:
    dataframe (DataFrame): The dataframe we want to analyse
    dataframe_name (str) : Name of the dataframe 
    
    Returns:
    str:Returning summary of the dataframe shape
    DataFrame: Returning the firtst 5 rows of the dataframe 

   """
    print("The {} dataframe has {} rows and {} columns.".format(dataframe_name, dataframe.shape[0], dataframe.shape[1]))
    print(80*("*"))
    print("The {} dataframe appears:".format(dataframe_name))
    return dataframe.head(5)


def fix_dates(dataframe):
    """Converts the date strings of the dataframe to a datetime objects in a Y-m-d format. 

    Parameters:
    dataframe (DataFrame): The dataframe in which we want to convert the date strings datetimes objects 
    
    
    Returns:
    
    DataFrame: Returns the columns of the dataframe with coverted date strings to datetime objects in a Y-m-d format.

   """
    try:
        dataframe.columns = list(dataframe.columns[:4]) + [datetime.strptime(d, "%m/%d/%y").date().strftime("%Y-%m-%d") for d in dataframe.columns[4:]]
    except:
        print('An error occured!')
        raise


def missing_values_stats(dataframe, dataframe_name):
    """Finds the missing values of the dataframe. 

    Parameters:
    dataframe (DataFrame): The dataframe in which we want to find the missing values 
    dataframe_name (str) : Name of the dataframe 
    
    Returns:
    str:Returning summary of the missing values in the dataframe 
    
   """
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
    """Finds the negative values of the dataframe. 

    Parameters:
    dataframe (DataFrame): The dataframe in which we want to find the negative values 
    dataframe_name (str) : Name of the dataframe 
    
    Returns:
    str:Returning summary of the negative values in the dataframe 
    
   """
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
    

def organize_dataframes(dataframe, value_name, column_number):

    """Reshapes the dataframe from wide to long and make our analysis of data easier. 

    Parameters:
    dataframe (DataFrame): The dataframe in which we want to find the negative values 
    value_name (str) : value_name 
    column_number (int) : Number of the column  
    
    Returns:
    DataFrame:Returning the dataframe in a long format
    
   """
    organized_dataframe = dataframe.melt(id_vars=['Country_Region', 'Province_State', 'Lat', 'Long'], value_vars=dataframe.columns[column_number:], var_name='Date', value_name=value_name)

    return organized_dataframe

