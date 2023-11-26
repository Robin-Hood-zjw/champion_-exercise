# Reads all data from a .Json file (use the attached file trainings.txt).
# Generate output as JSON in the three following ways.

# List each completed training with a count of how many people have completed that training.

# Given a list of trainings and a fiscal year (defined as 7/1/n-1 – 6/30/n), for each specified training, list all people that completed that training in the specified fiscal year.
# Use parameters: Trainings = "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"; Fiscal Year = 2024

# Given a date, find all people that have any completed trainings that have already expired, or will expire within one month of the specified date (A training is considered expired the day after its expiration date). For each person found, list each completed training that met the previous criteria, with an additional field to indicate expired vs expires soon.
# Use date: Oct 1st, 2023

# A note for all tasks. It is possible for a person to have completed the same training more than once. In this event, only the most recent completion should be considered.
import json
from datetime import datetime, timedelta

def read_data(path: str) -> list:
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except:
        path = input('Please type in the path of the data source.\n')

    return data

def test_1(source) -> None:
    uniq_training_dict = dict()

    for record in source:
        person_name = record['name']
    
        for training in record['completions']:
            training_name = training['name']

            if training_name not in uniq_training_dict:
                uniq_training_dict[training_name] = dict()
                uniq_training_dict[training_name]['uniq_people'] = set()

            uniq_training_dict[training_name]['uniq_people'].add(person_name)

    print("\nThe Results of the Test#1 as below:")
    for key, val in uniq_training_dict.items():
        print(f"Training Type: {key} -- Completed Count: {len(list(val['uniq_people']))}")
    print("\n")

def test_2(source, types, year) -> None:
    db_info = dict()
    date_start, date_end = datetime(year - 1, 7, 1), datetime(year, 6, 30)

    for record in source:
        person_name = record['name']

        for detail in record['completions']:
            training_name = detail['name']
            time_stamp = detail['timestamp'].split('/')


            cur_date = datetime(int(time_stamp[2]), int(time_stamp[0]), int(time_stamp[1]))
            if cur_date > date_start and cur_date < date_end and training_name in types:
                if training_name not in db_info:
                    db_info[training_name] = set()
                
                db_info[training_name].add(person_name)

    print("\nThe Results of the Test#2 as below:")
    for key, val in db_info.items():
        uniq_people = list(val)

        for people in uniq_people:
            print(f"Training Type: {key} ----- Person Name: {people}")

        print('\n')


def test_3(source, year, month, day) -> None:
    db_info = dict()
    date1 = datetime(year, month, day)
    date2 = date1 - timedelta(days=30)

    for record in source:
        person_name = record['name']

        for detail in record['completions']:
            training_name = detail['name']
            time_stamp = detail['timestamp'].split('/')

            cur_date = datetime(int(time_stamp[2]), int(time_stamp[0]), int(time_stamp[1]))
            if cur_date >= date2 and cur_date < date1:
                if person_name not in db_info:
                    db_info[person_name] = dict()
                db_info[person_name][training_name] = 'expire soon'
            elif cur_date > date1:
                if person_name not in db_info:
                    db_info[person_name] = dict()
                db_info[person_name][training_name] = 'expired'

    for person_name, training_dict in db_info.items():
        # print(f"Person Name: {person_name}")
        for training_name, status in training_dict.items():
            print(f"Person Name: {person_name}  -----  {training_name}  -----  status: {status}")
        # print("\n")

if __name__ == "__main__":
    default_file_path = './trainings.txt'
    source = read_data(default_file_path)
    test_1(source=source)

    default_types = ['Electrical Safety for Labs', 'X-Ray Safety', 'Laboratory Safety Training']
    default_fiscal_year = 2024
    test_2(source, default_types, default_fiscal_year)

    default_date = datetime(2023, 10, 1)
    test_3(source, 2023, 10, 1)