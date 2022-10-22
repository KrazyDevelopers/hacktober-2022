class GC:

    def __init__(self) -> None:
        self.encode_lower = {'g': 'a', 'a': 'g', 'd': 'e', 'e': 'd', 'r': 'y', 'y': 'r', 'p': 'o',
                             'o': 'p', 'l': 'u', 'u': 'l', 'k': 'i', 'i': 'k'}
        self.encode_upper = {'G': 'A', 'A': 'G', 'D': 'E', 'E': 'D', 'R': 'Y', 'Y': 'R', 'P': 'O',
                             'O': 'P', 'L': 'U', 'U': 'L', 'K': 'I', 'I': 'K'}

    def code(self, text):
        encode_text = ''
        for char in text:
            if char.isupper():
                char = self.encode_upper.get(char, char)
                encode_text += char
            elif char.islower():
                char = self.encode_lower.get(char, char)
                encode_text += char
            else:
                encode_text += char
        return encode_text

    def encode(self, text):
        return self.code(text)

    def decode(self, text):
        return self.code(text)


x = GC()
print(x.encode('KrazyDevelopers/hacktober'))
print(x.decode('IygzrEdvdupodys/hgcitpbdy'))
