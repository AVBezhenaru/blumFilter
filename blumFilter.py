from bitarray import bitarray

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bitarray = self.filter_len * bitarray('0')

    def hash1(self, str1):
        index = 0
        for c in str1:
            code = ord(c)
            index = (index * 17) + code

        index = index % self.filter_len
        return index

    def hash2(self, str1):
        index = 0
        for c in str1:
            code = ord(c)
            index = (index * 223) + code

        index = index % self.filter_len
        return index

    def add(self, str1):
        index = self.hash1(str1)
        self.bitarray[index] = index
        index2 = self.hash2(str1)
        self.bitarray[index2] = index2

    def is_value(self, str1):
        index = self.hash1(str1)
        index2 = self.hash2(str1)

        if self.bitarray[index] == True and self.bitarray[index2] == True:
            return True

        return False
