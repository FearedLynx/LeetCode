def length_of_longest_substring(s: str) -> int:
    # expects a string in, and int out
    last_seen = {}
    start = 0
    longest = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            # we also check if it happened outside the 
            # window using last_seen[ch] >= start
            start = last_seen[ch] + 1
            # if the character is a repeat inside the window
            # we shrink the window by moving START
        last_seen[ch] = i
        # we update the index of the character
        # "this character was last seen at this position"
        longest = max(longest, i - start + 1)
        # i - start + 1 is the length of the current window
        # we compare it and keep the larger one

    return longest

print(length_of_longest_substring("abcabcbb"))