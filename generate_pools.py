import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

groupA = data['groupA']
groupB = data['groupB']
groupC = data['groupC']
groupD = data['groupD']

# Closing file
f.close()

results = []
# Iterating through the json
# list
for playerA in groupA:
    for playerB in groupB:
        for playerC in groupC:
            for playerD in groupD:
                results.append('A: ' + playerA['name'] + ' B: ' + playerB['name'] +
                               ' C: ' + playerC['name'] + ' D: ' + playerD['name'])

with open('results.txt', 'w') as f:
    for group in results:
        f.write("%s\n" % group)
