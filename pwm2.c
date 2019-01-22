#include <pwm.h>
int16 val_t1;
int pwm_enable;
#define init_char 0x0a
#define ok_char 0x0a
#define nok_char 0x0f
#define out_pin pin_b3

#INT_TIMER1
void  TIMER1_isr(void) 
{
   set_timer1(val_t1);
   if (pwm_enable==1)
       output_toggle(out_pin);
}
int8 low, high, state;
#INT_RDA
void  RDA_isr(void) 
{
int8 chksum;
    if (state==0)
    {
    output_low(out_pin);
        if(init_char==getc())
            state=1;
        else
            state=0;
        
    }
    if (state==1)
    {
        high = getc();
        state=2;
    }
    if (state==2)
    {
        low= getc();
        state=3;
    }
    if (state==3)
    {
         if (init_char+low+high==getc())
         {
         val_t1=high;
         val_t1=val_t1<<8;
         val_t1=val_t1+low;
         //set_timer1(val_t1);
         if (val_t1==0)
            pwm_enable=0;
         else
            pwm_enable=1;
         putc(ok_char);
         }
        putc(nok_char);
        state=0;
        low=0;
        high=0;
    }

}
//val=(65536)-2*fosc/f*PRE
//freq=2*fosc/PRE(65536-val)
void main()
{
   state=0;
   val_t1=0;
   pwm_enable=0;
   output_high(out_pin);
   setup_timer_1(T1_EXTERNAL|T1_DIV_BY_1|0x8);
   set_timer1(val_t1);
   
   enable_interrupts(GLOBAL);
   enable_interrupts(INT_RDA);
   enable_interrupts(INT_TIMER1);

   while(TRUE);
}
