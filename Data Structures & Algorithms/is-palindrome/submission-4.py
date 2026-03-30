class Solution:
    def isPalindrome(self, s: str) -> bool:
        dirty_string = s.replace(" ","").lower()
        print(f" s = {dirty_string}, len = {len(dirty_string)}")

        
        #  string = ''.join(filter(c.isalpha, dirty_string))
        
        if not dirty_string.isalnum():
            string = ""   
            for c in dirty_string:
                if c.isalnum():
                    string += c
        else:
            string = dirty_string
                  

        i = 0
        j = len(string)-1

        while i <= len(string) and j >= 0:
            print (string[i], string[j])
            if string[i] != string[j]:

                return False
            i += 1
            j -= 1



        return True