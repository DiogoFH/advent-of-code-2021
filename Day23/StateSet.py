class StateSet(set):
    def __init__(self):
        set.__init__(self)
    
    def add(self, elem):
        if set.__contains__(self, elem):
            oldElem = set.remove(self, elem)
            if oldElem.cost > elem.cost:
                set.add(self, elem)
            else:
                set.add(self, oldElem)
        else:
            set.add(self, elem)
        