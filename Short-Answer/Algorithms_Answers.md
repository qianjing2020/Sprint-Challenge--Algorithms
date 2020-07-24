#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3)


b) O(n*logn)


c) O(2^n)

## Exercise II

Problem:
We don't know which floor is safe to drop eggs so we have lots of eggs to test out. Drop eggs from different floors of a n-story building, if floor <= f, egg safe, other wise egg broken. Find f, and minimize the egg use. 

Algorithm/psuedocode:

Set initial condition: f = 0 (ground floor), egg_broken = 0 (false)
Start from ground floor, drop egg
If egg_broken is true: 
    return 0
While egg_broken is false AND f <= n
    f = f+1 
return f

Runtime is O(1) because my algorithm starts from floor 0, rather than floor n. And since f depends on egg physics rather than n, finding f would take a constant time!