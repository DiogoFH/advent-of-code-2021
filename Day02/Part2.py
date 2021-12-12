horizontal = depth = aim = 0
with open('input.txt', 'r') as f:
    for line in f:
        command, value = line.split() 
        if command == 'forward':
            horizontal += int(value)
            depth += aim*int(value)
        elif command == 'down':
            aim += int(value)
        elif command == 'up':
            aim -= int(value)
        
print(horizontal)
print(depth)
print(horizontal * depth)