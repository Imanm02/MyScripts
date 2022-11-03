import os
from multiprocessing import Pool
import subprocess

def run_command(path):
    name = path.split('\\')[-1]
    command = f"cd \"{path}\" && mkdir output"
    command += f" && mogrify -path output -crop 1672x789+124+197 *.jpg"
    command += f" && convert output\\*.jpg output\\{name}.pdf"
    print(command)
    process = subprocess.Popen(command, shell=True)
    return process

if __name__ == '__main__':
    paths = []
    for path, subdirs, files in os.walk('.'):
        if len(subdirs) != 0:
            continue
        paths.append(path[2:])
    processes = [run_command(path) for path in paths]
    for p in processes:
        print(p.wait())
