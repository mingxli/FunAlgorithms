'''
Hi there, this is a quick demo of the Prefix Sum Algorithm, which is used to solve the Array Manipulation code challenge on the HackerRank.
For the actual code challenge, can do a browser search for "hackerrank array manipulation".

Basic concepts:
 - Multi-dimensional arrays
 - Loops

Objective:
 - Find the max value in the array.

Challenge Description:
You started with a two-dimensional array as illustrated in the following:

**This is a conceptual description, may not identically matched the descriptions on HackerRank.

			   input queries
 1  2  3  4  5		      a  b  k
[0, 0, 0, 0, 0, ..., n]      [1, 5, 3]
[3, 3, 3, 3, 3, ..., n]      [4, 5, 2]
[3, 3, 3, 5, 5, ..., n]

In the illustration above, there are 'n' number of columns in the array table, 
number of rows is 3 (1 default row of [0, 0, 0, 0, ...., n] + 2 rows from the input queries).

For the method declaration of "def arrayManipulation(n, queries)", where "n" is number of columns, and "queries" is an array with 3 values a, b, and k:
 a - is the starting index of the array, where 1 <= a <= n.
 b - is the ending index of the array, where 1 <= b <= n.
 k - is the value to add to the array from index position 'a' to index position 'b', 0 <= k <= 10^9.



To understand how this algorithm works, a good resource is on YouTube, just search for "array manipulation hackerrank solution" 
by "JAVAAID - Coding Interview Preparation", it's a 29 minutes video, but very informative :).
'''

def arrayManipulation(n, queries):
	array = [0]*(n+1) # Declare array of 0s in the n+1 length
	
	for query in queries:
		a = query[0]
		b = query[1]
		k = query[2]
		array[a-1] += k   # a-1: because array is 0 index base.  
		array[b] -= k     # b: this is part of the Prefix Sum Algorithm.

	print(array)
	
	# Apply Prefix Sum Algorithm to get the max value.
	maxValue = 0
	value = 0
	for i in array:
		value += i
		if value > maxValue:
			maxValue = value
	
	return maxValue

# Sample test case
queries = [[1,5,3], [4, 5, 2]]
result = arrayManipulation(5, queries)
print(result)


