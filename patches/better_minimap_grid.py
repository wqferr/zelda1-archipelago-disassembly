from os.path import dirname, join as pathjoin
from sys import argv, stderr
from bsdiff4 import file_patch_inplace

def usage():
    stderr.write(f"Usage: {argv[0]} builtrom.nes")
    exit(1)
    
def main():
    if len(argv) < 2:
        usage()
    print("Applying patch: better minimap grid")
    file_patch_inplace(argv[1], pathjoin(dirname(__file__), "minimap_patch.bsdiff4"))

if __name__ == "__main__":
    main()