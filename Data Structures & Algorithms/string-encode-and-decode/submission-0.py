class Solution:
    """
    i str list strs
    o str encoded_string which is the list joined together
    c all valid ascii characters
    e empty? single word?
    t O(N)
    s O(N+M)

    delimiter: len(word) + # + word
    dummy_input = ["Hello","World"]
    encoded_string = "5#Hello5#World"
    decode = [Hello, World]
    """
    def encode(self, strs: List[str]) -> str: # type: ignore
        encoded_string = ""

        for s in strs:
            encoded_string += (str(len(s)) + '#' + s)
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            j = i + length

            decoded_string.append(s[i:j])

            i = j
        
        return decoded_string