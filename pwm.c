#include <pwm.h>
int16 val_t1;

#INT_TIMER1
void  TIMER1_isr(void) 
{
   set_timer1(val_t1);
   output_toggle(pin_b3);
}

//#INT_SSP
void  SSP_isr(void) 
{

}
//val=(65536)-2*fosc/f*PRE
//freq=2*fosc/PRE(65536-val)
void main()
{
   val_t1=65023;
   setup_timer_1(T1_EXTERNAL|T1_DIV_BY_1|0x8);      //32.7 ms overflow
   set_timer1(val_t1);
   enable_interrupts(INT_TIMER1);
   //enable_interrupts(INT_SSP);
   enable_interrupts(GLOBAL);

   while(TRUE);
}
