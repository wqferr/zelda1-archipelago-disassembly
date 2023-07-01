from sys import argv, stderr

dungeon_rooms_1_through_6_addr = 0x18910
dungeon_rooms_7_through_9_addr = 0x18C10
num_dungeon_rooms_per_slice = 0x7F

new_empty_room = 0b00111111
new_has_boss_roar = 0b01000000
vanilla_empty_room = 0x03
vanilla_room_item_mask = 0b00011111
vanilla_has_removed_boss_roar = 0b00100000

def usage():
    stderr.write(f"Usage: {argv[0]} builtrom.nes")
    exit(1)

def vanilla_empty(room_byte: int):
    """Returns whether or not a room is empty by the vanilla check."""
    return (room_byte & vanilla_room_item_mask) == vanilla_empty_room

def set_really_empty(room_byte: int) -> int:
    """Return a room byte with the same flags as the input but empty in the new check."""
    return room_byte | new_empty_room

def update_room_flags(room_byte):
    if room_byte & vanilla_has_removed_boss_roar:
        room_byte |= new_has_boss_roar
        room_byte &= ~vanilla_has_removed_boss_roar
    if vanilla_empty(room_byte):
        room_byte = set_really_empty(room_byte)
    return room_byte

def main():
    if len(argv) < 2:
        usage()

    print('Applying patch: update "empty dungeon room" flag')
    with open(argv[1], "rb") as rom_file:
        rom_data = bytearray(rom_file.read())

    for room_idx in range(num_dungeon_rooms_per_slice):
        # get both rooms that share an index
        early_room = rom_data[dungeon_rooms_1_through_6_addr + room_idx]
        late_room = rom_data[dungeon_rooms_7_through_9_addr + room_idx]
        early_room = update_room_flags(early_room)
        late_room = update_room_flags(late_room)

        # put bytes back
        rom_data[dungeon_rooms_1_through_6_addr + room_idx] = early_room
        rom_data[dungeon_rooms_7_through_9_addr + room_idx] = late_room

    # write everything back
    with open(argv[1], "wb") as rom_file:
        rom_file.write(rom_data)

if __name__ == "__main__":
    main()