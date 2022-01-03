from Day23.burrow import Burrow

class State:
    def __init__(self, cost=0, amphipodLocations=[]):
        self.cost = cost
        self.amphipodLocations = amphipodLocations
        
    def __str__(self):
        strSelf = ''
        for amphipod, location in self.amphipodLocations:
            strSelf += (amphipod + ':' + location + ' ')
        strSelf += str(self.cost)
        return strSelf 
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        selfAmphipodLocations = [(a[0],l) for a,l in self.amphipodLocations]
        otherAmphipodLocations = [(a[0],l) for a,l in other.amphipodLocations]
        
        for amphipod, location in selfAmphipodLocations:
            if (amphipod, location) not in otherAmphipodLocations:
                return False
        return True
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __key(self):
        return tuple(sorted([(a[0],l) for a,l in self.amphipodLocations]))

    def __hash__(self):
        return hash(self.__key())
    
    def isEndState(self):
        for amphipod, location in self.amphipodLocations:
            if not amphipod[0] == location[0]:
                return False
        return True
    
    def generateSucessorStates(self):
        sucessorStates = []
        
        for amphipod, location in self.amphipodLocations:
            destinations = []
            if amphipod[0] == location[0]:
                # amphipod already in correct room. Check if he is blocking an amphipod in the wrong room
                otherAmphipod = [(a,l) for a,l in self.amphipodLocations if l[0] == location[0] and int(l[1]) > int(location[1]) and a[0] != l[0]]
                if len(otherAmphipod) != 0:
                    destinations = ['H0', 'H1', 'H3', 'H5', 'H7', 'H9', 'H10']
            elif location[0] == 'H':
                # amphipod in the hall. check if his room only has amphipods of his type
                amphipodsInWrongRoom = [(a,l) for a,l in self.amphipodLocations if l[0] == amphipod[0] and a[0] != l[0]]
                if len(amphipodsInWrongRoom) == 0:
                    amphipodsAlreadyInRoom = [(a,l) for a,l in self.amphipodLocations if l[0] == amphipod[0] and a[0] == l[0]]
                    destinations = [amphipod[0]+str(3-len(amphipodsAlreadyInRoom))]
            else:
                # amphipod in the wrong room
                destinations = ['H0', 'H1', 'H3', 'H5', 'H7', 'H9', 'H10']
            
            for destination in destinations:
                if self.pathIsClear(location, destination):
                    sucessorStates.append(self.createNewState(amphipod, destination))
        return sucessorStates
                
    def pathIsClear(self, origin, destination):
        occupiedLocations = [loc for amp, loc in self.amphipodLocations]
        for location in Burrow.paths[origin][destination][0]:
            if location in occupiedLocations:
                return False
        return True
    
    def createNewState(self, movedAmphipod, destination):
        newState = State(0, [])
        for amphipod, location in self.amphipodLocations:
            if movedAmphipod == amphipod:
                newState.amphipodLocations.append((amphipod, destination))
                newState.cost = self.cost + Burrow.paths[location][destination][1] * self.amphipodCostMultiplier(movedAmphipod)
            else:
                newState.amphipodLocations.append((amphipod, location))
        return newState

    def amphipodCostMultiplier(self, amphipod):
        if amphipod[0] == 'A':
            return 1
        elif amphipod[0] == 'B':
            return 10
        elif amphipod[0] == 'C':
            return 100
        elif amphipod[0] == 'D':
            return 1000
            