class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        have = 0
        need_count = len(need)

        left = 0

        result = [-1, -1]
        min_length = float("inf")

        for right in range(len(s)):

            c = s[right]

            if c in need:
                window[c] = window.get(c, 0) + 1

                if window[c] == need[c]:
                    have += 1

            # Current window contains everything we need
            while have == need_count:

                # record smallest
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = [left, right]

                # remove left character
                c = s[left]

                if c in need:
                    window[c] -= 1

                    if window[c] < need[c]:
                        have -= 1

                left += 1

        left, right = result

        if min_length == float("inf"):
            return ""

        return s[left:right + 1]