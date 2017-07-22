import pandas as pd

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
    sex_dict = {'female': 0,
                'male': 0}
    file = open(_filename, 'w')
    for sex in sex_dict:
        sex = dataframe['Sex'].value_counts()[sex]
        file.write(str(sex) + ' ')
    file.close()


# Get survived in percents
def survived_in_percents(dataframe, _filename):
    passengers_number = dataframe.index[-1]
    if_survived = 1
    survived = \
        round(dataframe['Survived'].value_counts()[if_survived] * 100 / passengers_number, 2)
    print(survived)
    file = open(_filename, 'w')
    file.write(str(survived) + ' ')
    file.close()


# Get percent of first class passengers relative to the general number of passengers.
def get_first_class_percentage(dataframe, _filename):
    passengers_number = dataframe.index[-1]
    if_first_class = 1
    firstclass = \
        round(dataframe['Pclass'].value_counts()[if_first_class] * 100 / passengers_number, 2)
    print(firstclass)
    file = open(_filename, 'w')
    file.write(str(firstclass) + ' ')
    file.close()

get_first_class_percentage(data, filename[2])
#survived_in_percents(data, filename[1])