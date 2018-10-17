from collections import Counter
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r_len, c_len = len(board), len(board[0])
        letter_table = {}
        letter_list = []

        for r_id, row in enumerate(board):
            for c_id, letter in enumerate(row):
                letter_table[letter] = letter_table.get(letter, []) + [[r_id, c_id]]
                letter_list += [letter]
        letter_list = list(set(letter_list))
        c = Counter(word)

        # simple check possible or not
        for w in list(set(word)):
            if w not in letter_list:
                return False
            if len(letter_table.get(w, [])) < c[w]:
                return False

        # recursive check each letter
        def near_search(letters, letter_pos, order_list=[]):
            if len(letters) == 0:
                return True
            near_letters = []
            r_id, c_id = letter_pos
            if r_id > 0:
                n_l = board[r_id-1][c_id]
                n_pos = [r_id-1, c_id]
                near_letters += [[n_l, n_pos]]

            if r_id+1 < r_len:
                n_l = board[r_id+1][c_id]
                n_pos = [r_id+1, c_id]
                near_letters += [[n_l, n_pos]]

            if c_id > 0:
                n_l = board[r_id][c_id-1]
                n_pos = [r_id, c_id-1]
                near_letters += [[n_l, n_pos]]

            if c_id+1 < c_len:
                n_l = board[r_id][c_id+1]
                n_pos = [r_id, c_id+1]
                near_letters += [[n_l, n_pos]]

            for n_letter, letter_pos in near_letters:
                if n_letter == letters[0] and letter_pos not in order_list:
                    next_list = order_list + [letter_pos]
                    if near_search(letters[1:], letter_pos, next_list):
                        return True
            return False

        # start search, find the initial pos
        start_word = word[0]
        for letter_pos in letter_table[start_word]:
            if near_search(word[1:], letter_pos):
                return True
        return False