# Elements of Programming Interview in Python

## Skipped Sections:

1. Skipped chapters 1-3 because those are based on interview steps. Need to read later, before interviewing.
2. Skipped chapter 4 (Primitives) because too detailed. Come back  to this later.

---

## Array

### Operation Complexity:

| Operation |  Complexity | 
| ----------- | ----------- | 
| Append (at end) |  O(1) |
| Pop (at end) | O(1) |
| Insert (start/middle) | O(n) |
| Delete | O(n) |
| a in Array | O(n) | 


### Tips:
    - Array problems usually use the array itself to reduce space complexity to O(1)
    - Try to insert at back instead of front. 
      - Insert at front takes more time than end because elements have to be copied to the next position.
    - Instead of deleting an entry, consider overwriting.

* Contiguous block of memory

---

