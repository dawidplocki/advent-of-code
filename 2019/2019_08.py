PICTURE_SIZE = (25, 6)


def load_input_file(file_name):
    with open(file_name) as file:
        return file.read().strip()


def split_to_layers(picture, size):
    layer_size = size[0] * size[1]
    i = 0
    while i < len(picture):
        yield picture[i:i + layer_size]
        i += layer_size


def solution_for_first_task(picture):
    layers_meta_data = [
            (layer.count('0'), layer.count('1'), layer.count('2'))
            for layer in split_to_layers(picture, PICTURE_SIZE)
        ]

    least_zeros_layer = sorted(layers_meta_data, key=lambda y: y[0])[0]
    return least_zeros_layer[1] * least_zeros_layer[2]


# The input is taken from: https://adventofcode.com/2019/day/8/input
picture = load_input_file('input.08.txt')
print("Solution for the first part:", solution_for_first_task(picture))


def solution_for_second_task(picture):

    def transform_picture(picture, size):
        layers = split_to_layers(picture, size)
        current_picture = list(next(layers))
        for layer in layers:
            current_picture = [(f if f != '2' else s) for f, s in zip(current_picture, list(layer))]

        return current_picture

    def split_picture_to_lines(picture, size):
        result = ''
        i = 0
        while i < len(picture):
            result += ''.join(picture[i:i + size[0]]) + '\n'
            i += size[0]

        return result

    def decolour(picture):
        return picture.replace('0', '#').replace('1', ' ')

    return decolour(
            split_picture_to_lines(
                transform_picture(picture, PICTURE_SIZE),
                PICTURE_SIZE))


print("Solution for the first part:")
print(solution_for_second_task(picture))
