'''3/11/2003'''
"""Ronin Deschamps"""
"""I Pledge my honor that I have abided by the Stevens Honor System"""

# lab exercise: circuits in Python 

# Study the comments and code provided,
# before doing the exercises.


# Logic gates; should only be applied
# to "bits", i.e., either 0 and 1
def gnot(x):
    assert x in [0,1]
    return int(not(x)) 
def gand(x,y):
    assert x in [0,1] and y in [0,1]
    return x and y
def gor(x,y):
    assert x in [0,1] and y in [0,1]
    return x or y


# Example: XOR
# Definition x y | x xor y
#            0 0 | 0
#            0 1 | 1
#            1 0 | 1
#            1 1 | 0
# Here is an expression for the 1-rows, using ! for not
#   !xy + x!y 
# Here is code using only the logic gate functions:
def XOR(x,y):
    return gor( gand(gnot(x),y), gand(x,gnot(y)) )

def testXOR():
    assert XOR(0,0) == 0
    assert XOR(0,1) == 1
    assert XOR(1,0) == 1
    assert XOR(1,1) == 0
    print("testXOR success")


# EXERCISE
# Define this function as a single return using
# only the logic gate functions.
def gor3(x,y,z):
    '''Or of three inputs.'''
    return gor(z, gor(x, y))


# EXERCISE
# Full adder.  See Lecture 6 slide 10
# Implement this as a single return, using only
# the logical gate functions. 
# You may also use gor3 or similar helper functions
# that you write using just gates.
# And you may use assigned-once variables:
# think of those as named wires.

def gand3(x, y, z):
    '''and of three inputs'''
    return gand(z, gand(x, y))

def  XOR3(x, y, z):
    '''or all three inputs'''
    return XOR(z, XOR(x, y))

def FA(x,y,z):
    return (gor(gand(x, y), (gand(z,XOR(x, y)))), XOR3(x, y, z))


def FAtest(x,y,c):
    '''Compute FA using integer arithmetic.'''
    s = (x+y+c) % 2
    d = 1 if x+y+c >= 2 else 0
    return (d,s)

def testFA():
    assert FA(0,0,0) == FAtest(0,0,0) 
    assert FA(0,1,0) == FAtest(0,1,0) 
    assert FA(1,1,1) == FAtest(1,1,1)
    print("testFA successful on 3 out of 8 cases")


# Review slide 12 of Lecture 6 ("A Circuit for Adding") before continuing.

def twoBitAdd(xx,yy):
    '''Assume xx and yy are pairs (xt,xo) and (yt,yo) of bits.
    Return (cout,(zt,zo)) where (zt,zo) is their two-bit sum
    is the carry bit. Note: xo is the one's place and xt is
    the two's place.  ALERT: use the notation xx[0] to refer to xt,
    and xx[1] to refer to xo.'''
    (c,zo) = FA(xx[1],yy[1],0)
    (d,zt) = FA(xx[0],yy[0],c)
    return (d,(zt,zo))
# Notice the assignments to two variables at once,
# which only works if the right-hand side evaluates to a pair.


def test_twoBitAdd():
    zero = (0,0)
    one = (0,1)
    two = (1,0)
    three = (1,1)
    c,ww = twoBitAdd(one,zero)
    assert( ww == (0,1) and c == 0 )
    c,ww = twoBitAdd(one,one)
    assert( ww == (1,0) and c == 0 )
    c,ww = twoBitAdd(three,three)
    assert( ww == (1,0) and c == 1 )
    print("test_twoBitAdd worked (but incomplete test)")


# EXERCISE: implement the following, using gates and/or FA.
# Hint: you might start by defining something like twoBitAdd
# but that also has a carry input.

def TwoBitAddCarry(xx, yy, cin):
    """two bit add with carry"""
    (c, z) = FA(xx[1], yy [1], cin)
    (d, zt) = FA(xx[0], yy[0], c)
    return (d, zt, z)


def fourBitAdd(xxxx,yyyy):
    '''Assume xxxx is a quadruple (xe,xf,xt,xo) of four bits,
    with xe the high-order bit (i.e., eight's place).  Likewise
    yyyy.  Return (c,zzzz) where zzzz is their four-bit sum
    and c is the carry.'''
    (c, z, zo) = TwoBitAddCarry(xxxx[2: ], yyyy[2: ], 0)
    (d, ze, zf) = TwoBitAddCarry(xxxx[ :2], yyyy[ :2], c)
    return(d, (ze, zf, z, zo))

# EXERCISE: implement the following.
def test_fourBitAdd():
    '''at least four test cases'''
    assert fourBitAdd((1, 1, 0, 0), (0, 0, 0, 0)) == (0, (1, 1, 0, 0))
    assert fourBitAdd((1, 1, 0, 0), (0, 0, 1, 1)) == (0, (1, 1, 1, 1))
    assert fourBitAdd((1, 1, 0, 1), (1, 0, 1, 1)) == (1, (1, 0, 0, 0))
    assert fourBitAdd((1, 0, 0, 0), (1, 1, 1, 1)) == (1, (0, 1, 1, 1))
    print("test_fourBitAdd Passed")
    
