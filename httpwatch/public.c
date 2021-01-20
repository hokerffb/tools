#include "public.h"

void hex_print(const u_char *buf, int len, int offset) 
{ 
	    u_int i, j, jm; 
		    int c; 

			    printf("\n"); 
				    for (i = 0; i < len; i += 0x10) { 
						          printf(" %04x: ", (u_int)(i + offset)); 
								            jm = len - i; 
											          jm = jm > 16 ? 16 : jm; 

													            for (j = 0; j < jm; j++) { 
																	                if ((j % 2) == 1) 
																						                    printf("%02x ", (u_int) buf[i+j]); 
																					                else printf("%02x", (u_int) buf[i+j]); 
																									          } 
																          for (; j < 16; j++) { 
																			                  if ((j % 2) == 1) printf("   "); 
																							                  else printf(" "); 
																											            } 
																		            printf(" "); 

																					          for (j = 0; j < jm; j++) { 
																								                  c = buf[i+j]; 
																												                  c = isprint(c) ? c : '.'; 
																																                  printf("%c", c); 
																																				            } 
																							            printf("\n"); 
																										    } 
}

// not support multi thread
char* Substr(const char*str, unsigned start, unsigned end)
{
    unsigned n = end - start;
    static char stbuf[256];
    strncpy(stbuf, str + start, n);
    stbuf[n] = 0;
    return stbuf;
}
