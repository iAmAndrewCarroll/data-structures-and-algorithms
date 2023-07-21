# Day 30 Code Challenge

[Code For Today](https://github.com/iAmAndrewCarroll/data-structures-and-algorithms/pull/29)

 - [x] Top-level README “Table of Contents” is updated
 - [x] README for this challenge is complete
       - [x] Summary, Description, Approach & Efficiency, Solution
       - [x] Picture of whiteboard
       - [?] Link to code
 - [x] Feature tasks for this challenge are completed
 - [?] Unit tests written and passing
       - [?] “Happy Path” - Expected outcome
       - [?] Expected failure
       - [?] Edge Case (if applicable/obvious)

# Collaboration with Raven, chatGPT, Bard, Dan Q, Sarah G, Logan, Jared, Anthony, Slava

# Big shoutouts to ChatGPT for being the real MVP, Bard was there to but was overly verbose, Google, GitHub Repos


## Hashtable Implementation

This repository contains an implementation of a hashtable with separate chaining for handling collisions. The hashtable is used to store key/value pairs and allows efficient retrieval and update of data.

### Classes

#### Node Class

The `Node` class represents individual nodes of a linked list used for separate chaining in the hashtable to handle collisions.

#### Hashtable Class

The `Hashtable` class is the core of this implementation and provides methods for interacting with the hashtable:

- `set(key, value)`: This method is used to add or update key/value pairs in the hashtable, handling collisions using separate chaining with the linked list.
- `get(key)`: Retrieves the associated value for a given key from the hashtable. If the key is not present, it returns `None`.
- `has(key)`: Checks if a given key exists in the hashtable and returns a boolean indicating its presence.
- `keys()`: Returns a collection of all keys present in the hashtable.

### Hashing Function

The `_hash` method calculates the hash value of a given key and maps it to an index within the hashtable size. This hashing function ensures efficient distribution of keys across the hashtable.

### Test Cases

The implementation includes comprehensive test cases using `pytest` to validate the correctness of the `Hashtable` class. The tests cover scenarios such as:

- Setting key/value pairs in the hashtable.
- Retrieving values using keys and verifying correctness.
- Checking for the existence of keys in the hashtable.

Feel free to explore the code and test cases to gain a better understanding of how the hashtable works and to ensure its correctness.


