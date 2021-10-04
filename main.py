#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
from pprint import pprint
import csv

def open_file():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    return contacts_list

def edit_contact():
    contacts_list = open_file()
    new_contacts_list = []
    for contacts in contacts_list:
        lastname = re.split(" ", contacts[0])
        firstname = re.split(" ", contacts[1])
        surname = contacts[2]
        organization = contacts[3]
        position = contacts[4]
        phone = contacts[5]
        pattern = r"((\+7)|(8\s)|(8\())(\s?\(?495\)?)(\s|\-?)(\d{3,3})(\s|\-?)(\d{2,2})(\-?)(\d{2,2})((\s)(\(?)(\w+\.)(\s)(\d+)(\)?))?"
        pattern = re.compile(pattern)
        phone = pattern.sub(r"+7(495)\7-\9-\11 \15\17", phone)
        email = contacts[6]
        new_list = lastname + firstname
        new_list.append(surname)
        new_list = list(filter(str.strip, new_list))
        if len(new_list) < 3:
            new_list.append("")
        new_list.append(organization)
        new_list.append(position)
        new_list.append(phone)
        new_list.append(email)
        new_contacts_list.append(new_list)
    return new_contacts_list

def remove_duplicates():
    new_contacts_list = edit_contact()
    num = 0
    while num < len(new_contacts_list):
        for id, contact in enumerate(new_contacts_list[int(num + 1):]):
            if new_contacts_list[num][0] and new_contacts_list[num][1] in contact:
                for i, element in enumerate(new_contacts_list[num]):
                    if element == "":
                        new_contacts_list[num][i] = contact[i]
                new_contacts_list.remove(contact)
        num += 1
    return new_contacts_list

def edit_phonebook():
    new_contacts_list = remove_duplicates()
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
    return "Контакты успешно отредактированы"

pprint(edit_phonebook())