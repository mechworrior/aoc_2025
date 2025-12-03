current_position = 50
zero_count = 0
with open("01_01/input.txt") as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])
        if direction == "R":
            current_position += steps
            current_position = current_position % 100
        elif direction == "L":
            current_position -= steps
            current_position = current_position % 100
        if current_position == 0:
            zero_count += 1

print(zero_count)
