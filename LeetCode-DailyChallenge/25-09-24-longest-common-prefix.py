def longestCommonPrefix(arr1, arr2):
    """
    Find the longest common prefix length between two sorted arrays of strings.

    Parameters:
    arr1 (List[str]): The first sorted array of strings.
    arr2 (List[str]): The second sorted array of strings.

    Returns:
    int: The length of the longest common prefix between arr1 and arr2.
    """
    max_prefix_len = 0

    arr1_str = sorted(map(str, arr1))
    arr2_str = sorted(map(str, arr2))

    i, j = 0, 0
    while i < len(arr1_str) and j < len(arr2_str):
        a_str, b_str = arr1_str[i], arr2_str[j]
        min_len = min(len(a_str), len(b_str))
        prefix_len = 0

        for k in range(min_len):
            if a_str[k] != b_str[k]:
                break
            prefix_len += 1

        max_prefix_len = max(max_prefix_len, prefix_len)

        if a_str < b_str:
            i += 1
        else:
            j += 1

    return max_prefix_len
