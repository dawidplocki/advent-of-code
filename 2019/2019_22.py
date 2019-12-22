INSTRUCTION_CUT = 0
INSTRUCTION_DEAL = 1
INSTRUCTION_NEW_STACK = 2


def load_input_file(file_name):
    with open(file_name) as file:
        yield from (line.strip() for line in file)


def parse(task_input: [str]):
    deal_phrase = 'deal with increment '
    cut_phrase = 'cut '

    for line in task_input:
        if 'into new stack' in line:
            yield INSTRUCTION_NEW_STACK, 0
        elif deal_phrase in line:
            yield INSTRUCTION_DEAL, int(line[len(deal_phrase):])
        elif cut_phrase in line:
            yield INSTRUCTION_CUT, int(line[len(cut_phrase):])


def shuffle_cards(deck, instructions):
    deck_length = len(deck)

    for instruction, paramater in instructions:
        if instruction == INSTRUCTION_NEW_STACK:
            deck.reverse()
        elif instruction == INSTRUCTION_CUT:
            deck = deck[paramater:] + deck[:paramater]
        elif instruction == INSTRUCTION_DEAL:
            new_deck = [0] * deck_length
            for i, card in enumerate(deck):
                new_deck[(i * paramater) % deck_length] = card
           
            deck = new_deck

    return deck


def test(instructions_list, result):
    instructions = list(parse(instructions_list.splitlines()))
    excepted = list(map(int, result.split(' ')))
    recieved = shuffle_cards(list(range(10)), instructions)

    assert recieved == excepted


def solution_for_first_part(task_input):
    deck = list(range(10007))
    return shuffle_cards(deck, parse(task_input)).index(2019)


test('''deal with increment 7
deal into new stack
deal into new stack''', '0 3 6 9 2 5 8 1 4 7')

test('''cut 6
deal with increment 7
deal into new stack''', '3 0 7 4 1 8 5 2 9 6')

test('''deal with increment 7
deal with increment 9
cut -2''', '6 3 0 7 4 1 8 5 2 9')

test('''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1''', '9 2 5 8 1 4 7 0 3 6')

# The input is taken from: https://adventofcode.com/2019/day/22/input
task_input = list(load_input_file('input.22.txt'))
print("Solution for the first part:", solution_for_first_part(task_input))
