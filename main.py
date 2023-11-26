import json
# 
# Reads all data from a .Json file (use the attached file trainings.txt).
# Generate output as JSON in the three following ways.

# List each completed training with a count of how many people have completed that training.

# Given a list of trainings and a fiscal year (defined as 7/1/n-1 – 6/30/n), for each specified training, list all people that completed that training in the specified fiscal year.
# Use parameters: Trainings = "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"; Fiscal Year = 2024

# Given a date, find all people that have any completed trainings that have already expired, or will expire within one month of the specified date (A training is considered expired the day after its expiration date). For each person found, list each completed training that met the previous criteria, with an additional field to indicate expired vs expires soon.
# Use date: Oct 1st, 2023

# A note for all tasks. It is possible for a person to have completed the same training more than once. In this event, only the most recent completion should be considered.
with open('./trainings.txt', 'r') as file:
    data = json.load(file)

uniq_training_dict = dict()

for record in data:
    person_name = record['name']

    for training in record['completions']:
        training_name = training['name']

        if training_name not in uniq_training_dict:
            uniq_training_dict[training_name] = dict()
            uniq_training_dict[training_name]['uniq_people'] = set()

        uniq_training_dict[training_name]['uniq_people'].add(person_name)

for key, val in uniq_training_dict.items():
    print(f"Training Type: {key} -- Completed Count: {len(list(val['uniq_people']))}\n")