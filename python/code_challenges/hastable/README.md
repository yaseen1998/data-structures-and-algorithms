## Hashtables
A data structure that makes it easier to search for a value inside a list, each value will have a hash generated by a hash function and stored in an index equal to this hash, if we have a key, we will use the same algorithm to produce its hash and retrieve it from the list

## Challenge
Create a class for hashtable, include methods to hash a key, get a key, and check if the key is stored in the hashtable

## Approach & Efficiency
In case of no collision big o of time and space will be o(1), with collision, the big o will be o(n) where n here represents the number of values having the same hash and not the list length.

##
test 1  add to hashtable
test 2 get from hashtable
test 3 get from hashtable elemint does not exist
test 4 get from hashtable group of item
test 5 get from hashtable one of group of item
test 6 check if elemnt exist true
test 7 check if elemnt exist false
