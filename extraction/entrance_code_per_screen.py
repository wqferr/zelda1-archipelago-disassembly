#!python3
from sys import argv, stderr

SCREEN_ENTRANCE_DATA_START = 0x18490 # headered
NUM_SCREENS = 0x7F

table_byte_to_entrance = lambda x: x >> 2

def usage():
    stderr.write(f"Usage: {argv[0]} rom.nes\n")
    exit(1)

def main():
    if len(argv) < 2:
        usage()

    with open(argv[1], "rb") as rom_file:
        rom_file.seek(SCREEN_ENTRANCE_DATA_START)
        rom_data = rom_file.read(NUM_SCREENS)
    
    for screen_index, screen_byte in enumerate(rom_data):
        screen_entrance = table_byte_to_entrance(screen_byte)
        if screen_entrance == 0:
            screen_entrance = "(None)"
        else:
            screen_entrance = f"0x{screen_entrance:02x}"
        print(f"0x{screen_index:02x}", "->", screen_entrance)
        
if __name__ == "__main__":
    main()