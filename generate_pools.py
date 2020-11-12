import json


class Player:
    def __init__(self, name, GWR, OWGR):
        self.name = name
        self.GWR = GWR
        self.OWGR = OWGR


class Group:
    def __init__(self, playerA, playerB, playerC, playerD, groupOWGR, groupGWR):
        self.playerA = playerA
        self.playerB = playerB
        self.playerC = playerC
        self.playerD = playerD
        self.groupOWGR = groupOWGR
        self.groupGWR = groupGWR


def writeGroupsToFile(file_name, groups):
    with open(file_name, 'w') as f:
        for group in groups:
            group_str = 'A: ' + group.playerA.name + ' B: ' + group.playerB.name + ' C: ' + group.playerC.name + \
                ' D: ' + group.playerD.name + ' OWGR: ' + \
                str(group.groupOWGR) + ' GWR: ' + str(group.groupGWR)
            f.write("%s\n" % group_str)


def playerDecoder(raw_players):
    players = []
    for player in raw_players:
        players.append(Player(player['name'], player['GWR'], player['OWGR']))
    return players


def get_group_gwr(group):
    return group.groupGWR


def get_group_owgr(group):
    return group.groupOWGR


def get_group_total_rank(group):
    return group.groupOWGR + group.groupGWR


# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

groupA = playerDecoder(data['groupA'])
groupB = playerDecoder(data['groupB'])
groupC = playerDecoder(data['groupC'])
groupD = playerDecoder(data['groupD'])

# Closing file
f.close()

results = []
# Iterating through the json
# list
for playerA in groupA:
    for playerB in groupB:
        for playerC in groupC:
            for playerD in groupD:
                groupOWGR = playerA.OWGR + playerB.OWGR + playerC.OWGR + playerD.OWGR
                groupGWR = playerA.GWR + playerB.GWR + playerC.GWR + playerD.GWR
                results.append(Group(playerA, playerB, playerC,
                                     playerD, groupOWGR, groupGWR))

writeGroupsToFile('unranked_results.txt', results)

results.sort(key=get_group_owgr)

writeGroupsToFile('owgr_results.txt', results)

results.sort(key=get_group_owgr)

writeGroupsToFile('gwr_results.txt', results)

results.sort(key=get_group_total_rank)

writeGroupsToFile('total_rank_results.txt', results)
