# Asymptotic Notation

Think about an asymptote, the imaginary line on a graph that is as close to it as possible.
We are about the tail end of a function on a graph, or it's behavior as it scales.

```
https://www.youtube.com/watch?v=0oDAlMwTrLo
```

## Big O

    Big O is the Upper Bound of your algorithm's complexity.

Imagine a graph. On this graph is a function. This function is the actual function that our algorithm is producing.

Big O is an upper bound function that is as closely related to our algorithm's function as possible. The Upper bound function lies on top of our algorithm and matches its behavior.

This means that at worst-case, our algorithm will behave like this function.

## Big Omega

    Big Omega is the Lower Bound of your algorithm's complexity.

Imagine a graph. On this graph is a function. This function is the actual function that our algorithm is producing.

Big Omega is the lower bound function that is as closely related to our algorithm's function as possible. The Lower bound function lies below of our algorithm and matches its behavior.

This means that at best-case, our algorithm will behave like this function.

## Big Theta

    Big Theta is the Exact Bound of your algorithm's complexity.

Imagine a graph. On this graph is a function. This function is the actual function that our algorithm is producing.

Big Theta is the intersection of upper and lower bound functions (meaning a single point).

---

## O(log n)

* Think about halving (tree traversal or binary search)

Log<sub>2</sub>16 = 4
4<sup>2</sup> = 16

    This means that it takes 4 steps to get to the answer. 
    (4 steps of halving 16 to get to 1)
    16 -> 8 -> 4 -> 2 -> 1

---

## + or x

    If algorithm says do this, then that... add O(a + b)
    If algorithm says do this for each time you do that... multiply O(a x b)