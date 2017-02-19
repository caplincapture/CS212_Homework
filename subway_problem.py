# -----------------
# takes lines as input  and returns
# a dictionary of the form {station:{neighbor:line, ...}, ... } 
#
# For example, when calling subway(boston), one of the entries in the 
# resulting dictionary should be 'foresthills': {'backbay': 'orange'}. 
# This means that foresthills only has one neighbor ('backbay') and 
# that neighbor is on the orange line. Other stations have more neighbors:
# 'state', for example, has 4 neighbors.
#
# ride(here, there, system) takes as input 
# a starting station (here), a destination station (there), and a subway
# system and returns the shortest path.
#
# longest_ride(system) returns the longest possible ride in a given 
# subway system. 
import collections

def subway(**lines):
    '''Define a subway map. Input is subway(linename='station1 station2...'...).
    Convert that and return a dict of the form: {station:{neighbor:line,...},...}
    #represent state, action pairs, state is neighboring station, 
    action is next action 
    dictionary initialization to fill with loop
    # defaultdict returns a dictionary by default if it's empty, ask for a station, 
    if nothing there, fill with dict
    # items called on argument from subway '''
    successors = collections.defaultdict(dict)
    for linename, stops in lines.items(): # lines.items set of lines, stops pairs
        for a, b in overlapping_pairs(stops.split()): # splits stops up into a list
            successors[a][b] = linename # e.g. blue line government to bowdoin and vice versa
            successors[b][a] = linename
    return successors 

def overlapping_pairs(items):
    return [items[i:i+2] for i in range(len(items) - 1)]

boston = subway(
    blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
    green='lechmere science north haymarket government park copley kenmore newton riverside',
    red='alewife davis porter harvard central mit charles park downtown south umass mattapan')

def ride(here, there, system=boston):
    "Return a path on the subway system from here to there."
    # s is state, station
    # system[s] is dictionary will look into system and give a list of successors
    # shortest path search is graph search w/o cost
    return shortest_path_search(here, lambda s: system[s], lambda s: s == there)


def longest_ride(system):
    """"Return the longest possible 'shortest path' 
    ride between any two stops in the system."""
    # have to find all the stops, complicated because they are hidden
    # in the dictionary for the system, iterate through with generator exp
    # iterate through all possible stops and b all possible stops
    # generate all of the paths between them, look for max distance using key
    stops = set(s for dic in boston.values() for s in dic)
    return max([ride(a, b) for a in stops for b in stops], key=len) 

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]
    
def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def test_ride():
    assert ride('mit', 'government') == [
        'mit', 'red', 'charles', 'red', 'park', 'green', 'government']
    assert ride('mattapan', 'foresthills') == [
        'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
        'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills']
    assert ride('newton', 'alewife') == [
        'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
        'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife']
    assert (path_states(longest_ride(boston)) == [
        'wonderland', 'revere', 'suffolk', 'airport', 'maverick', 'aquarium', 'state', 'downtown', 'park',
        'charles', 'mit', 'central', 'harvard', 'porter', 'davis', 'alewife'] or 
        path_states(longest_ride(boston)) == [
                'alewife', 'davis', 'porter', 'harvard', 'central', 'mit', 'charles', 
                'park', 'downtown', 'state', 'aquarium', 'maverick', 'airport', 'suffolk', 'revere', 'wonderland'])
    assert len(path_states(longest_ride(boston))) == 16
    return 'test_ride passes'

print test_ride()
