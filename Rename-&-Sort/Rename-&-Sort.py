import os

for path, subdirs, files in os.walk('.'):
    index_map = dict([])
    for idx, file in enumerate(sorted(files)):
        f_type = file.split('.')[-1].lower()
        if f_type == "py":
            continue
        next_index = index_map.get(f_type, 0) + 1
        os.rename(os.path.join(path, file), os.path.join(path, f"{next_index:04d}.{f_type}"))
        index_map[f_type] = next_index