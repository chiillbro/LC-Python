class Solution:
    def generateTag(self, caption: str) -> str:
        # caption: string
        res = []
        res.append("#")
        prev = 0

        caption = caption.strip()

        for i, char in enumerate(caption):
            if char == " " and i != 0:
                prev = 1
                continue
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                if prev:
                    res.append(char.capitalize())
                    prev = 0
                else:
                    res.append(char.lower())

        return ''.join(res[:min(100, len(res))])