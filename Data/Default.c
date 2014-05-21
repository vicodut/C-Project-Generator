/* inclusion des librairies */
#include <stdio.h>
#include <stdlib.h>

/* definition des constantes */
#ifndef clear
	#ifdef __unix__
		#define clear system("clear")
	#elif defined _WIN32
		#define clear system("cls")
	#endif
#endif
#ifndef flush
	#ifdef __unix__
		#define flush __flush(stdin)
	#elif defined _WIN32
		#define flush fflush(stdin)
	#endif
#endif

/* prototypes des fonctions */

/* fonction main : fonction principale du programme */
int main(int argc, char const *argv[])
{
	/* variables locales */
	/* instructions */

	return 0;
}