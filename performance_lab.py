# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    most_common = numbers[0]

    for num in counts:
        if counts[num] > counts[most_common]:
            most_common = num

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because we go through the list.
- Worst-case: O(n), because we count each number and check the counts.
- Average-case: O(n), because dictionary lookups are usually fast.
- Space complexity: O(n), because the dictionary may store every number.
- Why this approach? A dictionary makes counting numbers easier and faster.
- Could it be optimized? Using a dictionary is already efficient enough in my book.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n), because we check every number in the list.
- Worst-case: O(n), because each number is checked once.
- Average-case: O(n), because checking a set is usually O(1).
- Space complexity: O(n), because we store numbers in a set and a new list.
- Why this approach? It removes duplicates without changing their order.
- Could it be optimized? A set is faster than checking a list for duplicates.
- Trade-offs: It uses extra memory to make the program faster.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)

        seen.add(num)

    return sorted(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n), because we check every number.
- Worst-case: O(n), because we only go through the list once.
- Average-case: O(n), because checking a set is usually O(1).
- Space complexity: O(n), because we store numbers in a set and pairs in a list.
- Why this approach? Using a set makes finding matching numbers faster.
- Could it be optimized? This is already faster than using two nested loops.
- Trade-offs: It uses extra memory to avoid checking every possible pair.
"""
"""
Optimization for Problem 3:
My original solution used a list to store matching pairs.
This worked, but it could return duplicate pairs when numbers
were repeated. I improved it by using a set to store unique
pairs and sorting each pair so the order is consistent.

The original solution had O(n) average time complexity.
The improved solution has O(n + k log k) average time
complexity because the final k pairs are sorted.
The space complexity is O(n).

The trade-off is that sorting adds some extra work, but
the results no longer contain duplicate pairs.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    size = 0
    items = [None] * capacity

    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            new_items = [None] * new_capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            capacity = new_capacity

            print("Resized list to capacity:", capacity)

        items[size] = i
        size += 1

    return items[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list is full, its capacity doubles.
- Worst-case for a single append: O(n), because existing items must be copied.
- Amortized time per append: O(1), because resizing does not happen every time.
- Space complexity: O(n), because the list uses space based on how many items are added.
- Why does doubling reduce the cost overall? It gives extra room so the list does not need to resize every time an item is added.
- Trade-offs: Doubling uses extra memory, but it makes adding items faster overall.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_totals(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because we go through every number once.
- Worst-case: O(n), because every number must be added.
- Average-case: O(n), because the loop always processes the list.
- Space complexity: O(n), because we create a new list for the totals.
- Why this approach? It is simple and only requires one loop.
- Could it be optimized? This is already efficient because we only go through the list once.
- Trade-offs: We use extra memory to keep the original list unchanged.
"""


'Problem 1 Test'

assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5, 5, 2]) == 5
assert most_frequent([7]) == 7
assert most_frequent([]) is None

print("Problem 1 tests passed!")

'Problem 2 Test'

assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([3, 2, 1]) == [3, 2, 1]

print("Problem 2 tests passed!")

'Problem 3 test'

assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert set(find_pairs([1, 2, 3], 10)) == set()
assert set(find_pairs([], 5)) == set()
assert set(find_pairs([-2, 1, 4, 6], 4)) == {(-2, 6)}

print("Problem 3 tests passed!")

'Problem 4 Test'

assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

print("Problem 4 tests passed!")

'Problem 5 Test'

assert running_totals([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
assert running_totals([5, 5, 5]) == [5, 10, 15]
assert running_totals([]) == []
assert running_totals([-1, 2, -3]) == [-1, 1, -2]
assert running_totals([10]) == [10]

print("Problem 5 tests passed!")


assert find_pairs([1, 1, 4, 4], 5) == [(1, 4)]
print("Optimized Problem 3 test passed!")