def read_file(file_name, add_empty_line_if_none_exists=False):
    with open(file_name) as file:
        data = [line.rstrip() for line in file]
    if add_empty_line_if_none_exists and data[-1] != "":
        data.append("")
    return data


def calc_md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
