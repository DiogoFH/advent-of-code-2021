#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'


def solver():
    with open(__ficheiro, 'r') as file:
        algorithm = file.readline()
        file.readline()
        image = readImage(file)
        # printImage(image)
        
        for i in range(2):
            print(i)
            if algorithm[0] == '.':
                image = applyAlgorithm(image, algorithm, '.')
            else:
                image = applyAlgorithm(image, algorithm, '.' if i % 2 == 0 else '#')
            # printImage(image)
        
        # printImage(image)
        print(countLitPixels(image))
        
def countLitPixels(image):
    count = 0
    for line in image:
        count += line.count('#')
    return count

def applyAlgorithm(image, algorithm,pad):
    newImage = []
    for y in range(len(image)+2):
        newImage.append('')
        for x in range(len(image)+2):
            index = getAlgorithmIndex(image,x-1,y-1,pad)
            newImage[y] += algorithm[index]
    return newImage

def getAlgorithmIndex(image,x,y,pad):
    index = (  getPixelAt(image,x-1,y-1,pad)
             + getPixelAt(image,x,y-1,pad)
             + getPixelAt(image,x+1,y-1,pad)
             + getPixelAt(image,x-1,y,pad)
             + getPixelAt(image,x,y,pad)
             + getPixelAt(image,x+1,y,pad)
             + getPixelAt(image,x-1,y+1,pad)
             + getPixelAt(image,x,y+1,pad)
             + getPixelAt(image,x+1,y+1,pad))
    
    index = index.replace('.', '0')
    index = index.replace('#', '1')
    return int(index, 2)

def getPixelAt(image,x,y,pad):
    if not len(image) > x >= 0 <= y < len(image[0]):
        return pad
    else:
        return image[y][x]
            

def readImage(file):
    image = []
    for line in file:
        image.append(line.strip())
    return image
            

def printImage(image):
    for line in image:
        print(line)
    print()

if __name__ == "__main__":
    solver()

