"""
You've got much data to manage and of course you use zero-based and non-negative ID's
to make each data item unique!
Therefore, you need a method, which returns the smallest unused ID for your next new
data item...
Note: The given array of used IDs may be unsorted. For test reasons there may be
duplicate IDs, but you don't have to find or remove them!
"""

import numpy as np


def next_id(ids):
    """
    Convert the list to a set for O(1) average lookup time.
    :param ids:
    :return:
    """
    used_ids = set(ids)
    for i in range(len(ids) + 1):
        if i not in used_ids:
            return i
    return None


def next_id_numpy(ids):
    """
    NumPy-Based Solution.
    :param ids:
    :return:
    """
    ids_array = np.array(ids)  # Convert the list to a NumPy array
    unique_ids = np.unique(ids_array)  # Remove duplicates and sort the array
    for i in range(len(unique_ids) + 1):  # Iterate through 0 to len(unique_ids)
        if i not in unique_ids:
            return i
    return None


def next_id_vectorized(ids):
    """
    Fully vectorized approach by creating a range of integers and finding the smallest
    unused value directly.
    :param ids:
    :return:
    """
    ids_array = np.array(ids)  # Convert the list to a NumPy array
    unique_ids = np.unique(ids_array)  # Remove duplicates and sort the array
    all_possible_ids = np.arange(len(ids) + 1)  # Generate all integers from 0 to len(ids)
    unused_ids = np.setdiff1d(all_possible_ids, unique_ids)  # Find the difference
    return unused_ids[0]  # Return the smallest unused ID
