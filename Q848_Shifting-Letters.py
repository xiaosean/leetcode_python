class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        n = len(S)
        shift_n = len(shifts)
        asc_s = [ord(letter) for letter in S]
        zero_begin_asc_s = [asc_-97 for asc_ in asc_s]
        zero_begin_asc_s = zero_begin_asc_s[:shift_n]
        reverse_shift_asc_s = zero_begin_asc_s[::-1]
        accm = 0
        for i, shift in enumerate(shifts[::-1]):
            accm = (accm+shift) % 26
            reverse_shift_asc_s[i] = (reverse_shift_asc_s[i] + accm) % 26 
        reverse_shift_asc_s = reverse_shift_asc_s[::-1]
        after_asc = [chr(asc_+97) for asc_ in reverse_shift_asc_s]
        after_length = len(after_asc)
        if after_length < n:
            after_asc += S[after_length+1:]
        return "".join(after_asc)