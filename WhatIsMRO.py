'''
What is the MRO in Python?
------------------------------
MRO --> Method Resolution Order
-------------------------------
In Python, the MRO is from bottom to top and left to right. This means that,
first, the method is searched in the class of the object. If it’s not found,
it is searched in the immediate super class. In the case of multiple super classes,
it is searched left to right, in the order by which was declared by the developer
e.g. C(A,B) ==>  c->A->B
'''
class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()
print(D.mro())

# MRO of D : D ->C ->A->B ->object

class A : pass
class B(A) : pass
class C(A) : pass
class D(A) : pass
class E(B,C) : pass
class F(B,D) : pass
class G(C,D) : pass
class H (E,F,G) : pass
print(H.mro())

# MRO H : HEFBGCDO
'''
MRO(H): H+MRGE(MRO(E),MRO(F),MRO(G),EFG0)
      : H +((EBCO),(FBDO),(GCDO),(EFG0))
      : H + E +((BCO),(FBDO),(GCDO),(FGO))
      : H +E+F+((BCO),(BDO),GCDO,GO)
      : H+E+F+B+(CO,DO,GCDO,GO)
      : H+E+F+B+G+(CO,DO,CDO,O)
MRO(H): H+E+F+B+G+C+D+O
'''