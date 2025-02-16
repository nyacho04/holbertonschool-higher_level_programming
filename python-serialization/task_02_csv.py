#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """ function """
    try:

        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception as e:
        return False
