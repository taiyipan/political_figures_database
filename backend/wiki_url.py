#!/usr/bin/env python3

import sqlite3
import wikipedia

# script creates wiki_url entry for each member of the db

# connect to db
conn = sqlite3.connect('../congress.db')
cur = conn.cursor()


def create_name_list(table):
    cur.execute(f'SELECT first_name, last_name FROM {table}')
    rows = cur.fetchall()
    return [(first, last) for first, last in rows]


def create_wiki_url_list(name_list):
    wiki_urls = list()
    for _name in name_list:
        name = _name[0]+' '+_name[1]
        results = wikipedia.search(*_name)
        p = '(politician)'
        try:
            title = f'{name}'+' '+f'{p}' if (f'{p}' in result for result in results) else name
            page = wikipedia.page(title)
            wiki_urls.append(page.url)
        except:  # Exception as CannotFindWikiURL
            print(f'cannot find url for: {name}')
            wiki_urls.append(None)
    return wiki_urls


def add_column(table, column, data_type):
    try:
        cur.execute(f'''
                ALTER TABLE {table}
                ADD {column} {data_type}
                ''')
    except Exception as CannotAddColumn:
        print(f'cannot add {column} to {table} table')


def add_values_to_column(table, column, values, reference):
    for (value, ref) in zip(values, reference):
        if value is not None:
            pass
            # add value to said column in table
        #else:
        #    pass
        print(f'{value} : {ref}')


#house_names = create_name_list('house_members')
#senate_names = create_name_list('senate_members')
#house_wiki_urls = create_wiki_url_list(house_names)
#senate_wiki_urls = create_wiki_url_list(senate_names)

#add_column('house_members', 'wiki_url', 'varchar(255)')
#add_column('senate_members', 'wiki_url', 'varchar(255)')

#add_values_to_column(table=None, column=None, values=senate_wiki_urls, reference=senate_names)
