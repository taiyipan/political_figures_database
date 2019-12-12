from data_mine import data_mine_api

# get api_key
api_key = dict()
api_fname = 'api_key.txt'
with open(api_fname, 'r') as infile:
    tokens = infile.readline().split()
    api_key[tokens[0]] = tokens[1]

# data mine: members
congress = 116
chambers = ['house', 'senate']
for chamber in chambers:
    outfile_name = 'data/members/' + str(chamber) + '.json'
    url = 'https://api.propublica.org/congress/v1/' + str(congress) + '/' + str(chamber) + '/members.json'
    data_mine_api(url, api_key, outfile_name)

# data mine: votes
congress = 116
session = 1
chambers = ['house', 'senate']
for chamber in chambers:
    number = 0 
    valid_result = True
    while valid_result:
        try:
            number += 1
            outfile_name = 'data/votes/' + str(chamber) + '/' + str(number) + '.json'
            url = 'https://api.propublica.org/congress/v1/' + str(congress) + '/' + str(chamber) + '/sessions/' + str(session) + '/votes/' + str(number) + '.json'
            valid_result = data_mine_api(url, api_key, outfile_name)
        except:
            print('skip:', url)
            continue
