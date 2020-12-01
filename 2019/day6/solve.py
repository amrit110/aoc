import math


def read_input(input_file):
    with open(input_file, 'r') as f:
        return f.read().splitlines()


class Node:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return '{} - {}'.format(self.parent, self.name)


def traverse_to_root(node):
    num_orbits = 0
    path = []
    parent = node.parent
    if parent is not None:
        no, p = traverse_to_root(parent)
        path = p + [parent.name]
        num_orbits = no + 1

    return num_orbits, path


def populate_orbit_map(map_data):
    orbit_map = dict()

    for orbit in map_data:
        p, c = orbit.split(')')
        if orbit_map.get(p) is None:
            orbit_map[p] = Node(p)
        if orbit_map.get(c) is None:
            orbit_map[c] = Node(c, parent=orbit_map[p])
        else:
            orbit_map[c].parent = orbit_map[p]

    return orbit_map


def solve_part1():
    map_data = read_input('input.txt')

    orbit_map = populate_orbit_map(map_data)

    total_orbits = 0
    for node_name, node in orbit_map.items():
        num_orbits, _ = traverse_to_root(node)
        total_orbits += num_orbits

    return total_orbits


def solve_part2():
    map_data = read_input('input.txt')

    orbit_map = populate_orbit_map(map_data)

    no_you, com_to_you = traverse_to_root(orbit_map['YOU'])
    no_san, com_to_san = traverse_to_root(orbit_map['SAN'])
    you_to_com = com_to_you[::-1]
    is_in_com_to_san = set(com_to_san)

    num_transfers = 0
    for n in you_to_com:
        if n in is_in_com_to_san:
            intersect_node = n
            break
        num_transfers += 1

    intersect_idx = com_to_san.index(intersect_node)
    intersect_to_san = com_to_san[intersect_idx:]
    num_transfers = num_transfers + len(intersect_to_san) - 1

    return num_transfers


if __name__ == '__main__':
    print(solve_part1())
    print(solve_part2())
