# Current folder
from pathlib import Path as path

day_folder = path(__file__).parent.parent

with open(day_folder / "input.txt") as file:
    banks = file.readlines()


def find_greatest_voltage(bank: str, digits_needed: int, leading_digits = None) -> int:
    if len(bank) == digits_needed:
        return int("".join(leading_digits)+bank)
    
    if digits_needed == 1:
        return int("".join(leading_digits)+max(bank))

    max_digit = max(bank[:-digits_needed+1])

    max_index = bank.find(max_digit)
    leading_digits = leading_digits or []
    leading_digits.append(max_digit)


    return find_greatest_voltage(bank[max_index+1:], digits_needed-1, leading_digits)



total_voltage_difference = sum(find_greatest_voltage(bank.strip(), 12) for bank in banks)

print(total_voltage_difference)
