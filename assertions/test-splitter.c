#include<stdio.h>
#include<stdlib.h>
#include<strings.h>
#include "splitter.h"

/*
 * splitter routine, to demonstrate loop invariants
 * author: burt rosenberg
 * created: 5 sep 2014
 *
 * lastupdate: 6 sep 2014, 
 *			   using -D command line option to run through tests
 *
 */

#ifdef TEST1
#define A_TEST { 9,3,4,1,9,0,3,5,6,3,1,2,6,4,2,5,7,8 }
#define S_TEST 5
#endif

#ifdef TEST2
#define A_TEST { 9,3,4,1,9,0,3,5,6,3,1,2,6,4,2,5,7,8 } 
#define S_TEST 10
#endif

#ifdef TEST3
#define A_TEST { 9,3,4,1,9,0,3,5,6,3,1,2,6,4,2,5,7,8 }
#define S_TEST -1
#endif

#ifdef TEST4
#define A_TEST { 9 }
#define S_TEST 8
#endif

#ifdef TEST5
#define A_TEST { 9 }
#define S_TEST 10
#endif

#ifdef TEST6
#define A_TEST { 7,6,5,4,3,2,1,0,-1,-2 }
#define S_TEST 3
#endif

void print_array(int a[], int n, int s) {
	int i ;
	for (i=0;i<n;i++) {
    	if (i==s) printf(" | ") ;
    	printf("%d ",a[i]);
  	}
	printf("\n") ;
}

int main(int argc, char * argv[]){

	int a[] = A_TEST ;
	int n = sizeof(a)/sizeof(a[0]) ;
	int i, s ;
  
	s = split(a,n, S_TEST ) ;
	print_array(a,n,s) ;
	return 0 ;
	
}
