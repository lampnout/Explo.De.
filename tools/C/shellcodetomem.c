/*

    this program places the provided shellcode into a buffer
    
    example:
    
           $ gcc -o shellcodetomem shellcodetomem.c
          
           $ shellcodetomem.c \xdf\x25\x3a 
    
    \xdf\x25\x3a will be treated as a character argument and characters x d f x 2 5 x 3 a
    will resepctively be placed into the buffer in consecutive memory locations
    
    this tool transforms the input string into: d f \0 2 5 \0 3 a \0
    
    next step is to use strtol to convert the string to an integer
    this integer will be placed in a buffer called shellcode
    this is the actual step of storing the shellcode into the memory
    
    it can also be used to edit/expand the shellcode
    
*/

#include<stdio.h>
#include<stdint.h>
#include<stdlib.h>

int main(int argc, char **argv)
{
        uint8_t *shellcode;
        int i=0, count=0, count2=0;

        // usage
        if ( argc != 2 )
        {
                printf("\nshellcodetomem.c <shellcode>\n\n");
                exit(0);
        }

        // length of the input
        while ( argv[1][i++] != '\0' )
                count++;

        // length of the shellcode
        count = count/3;
        count2 = count;

        // given the shellcode, change each char from xXX to XX\0
        // e.g. \x55 will be 55\0
        // each pair must be null terminated for later use in strtol
        i=0;
        do
        {
                argv[1][i] = argv[1][i+1];
                argv[1][i+1] = argv[1][i+2];
                argv[1][i+2] = '\0';
                i=i+3;
        } while ( count-- != 1 );

        // allocate memory for the shellcode
        shellcode = (uint8_t *)malloc(sizeof(uint8_t)*count2);
        
        // transform each pair of characters into a number
        // e.g. \x55 will be saved as chars x 5 5
        // strtol will transform 5 5 into a number
        int j=0;
        for (i=0; i<count2; i++)
        {
                shellcode[i] = (unsigned char) strtol(&argv[1][j], NULL, 16);
                j=j+3;
        }

        // print the shellcode with the egg
        // egg + shellcode
        printf("\n[+] shellcode:\n");

        for (i=0; i<count2; i++)
                printf("\\x%02x", shellcode[i]);
        printf("\n\n");

        return 0;
        
}
