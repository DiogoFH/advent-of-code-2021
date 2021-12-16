#__ficheiro = 'sampleInput.txt'
#__ficheiro = 'sampleInput2.txt'
#__ficheiro = 'sampleInput3.txt'
#__ficheiro = 'sampleInput4.txt'
#__ficheiro = 'sampleInput5.txt'
#__ficheiro = 'sampleInput6.txt'
#__ficheiro = 'sampleInput7.txt'
__ficheiro = 'input.txt'

from Day16.packet import Packet

def solver():
    with open(__ficheiro, 'r') as file:
        transmission = file.read().strip()
        print(transmission) 
        
        binaryTransmission = bin(int(transmission, 16))[2:].zfill(len(transmission)*4)
        print(binaryTransmission)
        
        packet, remainder = decodePacket(binaryTransmission)
        
        print(packet)
        print(remainder)
        print(sumVersions(packet))
      
            
def decodePacket(binaryTransmission):
    version = int(binaryTransmission[:3],2)
    packetType = int(binaryTransmission[3:6],2)
    packet = Packet(version, packetType)
    
    if packetType == 4:
        packet.value, remainder = decodeLiteralPacket(binaryTransmission[6:])
    else:
        packet.subPackets, remainder = decodeOperatorPacket(binaryTransmission[6:])
    
    
    return packet, remainder

def decodeLiteralPacket(binaryTransmission):
    current = binaryTransmission[:5]
    remainder = binaryTransmission[5:]
    result = ''
    
    while current[0] == '1':
        result += current[1:]
        current = remainder[:5]
        remainder = remainder[5:]
        
    result += current[1:]
    
    return int(result, 2), remainder
    
def decodeOperatorPacket(binaryTransmission):
    lengthTypeId = binaryTransmission[0]
    remainder = binaryTransmission[1:]
    subPackets = []
    
    if lengthTypeId == '0':
        bitLength = int(remainder[:15], 2)
        remainder = remainder[15:]
        toDecode = remainder[:bitLength]
        remainder = remainder[bitLength:]
        while toDecode != '':
            packet, toDecode = decodePacket(toDecode)
            subPackets.append(packet)
    else:
        packetLength = int(remainder[:11], 2)
        remainder = remainder[11:]
        for i in range(packetLength):
            packet, remainder = decodePacket(remainder)
            subPackets.append(packet)
            
    return subPackets, remainder

def sumVersions(packet):
    sum = packet.version
    for subpacket in packet.subPackets:
        sum += sumVersions(subpacket)
    return sum 

if __name__ == "__main__":
    solver()