import pandas as pd
import openpyxl as pyxl
def find_substring(string, separator_1, separator_2):
    """Function pulls out the substrings which are separated by a given separators:
    separator_1 at the beginning and separator_2 at the ending."""
    values = []
    for letter in range(len(string)):
        separator_1_pos = string.find(separator_1, letter)
        separator_2_pos = string.find(separator_2, letter)
        if separator_1_pos == -1 or separator_2_pos == -1:
            continue
        elif separator_1_pos < separator_2_pos:
            values.append(string[separator_1_pos:separator_2_pos+1])
    keys_new = []
    for elem in values:
        if elem not in keys_new:
            keys_new.append(elem)
    values = keys_new
    return values

def convert_to_list(rule_string):
    """Function converts the logic string to a list with a keys (in a { }) and a values (in a " ").
    Function removes the elements with comparison operators like: >, <, >=, <="""
    rule_string = rule_string.replace(" ", "")
    to_replace = ["==", "!=", "in", "not", "and", "or"]
    to_remove = ["<", ">", "<=", ">="]
    for i in to_replace:
        rule_string = rule_string.replace(i, "#")
    rule_string = rule_string.replace("##", "#").split("#")
    for j in rule_string:
        for k in to_remove:
            if k in j:
                rule_string.remove(j)
    for n in rule_string:
        if "(" in n and ")" not in n:
            rule_string[rule_string.index(n)] = n.replace("(", "")
        if ")" in n and "(" not in n:
            rule_string[rule_string.index(n)] = n.replace(")", "")
    return rule_string


def find_rule_keys(rule_string="sample_string"):
    """Function pulls out the substrings which are covered by curly braces in a given string"""
    keys = []
    for letter in range(len(rule_string)):
        search_start_bracket = rule_string.find("{", letter)
        search_end_bracket = rule_string.find("}", letter)
        if search_start_bracket == -1 or search_end_bracket == -1:
            continue
        elif search_start_bracket < search_end_bracket:
            keys.append(rule_string[search_start_bracket:search_end_bracket + 1])
    keys_new = []
    for elem in keys:
        if elem not in keys_new:
            keys_new.append(elem)
    keys = keys_new
    return keys


def find_rule_value(rule_string="sample_string", char= '"'):
    """Function pulls out the substrings which are covered by apostrohpes in a given string"""
    keys = []
    for letter in range(len(rule_string)):
        search_start_bracket = rule_string.find(char, letter)
        search_end_bracket = rule_string.find(char, letter + 1)
        if search_start_bracket == -1 or search_end_bracket == -1:
            continue
        elif search_start_bracket < search_end_bracket:
            keys.append(rule_string[search_start_bracket:search_end_bracket + 1])
    keys_new = []
    for elem in keys:
        if elem not in keys_new and "{" not in elem:
            keys_new.append(elem)
    keys = keys_new
    return keys


def convert_to_dictionary_old(list):
    logic_dict = {}
    for i in range(len(list)):
        if "{" in list[i]:
            if list[i] not in logic_dict:
                list[i] = list[i].replace("{", "").replace("}", "")
                logic_dict[list[i]] = [list[i + 1]]
            else:
                list[i] = list[i].replace("{", "").replace("}", "")
                logic_dict[list[i]].append(list[i + 1])
            list[i] = list[i].replace("{", "").replace("}", "")
    return logic_dict

text_list = ['{Fund}', '("FNMA","USTRESURY")', '{Exposure}', '"PrivatePlacement"', '{Exposure}', '"Bond"']

def convert_to_dictionary(rule_list):
    indexes = [i for i in range(len(rule_list)) if "{" in rule_list[i]]
    dictionary = {}
    temp = []
    for elem in rule_list:
        elem = elem.replace("{", "").replace("}", "")
        temp.append(elem)
    rule_list = temp
    for i in indexes:
        if rule_list[i] not in dictionary:
            dictionary[rule_list[i]] = [rule_list[i + 1]]
        else:
            dictionary[rule_list[i]].append(rule_list[i + 1])
    return dictionary

