"""
Description:

Given multiple lists (name, age, height), each of size n :

An entry contains one name, one age and one height.
The attributes corresponding to each entry are determined by the index of each list.
For example, the first entry is comprised of the first elements of each list,
the second entry is comprised of the second elements of each list, etc.

A duplicate entry is one in which the name, age and height are ALL the same.

Write a function which takes in the attributes for each entry and returns an integer
for the number of duplicated entries. For a set of duplicates,
the original entry should not be counted as a duplicate.
"""


def count_duplicates(names, ages, heights):
    # Combine the attributes into a single list of tuples
    entries = list(zip(names, ages, heights))
    print(entries)

    # Use a dictionary to count occurrences of each entry
    entry_counts = {}
    for entry in entries:
        if entry in entry_counts:
            entry_counts[entry] += 1
        else:
            entry_counts[entry] = 1

    # Find keys with counts > 1
    duplicates = {key: count for key, count in entry_counts.items() if count > 1}

    # Output the duplicate keys
    print("Duplicate entries:")
    for key, count in duplicates.items():
        print(f"{key}: {count} times")

    # Count entries that occur more than once (duplicates)
    duplicate_count = sum(count - 1 for count in entry_counts.values() if count > 1)
    return duplicate_count


# Example usage:
names = ["Alice", "Bob", "Alice", "Charlie", "Alice"]
ages = [25, 30, 25, 35, 25]
heights = [5.5, 6.0, 5.5, 5.9, 5.5]

print(count_duplicates(names, ages, heights))  # Output: 2
