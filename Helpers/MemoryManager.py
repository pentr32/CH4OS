import pymem            # pip install pymem
import pymem.process
import re
import struct

pm = pymem.Pymem("csgo.exe")


def aob_scan(dll, range, signature, instance):
    if signature == "":
        return -1

    temp_signature = re.sub("[^a-fA-F0-9]", "", signature.replace("??", "3F"))

    count = -1
    search_range = bytes.fromhex(temp_signature)

    read_memory = pm.read_int(dll, range)
    temp1 = 0
    i_end = min(len(search_range), 0x20)

    for j in range(i_end):
        if search_range[j] == 0x3F:
            temp1 |= (1 << (i_end - j - 1))

    s_bytes = [0] * 0x100

    if temp1 != 0:
        s_bytes = [temp1] * 0x100

    temp1 = 1
    index = i_end - 1

    while index >= 0:
        s_bytes[search_range[index]] |= temp1
        index -= 1
        temp1 <<= 1

    temp2 = 0

    while temp2 <= len(read_memory) - len(search_range):
        last = len(search_range)
        temp1 = len(search_range) - 1
        temp3 = -1

        while temp3 != 0:
            temp3 &= s_bytes[read_memory[temp2 + temp1]]

            if temp3 != 0:
                if temp1 == 0:
                    count += 1

                    if count == instance:
                        return dll + temp2

                    temp2 += 2

                last = temp1

            temp1 -= 1
            temp3 <<= 1

        temp2 += last

    return -1


def scan_pattern(dll, pattern, extra, offset, mode_subtract):
    temp_offset = struct.unpack("<i", pm.read_int(aob_scan(dll, 0x1800000, pattern, 0) + extra, 4))[0] + offset

    if mode_subtract:
        temp_offset -= dll

    return temp_offset


def read_matrix(process_handle, address, matrix_size):
    byte_size = struct.calcsize('f')
    buffer = bytearray(byte_size * matrix_size)
    pm.Pymem(process_handle)
    pm.read_bytes(address, buffer)
    return struct.unpack('f' * matrix_size, buffer)
