#include<stdio.h>

int main(void){
  printf("Payload size: 256 bytes\n");
	printf("\"");
	for (int i=0; i<256; i++){
		if ((i%15)==0 && i!=0){
		  printf("\"\n\"", i);
		}
		printf("\\x%02x", i);
	}
	printf("\"\n");
	return 0;
}
