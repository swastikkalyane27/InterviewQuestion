'''
A for loop runs for a pre-determined number of times. So,
it can iterate through an array from start to finish, say, but
it will only ever loop for that specific number.

A while loop will carry on until a pre-determined scenario takes place.That may happen immediately,
or it may require a hundred iterations.So,
the number of loops is governed by an outcome, not a number.
For example, you can continue looping until the user presses the Z key
(while keyPressed != 'Z') - the loop will constantly run until that happens.It may never happen.
'''
for i in range (10) :
    print(i,end=' ')
print()

i=0
while i>10:
    print(i)
    i+=1