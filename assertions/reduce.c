#include<stdio.h>
#include<stdlib.h>
#include<strings.h>


/*
 * program to demonstrate assertions, and reduce a fraction to lowest terms
 * author: burt rosenberg
 * date: 6 sep 2014
 * lastupdate:
 */
 
struct P { int a ; int b ; } ;

int gcd( int a, int b ) {

	// ASSERT: 0 < b <= a

	while ( b!=0 ) {
		int t = a%b ;
		a = b ;
		b = t ;	
	}
	return a ;
}

struct P * reduce(struct P * p) {
	
	// ASSERT: p->a/p->b is a fraction
	
    int a, b, s, d ;
    
    if ( !p->b ) {
    	p->a = 0 ;
    	return p ;
    }
    if ( !p->a ) {
    	p->b = 1 ;
    	return p ;
    }
    
	// ASSERT: p->a != 0 && p->b != 0
	
    a = p->a ;
    b = p->b ;
    
    s = a*b ;
    s = (s<0) ? -1 : 1 ;
    a = (a<0) ? -a : a ;
    b = (b<0) ? -b : b ;
    
    if (a<b) { int t = a ; a = b ; b = t ; }
    
    // ASSERT: 0<a<=b, and (relevance requirement) s * a/b or s * b/a 
    // is the original fraction
    
    d = gcd(a,b) ; // function gcd's pre-conditions match above assertion
    
    // ASSERT: d is the gcd(a,b) (function gcd's post-condition)
	
	{
		int t ;
    	p->a = s * ( ((t=p->a/d)<0) ? -t: t );
    	p->b = ((t=p->b/d)<0) ? -t: t ;
    }
    
    // ASSERT: p->a/p->b is the original fraction in lowest terms
    
    return p ;
}

#define USAGE " numerator denominator"

int main(int argc, char * argv[]) {

	struct P * p ;
	
	if (argc!=3) {
		printf("%s%s\n", argv[0], USAGE) ;
		return 0 ;
	}

	p = (struct P *) malloc(sizeof(struct P));	
	p->a = atoi(argv[1]) ;
	p->b = atoi(argv[2]) ;
	reduce(p) ;
	printf("%d/%d\n", p->a, p->b) ;

}

