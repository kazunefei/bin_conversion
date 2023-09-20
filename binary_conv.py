
file1 = open("bootloader.bin", mode = "rb")
bootloader = file1.read()

bootl_list = list()
bootl_list.clear()
i=0
while i < len(bootloader):
    bootl_list.append(hex(bootloader[i]))
    i+=1
file1.close()


file2 = open("firmware.bin", mode = "rb")
firmware = file2.read()

firm_list = list()
firm_list.clear()
i=0
while i < len(firmware):
    firm_list.append(hex(firmware[i]))
    i+=1
file2.close


file3 = open("partitions.bin", mode = "rb")
partitions = file3.read()

part_list = list()
part_list.clear()
i=0
while i < len(partitions):
    part_list.append(hex(partitions[i]))
    i+=1
file3.close


bootl_string = ",".join(bootl_list)
firm_string = ",".join(firm_list)
part_string = ",".join(part_list)
combined = open("dest_binaries.c", "w")
combined.write("#include <stdint.h>")
combined.write("\n")
combined.write("\n")
combined.write(f"const uint8_t  DEST_bootloader_bin[] = {{{bootl_string}}};")
combined.write("\n")
combined.write("const uint32_t DEST_bootloader_bin_size = sizeof(DEST_bootloader_bin);")
combined.write("\n")
combined.write(f"const uint8_t  DEST_firmware_bin[] = {{{firm_string}}};")
combined.write("\n")
combined.write("const uint32_t DEST_firmware_bin_size = sizeof(DEST_firmware_bin);")
combined.write("\n")
combined.write(f"const uint8_t  DEST_partitions_bin[] = {{{part_string}}};")
combined.write("\n")
combined.write("const uint32_t DEST_partitions_bin_size = sizeof(DEST_partitions_bin);")


