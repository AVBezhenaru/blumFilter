
bf = BloomFilter(32)

print("result", bf.hash1("0123456789"))

print(bf.bitarray)
bf.add("0123456789")

# print("is value", bf.is_value("0123456789"))
print("is value", bf.is_value("0123456789"))

