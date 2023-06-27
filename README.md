Introduction
------------

This is Archipelago, a multi world randomizer. This means it randomizes multiple games at once, giving
you items in different games, or from different games. For a complete description of what it can do,
check the [relevant docs from the main Archipelago repo](https://github.com/Rosalie-A/Archipelago/blob/1f5cd8d7210b850dba5c1946a40eb543c39bf3b5/worlds/tloz/docs/en_The%20Legend%20of%20Zelda.md)


This project is just supporting the main randomizer. We apply small tweaks to the rom, so that Archipelago
is able to work with the final rom more easily.

Development
-----------

We have done the following changes to make the ROM work better with Archipelago:
* Change how empty rooms are encoded, so there is a single way of doing it.

In the future, we want to implement the following features:


Building a ROM
--------------

The source files can be assembled with ca65. To build a ROM, first make an ext folder next to
src and put ca65 and ld65 inside. Then run build.ps1. The output will appear in a bin folder.

The build script expects to find Original.nes in the ext folder to compare the output to.
Original.nes must be the "(U) (PRG0) [!]" version of the ROM.

To skip the verification, pass the option --NoVerify to build.ps1.

Historical context
-------

This project started as a project from Aldo Núñez, who managed to remake The Legend of Zelda in a
higher level language, and decided to make a more shareable version. Aldo wrote their own tool to
generate the assembly file with multiple interesting features.

Almost 2 years later, Rosalie-A and t3hf1gm3ngt came around and started to work on making a
randomizer with the disassembly. Everything we're doing here is built on tops of their work and we'd
like to thank them for it!


Contact
-------

@billionai
@wqferr
@ToransuShoujo

Special thanks to:
--------

Also Núñez - For the original disassembly of the code!
Rosalie-A - For the changes and the first edition of the randomizer
t3hf1gm3ngt - For the work on the application side of the randomizer
