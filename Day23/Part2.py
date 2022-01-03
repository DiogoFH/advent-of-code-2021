from Day23.state import State
import time

#__ficheiro = 'sampleInputPart2.txt'
#__ficheiro = 'sampleInput2Part2.txt'
__ficheiro = 'inputPart2.txt'

def initiallize():
    state = State()
    with open(__ficheiro, 'r') as file:
        file.readline()
        hall = [c for c in file.readline().strip() if c != '#']
        amphipods = {'A':0, 'B':0, 'C':0, 'D':0}
        for i, c in enumerate(hall):
            if c != '#' and c != '.':
                state.amphipodLocations.append((c+str(amphipods[c]), 'H' + str(i)))
                amphipods[c]+=1
        room0 = file.readline().strip().split('#')
        room0 = [i for i in room0 if i]
        for i,c in enumerate(room0):
            if c != '.' and c!= '':
                if i == 0:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'A0'))
                    amphipods[c]+=1
                elif i == 1:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'B0'))
                    amphipods[c]+=1
                elif i == 2:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'C0'))
                    amphipods[c]+=1
                elif i == 3:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'D0'))
                    amphipods[c]+=1
        room1 = file.readline().strip().split('#')
        room1 = [i for i in room1 if i]
        for i,c in enumerate(room1):
            if c != '.':
                if i == 0:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'A1'))
                    amphipods[c]+=1
                elif i == 1:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'B1'))
                    amphipods[c]+=1
                elif i == 2:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'C1'))
                    amphipods[c]+=1
                elif i == 3:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'D1'))
                    amphipods[c]+=1
        room2 = file.readline().strip().split('#')
        room2 = [i for i in room2 if i]
        for i,c in enumerate(room2):
            if c != '.':
                if i == 0:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'A2'))
                    amphipods[c]+=1
                elif i == 1:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'B2'))
                    amphipods[c]+=1
                elif i == 2:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'C2'))
                    amphipods[c]+=1
                elif i == 3:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'D2'))
                    amphipods[c]+=1
        room3 = file.readline().strip().split('#')
        room3 = [i for i in room3 if i]
        for i,c in enumerate(room3):
            if c != '.':
                if i == 0:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'A3'))
                    amphipods[c]+=1
                elif i == 1:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'B3'))
                    amphipods[c]+=1
                elif i == 2:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'C3'))
                    amphipods[c]+=1
                elif i == 3:
                    state.amphipodLocations.append((c+str(amphipods[c]), 'D3'))
                    amphipods[c]+=1
                
    return state
    
def solver():
    start = time.time()

    state = initiallize()
    
    # print(state)
    # print(state.generateSucessorStates())
    
    stateList = [state]
    
    checkedStates = set()
    
    minCost = None
    while len(stateList) > 0:
    # for i in range(5):
        # print(stateList)
        stateList = sorted(stateList)
        currentState = stateList.pop(0)
        if currentState not in checkedStates:
            # print(len(stateList), len(checkedStates), currentState.cost)
            # stateSet.remove(currentState)
            # print(currentState)
            if currentState.isEndState():
                minCost = currentState.cost
                break
            else:
                stateList.extend(currentState.generateSucessorStates())
                checkedStates.add(currentState)
    
        # for state in stateSet:
        #     print(state)
    # print(stateSet)
    print(minCost)
    end = time.time()
    print(end - start)
    



if __name__ == "__main__":
    solver()
    
    # state = initiallize()
    # amphipod = 'D0'
    # location = 'D0'
    #
    # otherAmphipod = [(a,l) for a,l in state.amphipodLocations if l[0] == location[0] and int(l[1]) > int(location[1]) and a[0] != l[0]]
    # print(otherAmphipod)
    #

    

