#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <wiringPi.h>
static volatile int edge = 0, fall =0;
clock_t fall_t, edge_t, delta_t;

void fall_tempo (void)
{
	fall_t = clock();
	printf("%f\n", fall_t);
}

void edge_tempo(void)
{
	edge_t = clock();
}

int main()
{
	//forma de inciar o wiringPi e usando a numeracao BCM
	if (wiringPiSetupGpio () < 0)
    {
        printf ("vish") ;
    }
	pinMode (21, INPUT) ;
    pinMode (16,  INPUT) ;
    pinMode (20, OUTPUT);
	digitalWrite(20, LOW);
    pullUpDnControl(16, PUD_DOWN);
    pullUpDnControl(21, PUD_DOWN);
	while(1)
	{
		wiringPiISR (16, INT_EDGE_RISING, &edge_tempo);
		wiringPiISR (21, INT_EDGE_FALLING, &fall_tempo);
		//digitalWrite(20, digitalRead(16));
		delta_t = (double)(fall_t - edge_t);//tempo baixo
		if(delta_t > 0.01)
		{
			digitalWrite(20, HIGH);
		}
	}
}

