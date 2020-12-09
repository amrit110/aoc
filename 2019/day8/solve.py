from collections import defaultdict


def read_input(input_file):
    with open(input_file, "r") as f:
        return f.read()


def count_digits(layer, digit):
    return len([p for p in layer if int(p[-1]) == digit])


def read_img_layers():
    pwd = read_input("input.txt")
    w, h = 25, 6
    num_pixels = w * h
    num_layers = len(pwd) // num_pixels

    layers = defaultdict(list)
    for i in range(num_layers):
        layer_pixels = pwd[i * num_pixels : (i + 1) * num_pixels]

        for pix_idx, pix in enumerate(layer_pixels):
            layers[i].append((pix_idx // w, pix_idx % w, pix))

    return layers


def find_top_visible_pixel(layers, pix_idx):
    num_layers = len(layers)

    for i in range(num_layers):
        pix = int(layers[i][pix_idx][-1])
        if pix != 2:
            return pix


def print_msg(msg, w):
    img = ""
    for idx, pix in enumerate(msg):
        if pix == 1:
            img += str("X")
        else:
            img += " "
        if ((idx + 1) % w) == 0:
            img += "\n"

    print(img)


def solve_part1():
    layers = read_img_layers()

    layerwise_zero_counts = []
    num_layers = len(layers)
    for i in range(num_layers):
        layerwise_zero_counts.append(count_digits(layers[i], 0))

    min_zero_layer_idx = layerwise_zero_counts.index(min(layerwise_zero_counts))
    min_zero_layer = layers[min_zero_layer_idx]

    return count_digits(min_zero_layer, 1) * count_digits(min_zero_layer, 2)


def solve_part2():
    layers = read_img_layers()

    w, h = 25, 6
    num_pixels = w * h

    msg = []
    for i in range(num_pixels):
        msg.append(find_top_visible_pixel(layers, i))

    print_msg(msg, w)


if __name__ == "__main__":
    print(solve_part1())
    solve_part2()
