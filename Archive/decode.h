#ifndef DECODE_DOT_H
#define DECODE_DOT_H

typedef struct{
    short stim_amp;
    char stim_pw;
    char stim_freq;
    char stim_status;
}message;

message* decode(char b1, char b2, char b3, char b4);

#endif /* DECODE_DOT_H*/