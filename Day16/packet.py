class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.value = None
        self.subPackets = []
        
    def getValue(self):
        result = 0
        if self.type == 0:
            # sum
            result = 0
            for subpacket in self.subPackets:
                result += subpacket.getValue()
        elif self.type == 1:
            # product
            result = 1
            for subpacket in self.subPackets:
                result *= subpacket.getValue()
        elif self.type == 2:
            # minimum
            result = self.subPackets[0].getValue()
            for subpacket in self.subPackets[1:]:
                if result > subpacket.getValue():
                    result = subpacket.getValue()
        elif self.type == 3:
            # max
            result = self.subPackets[0].getValue()
            for subpacket in self.subPackets[1:]:
                if result < subpacket.getValue():
                    result = subpacket.getValue()
        elif self.type == 4:
            # literal
            result = self.value
        elif self.type == 5:
            # greater than
            if self.subPackets[0].getValue() > self.subPackets[1].getValue():
                result = 1
            else:
                result = 0
        elif self.type == 6:
            # less than
            if self.subPackets[0].getValue() < self.subPackets[1].getValue():
                result = 1
            else:
                result = 0
        elif self.type == 7:
            # equal to
            if self.subPackets[0].getValue() == self.subPackets[1].getValue():
                result = 1
            else:
                result = 0
        
        return result
        
    def __str__(self):
        if self.type == 4:
            return 'Packet: Version: ' + str(self.version) + ' Type: ' + str(self.type) + ' Value: ' + str(self.value)
        else:  
            return 'Packet: Version: ' + str(self.version) + ' Type: ' + str(self.type) + ' SubPackets: ' + str(self.subPackets)
        
    def __repr__(self):
        return str(self)