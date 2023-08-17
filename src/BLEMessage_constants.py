import sys
import math

P1_LOWER = 0
P1_UPPER = 5000
# encoding capacity in bits 
P1_SIZE = 16  

P2_LOWER = 0
P2_UPPER = 500
P2_SIZE = 8

P3_LOWER = 0
P3_UPPER = 200
P3_SIZE = 8

class MessageHelper():
    @classmethod
    def p1_range(cls):
        return (P1_UPPER - P1_LOWER)

    @classmethod
    def p2_range(cls):
        return(P2_UPPER - P2_LOWER)

    @classmethod
    def p3_range(cls):
        return(P3_UPPER - P3_LOWER)

    @classmethod
    def __capacity_from_bits(cls, num_bits):
        return 2 ** num_bits

    @classmethod
    def get_step(cls, param):
        if not type(param) is str:
            print("input invalid")
            sys.exit(1)
        if param == "P1":
            step = 1
            capacity = cls.__capacity_from_bits(P1_SIZE)
            range = cls.p1_range()
            while math.ceil(range / step) > capacity:
                step = step + 1
            return step
        
        if param == "P2":
            step = 1
            capacity = cls.__capacity_from_bits(P2_SIZE)
            range = cls.p2_range()
            while math.ceil(range / step) > capacity:
                step = step + 1
            return step
        
        if param == "P3":
            step = 1
            capacity = cls.__capacity_from_bits(P3_SIZE)
            range = cls.p3_range()
            while math.ceil(range / step) > capacity:
                step = step + 1
            return step
        
        else:
            print("input invalid")
            sys.exit(1)