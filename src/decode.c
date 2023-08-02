#include "decode.h"

typedef struct{
    short stim_amp;
    char stim_pw;
    char stim_freq;
    char stim_status;
}message;



message* decode(char b1, char b2, char b3, char b4){
    message *my_message;

    char amp_mask = 0x3;
    char status_mask = 0xFC;

    my_message->stim_amp = (b1 & amp_mask) * 256 + b2;
    my_message->stim_pw = b3 * 2;
    my_message->stim_freq = b4;
    my_message->stim_status = (b1 & status_mask);

    return my_message;
}