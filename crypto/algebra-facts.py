
# coding: utf-8

# ### The extended greatest common divisor algorithm
# 
# _burt rosenberg
# <br>
# 1 november 2019_
# 
# The GCD algorithm computes the greatest common divisor by 
# repeatedly reducing the problem as,
# $$
# gcd(a,b) = gcd(b,a\bmod b)
# $$
# until the recursion halts at 
# $$
# gcd(d,0)=d
# $$
# The extended version also keeps track of the quotient of the mod reduction, 
# and updates an s, t such that on completion,
# $$
# d = s\, a + t\, b
# $$
# which is also known as Bezout's equation.
# 
# This allows the fast computation of the inverse s of an integer a mod n from,
# $$
#    1 = s\,a + t\,n
# $$






def extended_gcd(a,b):
	"""
	extended GCD algorithm. recursive.
	returns (d,s,t) where d = s*a+t*b 
	and d = gcd(a,b)
	"""
	assert(
		a>=0 and b>=0 )
	if b==0:
		return (a,1,0)
	(q,r) = divmod(a,b)
	(d,s,t) = extended_gcd(b,r)
	# gcd(a, b) == gcd(b, r) == s*b + t*r == s*b + t*(a - q*b)
	return (d,t,s-q*t)


def test_e_gcd(n):
	for i in range(n):
		(d,s,t) = extended_gcd(i,n)
		if d==1:
			# check the inverse property
			if (i*s%n)!=1:
				print("***failed***")
				return
		else:
			# check the divisibility property
			if i%d!=0 or n%d!=0:
				print("***failed***")
				return
	print("***passed***")

            
test_e_gcd(100000)


# The Lagrange property is that a subgroup divides the order of a group; and that 
# subgroup can be "shifted" to create a partition of the items not in the subgroup 
# into cosets. The Euler Phi function calculates how many of each subgroup 
# size there will be.




def invertibles(n):
	xr = [i for i in 
		filter(lambda x: (extended_gcd(x,n)[0]==1),
				range(1,n))]
	xnr = [i for i in filter(lambda x: (x not in xr),
				range(n))]
	return xr, xnr


def generalized_orbit(g,n):
	"""
	The generalized orbit of g mod n is the permutation on Zn 
	multiplication by g, x goes to x*g%n.
	"""
	o = [1]
	if extended_gcd(g,n)[0]!=1:
		return o
	if g!=1:
		o += [g]
		while (o[-1]*g)%n!=1:
			o += [(o[-1]*g)%n]
	O = [o[:]]

	def flatten(O):
		l = []
		for o in O:
			l += o
		return l

	xr, xnr = invertibles(n)
	for l in range(0,len(xr)//len(o)):
		for x in xr:
			if x not in flatten(O):
				O += [[j*x%n for j in o]]
	return O

def visualize_orbit(n):
	xr, xrn = invertibles(n)
	#print("inv:",xr)
	print([xrn[0]],"\n   non-invertibles:",xrn[1:])
	g_o = []
	for g in xr:
		g_o += [generalized_orbit(g,n)]
	g_o = [y for (x,y) in sorted([(len(x),x) for x in g_o],reverse=True)]
	for g in g_o:
		if len(g)==1:
			print(g[0],"\n   ",g[0][1],"generates group")
		elif len(g[0])==1:
			print(g[0],"\n   invertibles:",g[1:])
		else:
			print(g[0],"\n   cosets:")
			for g1 in g[1:]:
				print("  ",g1)

def noninvt(n):
	xn, xnr = invertibles(n)
	print("\ninvertible times an non-invertible")
	for x in xn:
		print(x,[i*x%n for i in xnr])
	print("\nproduct of non-invertibles")
	for x in xnr:
		if x==0:
			continue
		print(x,[i*x%n for i in xnr])

visualize_orbit(15)
noninvt(15)


def euler_phi_function(n):
	"""
	phi(n) = n Prod (1-1/p), all primes p|n.
	"""
	return len(invertibles(n)[0])

def proof_of_eulers_theorem(n):
	"""
	Euler's is a generalization of little fermat for 
	any n. its proof can be that the map Zn->Zn multiplication
	by a where a is rel prime to n, is a permutation.

	Little fermat is the case n is a prime.
	"""
	xn, xnr = invertibles(n)
	# phi = len(xn)
	phi = euler_phi_function(n)
	for x in xn:
		p = [x*i%n for i in xn]
		if sorted(p)!=sorted(xn):
			print("***fail***")
		if pow(x,phi,n)!=1:
			print("***fail***")
	print("***passed fermat test***")


def wilsons_theorem(n):
	"""
	Gauss proved the generalization that 
	the product of all numbers relatively
	prime to n between 1 and n-1, 
	is -1 in the cases 
	- the power of an odd prime
	- twice such a number
	- or 4
	and 1 in all other cases.
	"""
	xn, xnr = invertibles(n)
	p = 1
	for x in xn:
		p = (p*x)%n
	if p==(n-1):
		p = -1
	if p==1:
		print("***not a prime***")
	elif p==-1:
		print("***a prime power, twice a prime power, or 4***")
	else:
		print("***fail***")


proof_of_little_fermat(113)
wilsons_theorem(113)

