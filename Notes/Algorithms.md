# Algorithms

## Binary Search

    Binary Search must be done on a sorted list.
    Linear Search is O(n) and can take a long time.
    Dividing search space by half. Then remove all to the left.
    Binary Search is O(log n)

## Bubble Sort

    Loop through the array and look at the first two numbers, then compare their size. The smaller value should swap place to the left.

    Nested for loops then compare their values.
    Time Complexity     O(n^2)
    Space Complexity    O(1)

## Quick Sort / Divide and Conquer

    First element is called pivot.
    After pivot is moved into correct position, all elements to the left must be smaller than it, and all the elements to the right must be greater than.
    Process of moving pivot to correct position and having two arrays to the left and right of it, is called partitioning.

    Two Types of Partitioning:
    1. Hoare
        Start pointer is after the pivot element. There is also an end pointer. 
        With start pointer, compare value to pivot to find a value greater than pivot. Once found, stop pointer.
        With end pointer, compare value to pivot to find a value less than pivot. Once found, end pointer.
        Then swap value of start and end pointer.
        Repeat process until end pointer is before start pointer. At this point, swap the pivot value with the end pointer.
        Finally, repeat the steps with both left and right partition.
    2. Lomuto
        End element is pivot. Start pointer is called P index.
        Move P index right until it is greater than pivot.
        Now i is a pointer created and moved right of P index until it finds a value less than pivot.
        Swap P index and i values.
        Move P index right until value is greater than pivot.
        i moves until it finds value less than pivot.
        Swap P index and i values.
        Repeat.

    Complexity is O(n^2)

## Insertion Sort

    Starts with unsorted array. An empty sorted array is created. 
    The first number of the unsorted array will be copied to the sorted array.
    Then the next number in the unsorted array is taken and compared with the value in the sorted array. Depending on the values, they are compared and the value is put to the right or left side.
    Imagine this without a second sorted array. Place those values into the same unsorted array so you arent using extra memory.
    Repeat.

    Complexity is O(n^2)

## Merge Sort

    Start with unsorted array.
    Divide array into 2 parts. Keep doing this until each array has 1 element which means it is sorted.
    Now merge each array with the other array, comparing which one is smaller than the other. This will create pairs.
    Continue process.

    Complexity O(n log n)

## Shell Sort

    Optimization of insertion sort.
    Looks at unsorted array and finds a subarray based on gaps.
    It will sort the gap values, then move the pointers of the gaps and continue to sort.
    This sorting of the gaps causes the bigger numbers to move towards the end (because an issue with insertion sort is when small numbers are at the end, this algorithm makes sure larger numbers are at the end)
    Reduce your gap number and repeat until gap number is 1.
    Once gap is 1 we do insertion sort.

    Complexity O(n^2)

## Selection Sort

    In unsorted array, find smallest element then swap it with the first element. 
    Repeat.

    Complexity O(n^2)
