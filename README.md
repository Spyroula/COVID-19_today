# COVID-19_today
### Table of Contents

1. [Requirments](#Requirments)
2. [Project Motivation](#motivation)
3. [Methodology](#methodology)
4. [File Descriptions](#files)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Requirments <a name="Requirments"></a>

Anaconda distribution of Python is sufficient to run the main python notebook of the project (covid_19_project.ipynb), although the plotly library (plotly==4.14.3) 
might need to be installed. The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

For this project, I aim to provide a COVID-19 epidemiological situation globally according to john Hopkins University data to better understand the state of the virus worldwide since day one. 

## Methodology<a name="methodology"></a>
This project follows the CRISP-DM process. 

### Business Understanding

I aim to adress the following question regarding our provide a COVID-19 epidemiological situation globally:

1. What is the current epidemiological situation globally in terms of confirmed cases and deaths?
2. What are the COVID-19 mortality rate and the growth factor globally? 
3. Which are the top 20 countries in terms of confirmed cases, deaths, and mortality rate? 
4. What is the current epidemiological situation in the US?
5. What is the current epidemiological situation in Europe?
6. What is the current epidemiological situation in Asia?

### Data Understanding

For the purpose of this project, we use the latest data from John Hopkins University GitHub repository: https://github.com/CSSEGISandData/COVID-19. The data of the repository is updated on daily basis and the version we use in this kernel is the: 4/2/2021. 

In Data Understanding section of the covid_19_project notebook, we explored the data.
For our analysis we focus on the 5 datasets available, mainly: 

1. confirmed patients in global region
2. deaths in global region
3. recovered patients in global region
4. confirmed patients in US region
5. deaths in US region

We obtain the shape, the view and detailed informations of the datasets. 

### Data Preparation

In order to prepare the data for our main analysis, we performed several preprocess steps. 

1. We deleted the columns that are not in the datasets of both regions, US and global. 
2. We identified and treated our missing values (e.g NaNs).
3. We identified and treated our negative values.
4. We rename several columns so they are in correspondence in all the datasets from both regions. 
5. We removed corrupted data and problematic values based on the information about the data collection that we have from the GitHub repo.
6. We reshaped our data into a more computer-friendly form, change the dataframes format from wide to long and make our analysis of data easier.
7. We grouped by the date and state/country and some up the values of confirmed cases, deaths and recoverved patients. 
8. We merged the datasets of both regions into one universal dataset, ending up having a dataset with Confirmed cases, Deaths and Recoverded for every country/state per day.
9. We applied log transformation to some features.
10. We calculated extra features, namely mortality rate, growth factor and new cases per day. 

### Modeling

### Results<a name="results"></a>

The answers to the above questions and an analysis and findings of the project can be found at the post available [here](https://spyroula-masiala.medium.com/covid-19-what-does-2021-hold-33e5ae8accb5).

### Deploy

## File Descriptions <a name="files"></a>

There is one notebook available in this repo (covid_19_project.ipynb) to show the main analysis related to the above questions.  
There is an additional `utils.py` file that runs the necessary functions for the project analysis. Moreover, there are 5 csv files containing the data used in this project. 


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit must be given to John Hopkins University data.  You can find the Licensing for the data and other descriptive information at the Github repo link available [here](https://github.com/CSSEGISandData/COVID-19).
