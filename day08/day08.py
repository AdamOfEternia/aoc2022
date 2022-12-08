import numpy as np


def get_num_trees_visible(trees):
    return np.count_nonzero(trees)


def is_tree_visible(trees, tree_col, tree_row):
    visible = [1] * 4
    row_to_check = trees[tree_row]
    col_to_check = []
    for row in trees:
        col_to_check.append(row[tree_col])

    for x in range(0, tree_col):
        t = row_to_check[x]
        if t >= trees[tree_row][tree_col]:
            visible[0] = 0
            break

    for x in range(tree_col + 1, len(row_to_check)):
        t = row_to_check[x]
        if t >= trees[tree_row][tree_col]:
            visible[1] = 0
            break

    for y in range(0, tree_row):
        t = col_to_check[y]
        if t >= trees[tree_row][tree_col]:
            visible[2] = 0
            break

    for y in range(tree_col + 1, len(row_to_check)):
        t = col_to_check[y]
        if t >= trees[tree_row][tree_col]:
            visible[3] = 0
            break

    return 1 in visible


def read_file():
    with (open("trees.dat")) as file:
        data = [line.rstrip() for line in file]
    return data


def main():
    trees = read_file()
    print(trees)

    visibility = np.ones((len(trees[0]), len(trees)), dtype=int)
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[y]) - 1):
            visibility[x, y] = int(is_tree_visible(trees, x, y))
    print(visibility)
    num_trees_visible = get_num_trees_visible(visibility)
    print(num_trees_visible)


if __name__ == "__main__":
    main()
