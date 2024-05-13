class PalindromeSolution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        reverse_string = ""
        int_string = str(x)

        last_idx = len(int_string) - 1
        for i in range(len(int_string)):
            reverse_string += int_string[last_idx - i]

        return int_string == reverse_string
