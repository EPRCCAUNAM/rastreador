#include <16F88.h>
#device ADC=10

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES WRT                      //Program Memory Write Protected
#FUSES PROTECT                  //Code protected from reads
#FUSES NOMCLR   

#use delay(internal=8000000)
#use rs232(uart1, baud=9600)
//#use i2c(SLAVE,I2C1,force_hw,FAST,address=0x60)

