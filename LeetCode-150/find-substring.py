def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    concat_len = word_len * num_words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    result = []

    for i in range(word_len):
        left = i
        right = i
        current_window_count = {}

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len

            if word in word_count:
                if word in current_window_count:
                    current_window_count[word] += 1
                else:
                    current_window_count[word] = 1

                while current_window_count[word] > word_count[word]:
                    current_window_count[s[left:left + word_len]] -= 1
                    left += word_len

                if right - left == concat_len:
                    result.append(left)
            else:
                current_window_count.clear()
                left = right

    return result

