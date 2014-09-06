#include<stdio.h>
#include<stdlib.h>
#include<strings.h>
#include "splitter.h"

/*
 * splitter routine, to demonstrate loop invariants
 * author: burt rosenberg
 * created: 5 sep 2014
 * lastupdate:
 *
 */

int assert_loop_invariant(int a[], int n, int p, int i1, int i2) {
	/* you can write assertions into you code; there is a library assert.h, and
	   Java actually has an assertion object; usually you don't do this. But here
	   it is for illustration purposes.
	*/
	
	int j;
	j = 0 ;
	while ( j<i1 ) {
		if ( a[j]>p ) {
			return 1 ;
		}
		j++ ;
	}
	j = i2 ;
	while ( j<n ) {
		if ( a[j]<= p ) {
			return 1 ;
		}
		j++;
	}
	
    return 0 ;
}

int split(int a[], int n, int p) {
    /* pre-condition: array a with n integer elements, 
     * and an integer p 
     */
    
    int i1,i2 ;
    
    /* L.I.: array is a permutation of the original array AND:
     *  1) for all 0<=j<i1, a[j]<=p
     *  2) for all i2<=j<n, a[j]>p
     */
    
    // initialize L.I.
    i1 = 0 ;
    i2 = n ;
    
    // ASSERT L.I.
    if (assert_loop_invariant(a,n,p,i1,i2)) printf("Assertion failed!\n") ;  
    while ( i1<i2 ) {
    	int t ;
    	
#ifdef VERBOSE
    	// check L.I. if we were to advance i1++
        if (assert_loop_invariant(a,n,p,i1+1,i2)) printf("L.I. fails.\n");
#endif

        if ( a[i1]>p ) {
           // L.I. would fail, fix it
           i2 -= 1 ;
           t = a[i2] ;
           a[i2] = a[i1] ;  // a[i1]>p so it belongs at an index between j2 and n
           a[i1] = t ;      // we don't know much about t
        }
        else {
           // L.I. would be ok, advance l1
           i1 += 1 ;       // a[i1]<=p, before the advance of i1
        }

        // ASSERT L.I.
        if (assert_loop_invariant(a,n,p,i1,i2)) printf("Assertion failed!\n") ; 
    }
    /* termination: each time through the loop either i2 decreases by one, 
     *  or i1 increases by one. 
     */
    
    
    /* post-condition: a permutation of the elements of a and an integer i such
     * that a[j]<=p for all 0<=j<i, and a[j]>p for all i<=j<n
     */
    return i1 ;
}
