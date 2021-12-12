horizontal = depth = 0
with open('input.txt', 'r') as f:
    for line in f:
        command, value = line.split() 
        if command == 'forward':
            horizontal += int(value)
        elif command == 'down':
            depth += int(value)
        elif command == 'up':
            depth -= int(value)
        
print(horizontal)
print(depth)
print(horizontal * depth)