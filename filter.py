""" First attempt at a python implementation of a bloom filter """

import hashlib
import os, sys


class Bloom:
    """ bloom filter implementation """
    def __init__(self, size):
        self.bits = []      # the bit array with set bits
        self.size = size    # arbitrarily chosen
        self.store = []     # stores the actual data

        for i in range(self.size):
            self.bits.append(False)
        print(self.bits)


    def md5_hash(self, value):
        md5 = hashlib.md5()
        md5.update(value.encode('utf-8'))
        result = int(md5.hexdigest(),16)
        return result % self.size

    def sha1_hash(self, value):
        sha1 = hashlib.sha1()
        sha1.update(value.encode('utf-8'))
        result = int(sha1.hexdigest(),16)
        return result % self.size

    def getHashBits(self, input):
        bit1 = self.md5_hash(input)
        bit2 = self.sha1_hash(input)
        return (bit1, bit2)

    def add(self, input):
        """ Add a value to our bloom filter"""
        (x,y) = self.getHashBits(input)
        self.bits[x] = True
        self.bits[y] = True
        self.store.append(input)

    def contains(self, value):
        """ Checks if our filter contains a certain value """
        (x,y) = self.getHashBits(value)
        bit_check = self.bits[x] & self.bits[y]
        if bit_check == False:
            print("answer from the bit array")
            return False
        else:
            # perform an actual lookup as 'yes' is only a _possible_ answer
            print("checked the store..")
            return value in self.store



if __name__ == '__main__':
    b = Bloom(10)
    print("Started the bloom filter.. what do you want to do?")
    while True:
        print("1) Add \n2) Contains")
        choice = input()
        if choice == '1':
            x = input("Input:")
            b.add(x)
        elif choice == '2':
            x = input("Input:")
            contains = b.contains(x)
            print(contains)




































