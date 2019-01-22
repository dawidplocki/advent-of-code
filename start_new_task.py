import os
from datetime import date
import webbrowser


def create_dictionary(year):
    year = str(today.year)
    if not os.path.exists(year):
        os.mkdir(year)


def create_files(year: int, day: int):
    day_with_zero = str(day).zfill(2)
    file_input_name = f'input.{day_with_zero}.txt'

    with open(os.path.join(str(year), f'{year}_{day_with_zero}.py'), 'w') as file:
        file.writelines(f'''



def load_input_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()




load_input_file('{file_input_name}')





# The solution is taken from: https://adventofcode.com/{year}/day/{day}/input
# print("Solution for the first part:", )

''')

    with open(file_input_name, 'w') as file:
        file.writelines('')


def open_tabs(year: int, day: int):
    webbrowser.open(f'https://adventofcode.com/{year}/day/{day}/input')
    webbrowser.open(f'https://adventofcode.com/{year}/day/{day}')


def find_first_missing(today):
    for year in range(2015, today.year + 1):
        year_with_zero = str(year)
        if not os.path.exists(year_with_zero):
            return year, 1

        for day in range(1, 26):
            day_with_zero = str(day).zfill(2)
            file_name = f'{year_with_zero}_{day_with_zero}.py'
            if not os.path.exists(os.path.join(year_with_zero, file_name)):
                return year, day


today = date.today()
year, day = (today.year, today.day) if today.month == 12 else find_first_missing(today)

create_dictionary(year)
create_files(year, day)
open_tabs(year, day)