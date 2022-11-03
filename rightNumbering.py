import os

for path, subdirs, files in os.walk('books'):
    for name in files:
        fpath = os.path.join(path, name)
        name, ext = name.split('.')
        try: 
            name = int(name)
            npath = '\\'.join(fpath.split('\\')[:-1]) + f"\\{name:03}." + ext
            os.rename(fpath, npath) 
        except: 
            pass
