import pandas as pd
import numpy as np

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
    write_to(_filename, value=[survived])


# Get percent of first class passengers relative to the general number of passengers.
def get_first_class_percentage(dataframe, _filename):
    passengers_number = dataframe.index[-1]
    if_first_class = 1
    firstclass = \
        round(dataframe['Pclass'].value_counts()[if_first_class] * 100 / passengers_number, 2)
    print(firstclass)
    write_to(_filename, value=[firstclass])


# Get average and median age
def get_age_params(dataframe, _filename):
    age = dataframe['Age']
    mean_age = round(age.mean(), 2)
    med_age = round(age.median(), 2)
    write_to(_filename, value=[mean_age, med_age])
    print("%.2f %.2f\n" % (mean_age, med_age))


def write_to(_filename, value):
    file = open(_filename, 'w')
    for v in value:
        file.write(str(v) + ' ')
    file.close()


get_age_params(data, filename[3])
#count_sex(data, filename[0])
#survived_in_percents(data, filename[1])
#get_first_class_percentage(data, filename[2])
