import bsdiff4

from sys import argv, stderr

def usage():
    stderr.write(f"Usage: {argv[0]} original.nes builtrom.nes patch.bsdiff4")
    exit(1)

def main():
    if len(argv) < 3:
        usage()

    print("Calculating bsdiff4 patch")
    bsdiff4.file_diff(argv[1], argv[2], argv[3])

if __name__ == "__main__":
    main()