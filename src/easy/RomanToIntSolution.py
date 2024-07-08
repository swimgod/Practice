class RomanToIntSolution:
    @staticmethod
    def romanToInt(s: str) -> int:
        roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        roman_sum = 0

        for idx, i in enumerate(s):
            next_idx = idx + 1
            prev_idx = idx - 1
            next_idx_exists = 0 <= next_idx < len(s)
            prev_idx_exists = 0 <= prev_idx < len(s)

            if next_idx_exists & prev_idx_exists:
                if roman_int_map[s[next_idx]] > roman_int_map[i]:
                    roman_sum += (roman_int_map[s[next_idx]] - roman_int_map[i])
                elif roman_int_map[s[prev_idx]] >= roman_int_map[i]:
                    roman_sum += roman_int_map[i]
            elif next_idx_exists & (not prev_idx_exists):
                if roman_int_map[s[next_idx]] > roman_int_map[i]:
                    roman_sum += (roman_int_map[s[next_idx]] - roman_int_map[i])
                else:
                    roman_sum += roman_int_map[i]
            else:
                if roman_int_map[s[prev_idx]] >= roman_int_map[i]:
                    roman_sum += roman_int_map[i]

        return roman_sum

    @staticmethod
    def romanToInt2(s: str) -> int:
        roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        roman_sum = 0
        for j in range(len(s)):
            roman_sum += roman_int_map[s[j]]

        for k in range(len(s)):
            next_idx = k + 1
            next_idx_exists = 0 <= next_idx < len(s)

            if next_idx_exists:
                if roman_int_map[s[next_idx]] > roman_int_map[s[k]]:
                    roman_sum -= roman_int_map[s[k]] * 2
        return roman_sum
