import pandas as pd
import numpy as np
import re

filename = ['sex.txt',
            'survived.txt',
            'firstclass.txt',
            'age.txt',
            'correlation.txt',
            'femname.txt']

# get data from csv file
data = pd.read_csv('titanic.csv', index_col='PassengerId')


# Get number of male and female passengers
def count_sex(dataframe, _filename):
    sex_naming = ['male', 'female']
    sex_list = []
    for name in sex_naming:
        sex_list.append(dataframe['Sex'].value_counts()[name])
    write_to(_filename, sex_list)


# Get survived in percents
def survived_in_percents(dataframe, _filename):
    passengers_number = dataframe.index[-1]
    if_survived = 1
    survived = \
        round(dataframe['Survived'].value_counts()[if_survived] * 100 / passengers_number, 2)
    print(survived)
    write_to(_filename, [survived])


# Get percent of first class passengers relative to the general number of passengers.
def get_first_class_percentage(dataframe, _filename):
    passengers_number = dataframe.index[-1]
    if_first_class = 1
    firstclass = \
        round(dataframe['Pclass'].value_counts()[if_first_class] * 100 / passengers_number, 2)
    print(firstclass)
    write_to(_filename, [firstclass])


# Get average and median age
def get_age_params(dataframe, _filename):
    age = dataframe['Age']
    mean_age = round(age.mean(), 2)
    med_age = round(age.median(), 2)
    write_to(_filename, [mean_age, med_age])
    print("%.2f %.2f\n" % (mean_age, med_age))


# Helper function
def write_to(_filename, value):
    file = open(_filename, 'w')
    for v in value:
        file.write(str(v) + ' ')
    file.close()


def siblings_correlation(dataframe, _filename):
    result = dataframe[['SibSp', 'Parch']]
    write_to(_filename, [round(result.corr('pearson')['SibSp']['Parch'], 2)])


def get_first_name(name):
    # if we have usual name, just search for the word after '. ' pattern
    _name = name
    name = re.search("\. ([A-Za-z]*)", name)
    # if name contains parenthesis, get the first word in it
    if name.group(1) == '':
        name_in_parenthesis = re.search(".*\((.*)\).*", _name)
        return name_in_parenthesis.group(1).split(" ")[0]
    return name.group(1)


def most_popular_female_name(dataframe, _filename):
    female_names = dataframe[dataframe['Sex'] == 'female']['Name']
    female_first_names = pd.Series()
    for name in female_names:
        name = get_first_name(name)
        female_first_names = female_first_names.append(pd.Series([name], [len(female_first_names)]))
    most_common_name = female_first_names.value_counts().idxmax()
    print(most_common_name)
    write_to(_filename, [most_common_name])


count_sex(data, filename[0])
survived_in_percents(data, filename[1])
get_first_class_percentage(data, filename[2])
get_age_params(data, filename[3])
siblings_correlation(data, filename[4])
most_popular_female_name(data, filename[5])