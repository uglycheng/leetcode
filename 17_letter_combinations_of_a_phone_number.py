class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_dict = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        if digits == "":
            return []
        letter_combinations = [""]
        for digit in digits:
            letter_combinations = [predix + new_digit for predix in letter_combinations for new_digit in map_dict[digit]]
        return letter_combinations