# Challenge Title
Write a function called "insertShiftArray"
that takes in an array and a value to be
added.  Without utilizing any of the built-in
methods available to your language, return
an array with the new value added at the
middle index.

## Whiteboard Process

* Whiteboard day 2
![Challenge 2 Whiteboard](./images/My%20Day%202%20Whiteboard.png)

## Approach & Efficiency
def function that takes array
and inserts new given value
at the middle position.  this
function only cares about
array index orders, nothing else.

Time O(n)
Space O(1)

## Solution

def insertShiftArray(array, value)

	midIdx = len(array) -1 // 2

	left = array[0 : midIdx]

	right = array[midIdx + 1 :]

	result = left + value + right

	return result

### Day 2 Collaborators
- Logan Reese
- TA: Brandon & Tammy
