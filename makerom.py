rom = bytearray([0xea] * 65536)

rom[0] = 0xa9
rom[1] = 0x42

rom[2] = 0x8d
rom[3] = 0x00
rom[4] = 0x60

rom[0xfffc] = 0x00
rom[0xfffd] = 0x00

with open("rom.bin", "wb") as f:
  f.write(rom)