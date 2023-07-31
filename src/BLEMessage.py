from BLEMessage_constants import MessageHelper
from BLEMessage_constants import P1_LOWER
from BLEMessage_constants import P1_UPPER
from BLEMessage_constants import P2_LOWER
from BLEMessage_constants import P2_UPPER
from BLEMessage_constants import P3_UPPER
from BLEMessage_constants import P3_LOWER

class BLEMessage:
    def __init__(self, p1:int, p2:int, p3:int, p4=False) -> None:
        if p1 > P1_UPPER or p1 < P1_LOWER:
            raise(Exception("input p1 outside of range (%i, %i)" %(P1_LOWER, P1_UPPER)))
        # Stim amplitude from 10 to 5000 in increments of 1 
        self.p1 = p1
        
        # Stim PW from 25 to 500 in increments of 2 
        if p2 > P2_UPPER or p2 < P2_LOWER:
            raise(Exception("input p2 outside of range (%i, %i)" %(P2_LOWER, P2_UPPER)))
        self.p2 = p2
        
        # Stim Freq from 20 to 200 in increments of 1
        if p3 > P3_UPPER or p3 < P3_LOWER:
            raise(Exception("input p3 outside of range (%i, %i)" %(P3_LOWER, P3_UPPER)))
        self.p3 = p3
        # Stim status
        self.p4 = p4
        self.b1, self.b2, self.b3, self.b4 = '', '', '', ''
        self.encode()
        
        
       
    def encode(self):
        self.encode_p1()
        self.encode_p2()
        self.encode_p3()
        if self.p4:
            self.new_b1 = chr(ord(self.b1) + 128)
        else:
            self.new_b1 = self.b1
        self.enc_message = (ord(self.new_b1) << 24) + (ord(self.b2) << 16) + (ord(self.b3) << 8) + ord(self.b4)
        
    
    # encode in increments of 1
    # p3's range is from 20 to 200, increments of 1 yield 181 values which can be covered by 8 bits 
    def encode_p3(self):
        print("----------\nencoding b4")
        #compression 
        step = MessageHelper.get_step("P3")
        comp_int = self.p3 // step
        print("compression step is %i" %step)
        print("b4 = %i" %self.p3)
        # convert int to char 
        self.b4 = chr(comp_int)
    
    # encode in increments of 2
    # p2's range is from 25 to 500, increments of 2 yield 237 values
    def encode_p2(self):
        print("----------\nencoding b3")
        # compression 
        step = MessageHelper.get_step("P2")
        comp_int = self.p2 // step
        print("compression step is %i" %step)
        print("b3 = %i" %comp_int)
        # convert int to char 
        self.b3 = chr(comp_int)
    
    # encode in increments of 1
    # p1's range is from 10 to 5000
    # rewrite with left shift
    def encode_p1(self):
        print("----------\nencoding b1 and b2")
        #compression 
        step = MessageHelper.get_step("P1")
        comp_int = self.p1 // step
        print("compression step is %i" %step)
        # print("comp_int in hex %s" %hex(comp_int))
        #masking
        u_mask_hex = "0xff00"   #mask for obtaining the upper byte
        l_mask_hex = "0x00ff"   #mask for obtaining the lower byte 
        u_mask = int(u_mask_hex, 16)
        l_mask = int(l_mask_hex, 16)
        upper = (u_mask & comp_int) >> 8
        lower = l_mask & comp_int
        print("b1 = %i, b2 = %i" %(upper, lower))
        self.b1 = chr(upper)
        self.b2 = chr(lower)
        
        """
        # convert int to binary string
        p1_binary = bin(self.p1)[1:]
        p1_binary = '{:0>16}'.format(p1_binary[1:])
        # divide into the first byte and second byte
        p1_b1 = p1_binary[:8] 
        p1_b2 = p1_binary[8:]
        # convert strings back to int and then to one byte chr
        self.b1 = chr(int(p1_b1, 2))
        self.b2 = chr(int(p1_b2, 2))
        """
        
    # not accouting for the most significant bit 
    def print_param(self):
        print("----------\nprinting parameters")
        # decompress param 
        print("StimAmp:", ord(self.b1) * 256 + ord(self.b2))
        print("Stim PW:", ord(self.b3) * 2)
        print("Stim Freq:", ord(self.b4))
        print("Stim status", self.p4)
        # compressed chr representation 
        print("chr message:", self.new_b1, self.b2, self.b3, self.b4)
        # compressed hex representation 
        print("Binary message:", hex(ord(self.new_b1)), hex(ord(self.b2)), hex(ord(self.b3)), hex(ord(self.b4)))
        print("int message %i" %self.enc_message)
        print("done\n----------")
