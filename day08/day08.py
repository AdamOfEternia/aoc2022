import numpy as np


def get_num_trees_visible(trees):
    return np.count_nonzero(trees)


def is_tree_visible(trees, tree_col, tree_row):
    visible = [1] * 4

    tree_height_to_check = trees[tree_row][tree_col]

    # left
    for t in trees[tree_row][:tree_col]:
        if t >= tree_height_to_check:
            visible[0] = 0
            break

    # right
    for t in trees[tree_row][tree_col+1:]:
        if t >= tree_height_to_check:
            visible[1] = 0
            break

    # up
    for t in trees[:, tree_col][:tree_row]:
        if t >= tree_height_to_check:
            visible[2] = 0
            break

    # down
    for t in trees[:, tree_col][tree_row+1:]:
        if t >= tree_height_to_check:
            visible[3] = 0
            break

    return 1 in visible


def read_file():
    with (open("trees.dat")) as file:
        data = [line.rstrip() for line in file]
    return data


def main():
    data = read_file()

    # get cols and rows
    cols = len(data[0])
    rows = len(data)

    # convert data into tree array
    trees = np.zeros((rows, cols), dtype=int)
    for x in range(0, cols):
        for y in range(0, rows):
            trees[y][x] = data[y][x]

    # create array of 0 and 1 representing blocked or visible
    # initialise all to 1 (visible)
    # check all trees within edge border only (border trees always visible)
    visibility = np.ones((rows, cols), dtype=int)
    for x in range(1, cols - 1):
        for y in range(1, rows - 1):
            visibility[y][x] = int(is_tree_visible(trees, x, y))

    num_trees_visible = get_num_trees_visible(visibility)
    print(num_trees_visible)


if __name__ == "__main__":
    main()
