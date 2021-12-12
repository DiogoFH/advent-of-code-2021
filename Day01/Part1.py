count = 0
last = '0'
with open('input.txt', 'r') as f:
    for line in f:
        if line > last:
            count = count + 1
        last = line
print(count)