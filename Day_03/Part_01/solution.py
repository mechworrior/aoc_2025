# Current folder
from pathlib import Path as path

day_folder = path(__file__).parent.parent

with open(day_folder / "input.txt") as file:
    banks = file.readlines()

def find_greatest_voltage(bank: str) -> int:
    bank = bank.strip()
    previous_tenth = 0
    previous_digit = 0
    max_tenth = 0
    max_oneth = 0
    for idx, char in enumerate(bank[1:-1]):
        if int(char) > previous_tenth:
            max_tenth = int(char)
            break_index = idx + 2
            previous_tenth = int(char)
    for idx, char in enumerate(bank[break_index:]):
        if int(char) > previous_digit:
            max_oneth = int(char)
            previous_digit = int(char)
    return max_tenth*10 + max_oneth


total_voltage_difference = sum(find_greatest_voltage(bank) for bank in banks)
print(total_voltage_difference)