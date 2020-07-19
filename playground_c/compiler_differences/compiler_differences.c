/*
compiler differences 
compiler options: 
gcc -S <filename>
gcc -S -fverbose-asm -g <filename> 

see also 
https://stackoverflow.com/questions/137038/how-do-you-get-assembler-output-from-c-c-source-in-gcc
*/

#include <stdbool.h>

int main(int argc, char const *argv[])
{
	bool a = true; 
	bool b = true; 
	bool c = false; 
	int answer = 0; 

	if (a && b && c) { answer = 1;}
	else if (a && b) { answer = 2;}
	else if (a) 	 { answer = 3;}

/*	if (a && b && c) { answer = 1;}
	else if (a && b && !c) { answer = 2;}
	else if (a && !b && !c) { answer = 3;}
*/
	return 0;
}