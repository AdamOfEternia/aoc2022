class Dir:
    def __init__(self, name, parent_index=-1):
        self.name = name
        self.parent_index = parent_index
        self.files = []
        self.size = 0
        self.child_indexes = []

    def add_file(self, name, size):
        f = f"{name}---{size}"
        self.files.append(f)
        self.size += size

    def add_child(self, child_index):
        self.child_indexes.append(child_index)

    def __repr__(self):
        return f"{self.name} size={self.size} (parent={self.parent_index})"


def read_terminal_output():
    with (open("term_out.dat")) as file:
        cmds = [line.rstrip() for line in file]
    return cmds


def get_family_size(dirs, parent_dir):
    total_size = parent_dir.size
    for c_idx in parent_dir.child_indexes:
        d = dirs[c_idx]
        total_size += get_family_size(dirs=dirs, parent_dir=d)
    return total_size


def main():
    output = read_terminal_output()

    dirs = [Dir(name="root")]
    curr_dir_idx = 0
    process_list = False
    for line in output:
        if line.startswith("$"):
            process_list = False
            if line == "$ ls":
                process_list = True
            elif line == "$ cd /":
                curr_dir_idx = 0
            elif line == "$ cd ..":
                curr_dir_idx = dirs[curr_dir_idx].parent_index
            elif line.startswith("$ cd "):
                parts = line.split()
                d_name = parts[-1]
                child_indexes = dirs[curr_dir_idx].child_indexes
                for idx in child_indexes:
                    d = dirs[idx]
                    if d.name == d_name:
                        curr_dir_idx = idx
                        break
        elif process_list:
            parts = line.split()
            if parts[0] == "dir":
                d = Dir(name=parts[1], parent_index=curr_dir_idx)
                dirs.append(d)
                d_idx = dirs.index(d)
                dirs[curr_dir_idx].add_child(child_index=d_idx)
            else:
                d = dirs[curr_dir_idx]
                d.add_file(name=parts[1], size=int(parts[0]))

    total_size = 0
    for d in dirs:
        size = get_family_size(dirs=dirs, parent_dir=d)
        if size <= 100000:
            print(f"{d.name} total size... {size}")
            total_size += size
    print(total_size)

    total_disk_space = 70000000
    update_space_needed = 30000000
    total_used_space = get_family_size(dirs=dirs, parent_dir=dirs[0])
    free_space = total_disk_space - total_used_space
    print(f"Disk={total_disk_space}, "
          f"Used={total_used_space}, "
          f"Free={free_space}, "
          f"Required={update_space_needed}, "
          f"Needed={(update_space_needed - free_space)}")

    dir_to_delete = None
    size_to_delete = total_disk_space
    for d in dirs:
        size = get_family_size(dirs=dirs, parent_dir=d)
        if size >= (update_space_needed - free_space):
            if size < size_to_delete:
                size_to_delete = size
                dir_to_delete = d
    print(f"Delete {dir_to_delete} to free up {size_to_delete} space")


if __name__ == "__main__":
    main()
