def letterCombinations(digits):
    ans = []
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
    def backTrack(i, str):
        if len(str) == len(digits):
            ans.append(str)
            return

        for char in letters[digits[i]]:
            backTrack(i+1,str + char)
    
    if not digits:
        return []

    backTrack(0,'')
    return ans
