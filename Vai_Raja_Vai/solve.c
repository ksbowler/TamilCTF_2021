#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
	unsigned int nowtime = (unsigned int) time( NULL );
	printf("%u\n",nowtime+10);
	srand(nowtime+10);
	int a,b,x;
	a = 0;
	b = 1;
	int val[53];
	while(b < 301) {
		if(b%6 == 0) {
			val[b/6-1] = a;
			a = 0;
			x = rand();
			a += x%7;
		} else {
			x = rand();
			a += x%7;
		}
		b++;
	}
	for(int i=0;i<53;i++) {
		printf("%d %d\n",i,val[i]);
	}
	printf("%u\n",nowtime+10);
}
