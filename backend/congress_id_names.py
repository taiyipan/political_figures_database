#!/usr/bin/env python3

import sqlite3


# connect to political_figures_database.db
conn = sqlite3.connect('../congress.db')
cur = conn.cursor()

# create house_member_dict from house_member table with names and bioguide_id
cur.execute('SELECT id, first_name, last_name FROM house_members')
rows_house = cur.fetchall()
house_members_dict = {bioguide_id: (first, last) for bioguide_id, first, last in rows_house}
# create lists of house members who have multiple given names
h_multi_first_names = [(bioguide_id, first, last) for bioguide_id, first, last in rows_house if len(first.split()) > 1]
h_multi_last_names = [(bioguide_id, first, last) for bioguide_id, first, last in rows_house if len(last.split()) > 1]

# create senate_member_dict from senate_member table
cur.execute('SELECT id, first_name, last_name FROM senate_members')
rows_senate = cur.fetchall()
senate_members_dict = {bioguide_id: (first, last) for bioguide_id, first, last in rows_senate}
# create lists of senate members who have multiple given names
s_multi_first_names = [(bioguide_id, first, last) for bioguide_id, first, last in rows_senate if len(first.split()) > 1]
s_multi_last_names = [(bioguide_id, first, last) for bioguide_id, first, last in rows_senate if len(last.split()) > 1]

#
print('house members with multiple first names:')
for fn in h_multi_first_names:
    print(*fn[1:])
print('\nhouse members with multiple last names:')
for ln in h_multi_last_names:
    print(*ln[1:])

print('\nsenate members with multiple first names:')
for fn in s_multi_first_names:
    print(*fn[1:])
print('\nsenate members with multiple last names:')
for ln in s_multi_last_names:
    print(*ln[1:])
