#!/usr/bin/python
# -*- coding: utf-8 -*-

# lastname,firstname,surname,organization,position,phone,email

import re
import sys
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
# pprint(contacts_list)

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
    new_contacts_list.append(new_list)
pprint(new_contacts_list)





