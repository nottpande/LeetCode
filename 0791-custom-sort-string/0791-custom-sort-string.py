class Solution:

    def customSortString(self, order: str, s: str) -> str:
        char_count = {char: 0 for char in order} 
        #the count of all the characters present in order.
        #initially the count is set to 0

        #Now we will check, how many characters present in order are present in s
        for char in s:
            if char in char_count:
                char_count[char] += 1

        #now we will create a sorted array of s, that will contain the alphabets as present in order
        sorted_s = ""
        for char in order:
            sorted_s += char * char_count[char]   #take the character, and add it how many times it is present in s.
        
        #Now add all the alphabets that are not in order, but are present in s
        for char in s:
            if char not in order:
                sorted_s += char

        return sorted_s

