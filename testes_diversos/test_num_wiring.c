#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>


int main()
{
    printf("1");
    wiringPiSetupGpio();
    printf("2");
    pinMode (20, OUTPUT) ;
    pinMode (16,  OUTPUT) ;

}
