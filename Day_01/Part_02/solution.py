current_position = 50
zero_count = 0
with open("01_01/input.txt") as file:
    for line in file:
        line = line.strip()

        direction = line[0]

        steps = int(line[1:])
        prev_position = current_position

        if direction == "R":
            current_position += steps
            if current_position > 100:
                zero_count += (current_position // 100)
                if current_position % 100 == 0:
                    zero_count -= 1    
            current_position = current_position % 100

        elif direction == "L":
            current_position -= steps
            if current_position < 0:
                zero_count += ((-current_position) // 100 +1)
                if current_position % 100 == 0:
                    zero_count -= 1
                if prev_position == 0:
                    zero_count -= 1
            current_position = current_position % 100

        if current_position == 0:
            zero_count += 1

print(zero_count)


# with open("01_01/input.txt") as file:
#     rotations = [(line[0], int(line[1:])) for line in file.read().split("\n") if line]

# sign = {"R": 1, "L": -1}
# dial, count = 50, 0
# for direction, distance in rotations:
#     for d in range(distance):
#         dial = (dial + sign[direction]) % 100
#         count += dial == 0

# print(count)