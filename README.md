# Delete and Earn using Python
Given an array of integers, maximize points received as you delete elements using the following rules:
- Delete all elements of your chosen value.  Add the sum of those values to your points.
- Delete all elements equal to your chosen value plus or minus 1.  No points are scored with these deletions.
- Once the entire array has been processed and there are no elements left, return the integer value of points calculated.

 
For example, the given array is elements = [5, 6, 6, 4, 11].  First, delete 11 for a score of 11.  
Since there is no value 11-1 = 10 or 11 + 1 = 12, proceed with elements = [5, 6, 6, 4]. Choose to delete the two 6's for 12 more points. 
Delete any 6-1=5 and 6+1 = 7 elements: elements = [4].  Delete the 4 for 4 points. The total score is 11 + 12 + 4 = 27.
