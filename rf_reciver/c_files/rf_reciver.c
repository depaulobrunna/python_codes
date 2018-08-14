#include <stdio.h>    // Used for printf() statements
#include <wiringPi.h> // Include WiringPi library!

int = sinal;

int pin_set();
int decod(temp);
int delta_tempo_edge();
int delta_tempo_fall();

int main()
{
    pin_set();


}

int pin_set()
{
    pinMode(16, INPUT);
    pinMode(20, INPUT);
    pullUpDnControl(16, PUD_DOWN);
    pullUpDnControl(20, PUD_DOWN);
     
}
int decod(temp)
{
    if (temp < 0.0005)
    {
        sinal=0;
        return(sinal)
    }
    if (0.01 > temp > 0.0005)
    {
        sinal=1;
        return(sinal)
    }
}
