import itertools


START_NODE = 0


def load_input_file(file_name):
    with open(file_name) as file:
        yield from (line.strip() for line in file)


def parse(lines: [str]):
    walls = set()
    nodes = {}

    y = 0
    for line in lines:
        for x, v in enumerate(line):
            if v == '#':
                walls.add((x, y))
            elif v in '0123456789':
               nodes[int(v)] = (x, y)

        y += 1

    return walls, nodes


def find_paths_lengths_to_all_nodes(walls, nodes, node):

    def find_all_posibilities(walls: set, node):
        x, y = node

        for px, py in [(x + px, py + y) for px, py in [(0, 1), (0, -1), (1, 0), (-1, 0)]]:
            new_node = (px, py)
            if not new_node in walls:
                yield new_node


    posibilities = [(node, 0)]
    visited = {}

    while posibilities:
        current, steps = posibilities.pop(0)
        if current in visited:
            visited[current] = min(visited[current], steps)
            continue
        else:
            visited[current] = steps

        new_steps_count = steps + 1
        for _next in find_all_posibilities(walls, current):
            posibilities.append((_next, new_steps_count))

    return {
            node_name:visited[position]
            for position, node_name in {v:k for k, v in nodes.items()}.items()
            if position in visited
        }


def find_the_minimum_path_length(maze_map: [str], path_generator):

    def check_path(connection_matrix, path):
        prev_node = 0
        path_steps = 0

        for node in path:
            path_steps += connection_matrix[prev_node][node]
            prev_node = node

        return path_steps

    walls, nodes = parse(maze_map)
    connection_matrix = {node_name:find_paths_lengths_to_all_nodes(walls, nodes, nodes[node_name]) for node_name in nodes.keys()}
    return min([check_path(connection_matrix, path) for path in path_generator(nodes)])


def solution_for_first_part(maze_map: [str]):

    def path_generator(nodes):
        yield from itertools.permutations([node for node in nodes.keys() if node != START_NODE])

    return find_the_minimum_path_length(maze_map, path_generator)


test_input = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''.splitlines()

assert solution_for_first_part(test_input) == 14

# The input is taken from: https://adventofcode.com/2016/day/24/input
maze_map = list(load_input_file('input.24.txt'))
print("Solution for the first part:", solution_for_first_part(maze_map))


def solution_for_second_part(maze_map: [str]):

    def path_generator(nodes):
        for path in itertools.permutations([node for node in nodes.keys() if node != START_NODE]):
            yield list(path) + [0]

    return find_the_minimum_path_length(maze_map, path_generator)


print("Solution for the second part:", solution_for_second_part(maze_map))
