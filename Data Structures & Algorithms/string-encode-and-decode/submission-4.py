class Solution:

    def encode(self, strs: List[str]) -> str:
        for i,w in enumerate(strs):
            strs[i] = f"{len(w)}#{w}"
        
        print(f"encdd strng = {''.join(strs)}")
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        result = []
        pointer = 0

        while pointer < len(s):
            anchor = pointer
            print(f"pntr: {pointer}")

            while s[anchor] != "#":
                anchor += 1
                print(f"anchor: {anchor}")
            
            size = int(s[pointer:anchor])
            print(f"size: {size}")

            word = s[anchor+1:anchor+1+size]
            result.append(word)

            pointer = anchor + 1 + size
            print(f"new pntr: {pointer}")

            


        print(f"{result}")
        return result
