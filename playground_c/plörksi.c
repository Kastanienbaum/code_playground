// plorksi  

#include <stdio.h>

int main(void)
{
	char *plorksi = "plorksi"; 
	printf("%s\n", (int)plorksi == 42 ? plorksi : plorksi ? plorksi : 24 ? plorksi : plorksi);
	return 0;
}

// EOF 