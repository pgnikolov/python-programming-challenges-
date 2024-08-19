def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Find the minimum length string from the list
    min_length = min(len(s) for s in strs)
    common_prefix = ""

    for i in range(min_length):
        char = strs[0][i]
        for s in strs:
            if s[i] != char:
                return common_prefix
        common_prefix += char
    return common_prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
