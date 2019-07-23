###### Booting
    getting hardware running
    getting the OS and other software required for user interaction with hardware running
[boot sector; sector containing machine code to be loaded into RAM and then executed @computeer built in firmware. the very first sector on the HDD is teh boot sector]
[partition table; table maintinaed on disk that describes the partition on that diskb]
# Process
- 1. power on == immediately firmware runs POST 
- 2. boot sequence govererned by the BIOS ROM
    + bios parameters are stored in CMOS
    + BIOS rom may be password protected
- 3. control passes to the MBR (master boot record) of the first bootable device detected
- 4. MBR containing the bootstrap loader points to boot record of selected operating system
- 5. OS begins


# BIOS
- runs the initial power on self test
- stored permanently on a specialised ROM flash memory chip on the motherboard
- identifies the system devices
- Plug and play system introduced, once had to manually set a variety of parameters suucch as the location in memory where the buffers and startup code, but now automated. eliminated hardware conflicts

# MBR, now the GPT (GUID partition table) is used
- the master boot record is the first 512 bytes of non volatile memory, holds the boot code and the parition table.
    + partition table shows file system as partitions on teh disk
    + boot code processes partition table to id which partition is bootable, then boot sector gains control in the active partition

# POST
- power on self test run @firmware, POST tests to see if computer working as appropriate
- detect erros @mobo, RAM, other memory, processor, video card, all associated hardware is tested, @no problem.




# Manufacturers
- American megatrends (AMI)
    + 1985, initially manufactured entire mobos, then original equipment manufacturing, especially AMIBIOS, which is a BIOS
