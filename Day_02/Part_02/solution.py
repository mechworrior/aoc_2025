# Current folder
from pathlib import Path as path

day_folder = path(__file__).parent.parent

with open(day_folder / "input.txt") as file:
    line = file.readline()


def is_bad_number(product_id):
    product_id_str = str(product_id)
    len_product_id = len(product_id_str)

    len_ranges = range(1, len_product_id // 2+1)
    
    for length in len_ranges:
        if product_id_str[:length]*(len_product_id//length) == product_id_str:
            print(product_id_str)
            return True



ranges = line.strip().split(",")
bad_numbers = set()
for range_ in ranges:
    start, end = map(int, range_.split("-"))
    for number in range(start, end + 1):
        if is_bad_number(number):
            bad_numbers.add(number)

print(sum(bad_numbers))
