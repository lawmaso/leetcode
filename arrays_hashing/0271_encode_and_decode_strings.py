"""
Design an algorithm to encode a list of strings
to a string. The encoded string is then sent
over the network and is decoded back to the
original list of strings.

Machine 1 (sender) has the function:
String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}

Machine 2 (receiver) has the function:
List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}

So Machine 1 does:
String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.
"""


class Solution:
    d: str  # delimiter

    def __init__(self, d: str = "%"):
        self.d = d

    def encode(self, strs: list[str]) -> str:
        encoding = ""

        for s in strs:
            encoding += str(len(s)) + self.d + s

        return encoding
    
    def decode(self, s: str) -> list[str]:
        decoding = []
        n = len(s)  # total chars of encoding

        i = 0
        while i < n:
            # find the length portion
            j = i
            while s[j] != self.d:
                j += 1

            # now s[i:j] = length (str)
            length = int(s[i:j])
            
            # position i and j to extract content
            i = j + 1       # i = after delimiter
            j = i + length  # j = length chars after delimiter

            # now s[i:j] is the content (str)
            # len(s[i:j]) = (i + length) - i = length (chars)
            decoding.append(s[i:j])

            i = j

        return decoding

"""
to encode, we'll need a deterministic way to structure it
for decoding

we'd need state on: length, content, and some way to separate encodings

[delimit][length][content]
%4word

doesn't work since word can contain digits, so the length gets lost

[length][delimit][content]
4%word

once delimit is reached, we have the length; this is deterministic and should work

encoding will just be the sum of [len(s)][delimit][content]

then decoding will just build out the strings from this string
"""

