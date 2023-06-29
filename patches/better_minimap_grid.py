from sys import argv, stderr

patch_addr = 0x8ec7
patch = bytes.fromhex("0066660000666600")

def usage():
    stderr.write(f"Usage: {argv[0]} builtrom.nes")
    exit(1)
    
def main():
    if len(argv) < 2:
        usage()
    print("Applying patch: better minimap grid")
    with open(argv[1], "rb") as rom_file:
        rom_data = bytearray(rom_file.read())
        
    for patch_byte_offset, patch_byte in enumerate(patch):
        rom_data[patch_addr + patch_byte_offset] = patch_byte
        
    with open(argv[1], "wb") as rom_file:
        rom_file.write(rom_data)

if __name__ == "__main__":
    main()