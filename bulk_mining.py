from data_mine import data_mine_api

# get api_key
api_key = dict()
api_fname = 'api_key.txt'
with open(api_fname, 'r') as infile:
    tokens = infile.readline().split()
    api_key[tokens[0]] = tokens[1]

# mine data
begin = 1
end = 353
chamber = 'senate'
for rollcall_number in range(begin, end + 1):
    outfile_name = 'rollcall_votes/' + str(chamber) + '_116/vote_' + str(rollcall_number) + '.json'
    url = 'https://api.propublica.org/congress/v1/116/' + str(chamber) + '/sessions/1/votes/' + str(rollcall_number) + '.json'
    data_mine_api(url, api_key, outfile_name)
