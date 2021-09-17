# Data Structures

## Array / List

    Python Arrays are dynamic (not static), which means it creates memory allocations and you wont run into ArrayOutOfBoundsException (adding to a list that doesnt have enough memory).
    Arrays are stored in contiguous memory locations.

    * Lookup by index               O(1)
    * Lookup by value               O(n)
    * Traversal                     O(n)
    * Insert at start/middle        O(n) --- this is a problem because when you insert a number into an Array, the proceeding values are copied over and moved to the next index (which takes a lot of time)
    * Insert at end                 O(1)
    * Delete                        O(n)

## Linked List

    Benefits over Array/List, insert is easier. No need for pre-allocated memory.
    Unlike List, Linked List is stored in random memory locations and linked by pointers. This is why insert is much faster, you only need to update the references to a memory location.
    So a linked list has both the value, and the pointer (which stores the reference of the memory location of the next value).

    * Lookup by index               O(n)
    * Lookup by value               O(n)
    * Traversal                     O(n)
    * Insert/Delete at start        O(1)
    * Insert/Delete at middle/end   O(n)

## Doubly Linked List

    Reference to memory locations back and forth.

## Hash Table / Dictionary

    Collision handling means that sometimes a key will have the same index as another key, meaning that 2 keys are pointing to the same value, which is wrong. 
    To solve this, there are 2 options: chaining and linear probing.
    
        Chaining: store multiple values in a memory location as a list.
        Therefore, when we look up an index in the Hash Table, it will point to memory with a list and depending on the size of the list will be O(n).

        Linear Probing: instead of storing multiple values in the same memory location as a list, we put the next value into an empty memory location. it will search for an empty slot in memory.

    * Lookup by key                 O(1)
    * Insert                        O(1)
    * Delete                        O(1)

## Stack

    Recommended way to use Stack in Python is from collections import deque because it is implemented with a doubly list rather than a list (which is dynamic and wastes memory).

    * Push                          O(1)
    * Pop                           O(1)
    * Lookup by value               O(n)

## Binary Search Tree

    In Binary Search Tree, nodes are not duplicated and the left children are always less than the parent node. The right child is always greater than the parent node.

    Breadth First Search:

    Depth First Search:
    1. In Order Traversal --- will list the node values in order --- left, node, right
    2. Pre Order Traversal
    3. Post Order Traversal

    Deleting a node, there are 3 options:
    1. Delete node with no children (leaf nodes)
    2. Delete node with 1 child
    3. Delete node with 2 children --- in this case, take all right children and get the lowest value and move it up.

    * Search                        O(log n) ----   n=8     8, 4, 2, 1      3 iterations        log 8 = 3

## Undirected Graph

    No direction between two nodes.
    Has nodes and edges.

## Directed Graph

    Nodes can have multiple directions between nodes.
    Edges can be weighted.