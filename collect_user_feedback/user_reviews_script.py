#! /usr/bin/env python3
import os
import requests

path_to_dir = '/data/feedback'

def list_of_paths(path_to_dir):
    absolute_paths = []
    all_reviews_list = os.listdir(path_to_dir)

    for review in all_reviews_list:
        absolute_path = os.path.abspath(os.path.join(path_to_dir, review))
        absolute_paths.append(absolute_path)

    return absolute_paths

list = list_of_paths(path_to_dir)
#print(list)


def return_dictionaries(list):
    reviews_dictionary = {"title":"", "name":"", "date":"", "feedback":""}

    for review in list:
        with open (review, "r") as file:
            reviews_dictionary["title"]=file.readline()
            reviews_dictionary["name"]=file.readline()
            reviews_dictionary["date"]=file.readline()
            reviews_dictionary["feedback"]=file.readline()
        requests.post("http://34.82.222.128/feedback/", json=reviews_dictionary)

return_dictionaries(list)

