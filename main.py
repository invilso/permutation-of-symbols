import random
import re


class Permuter:
    def getLines(self, string) -> list:
        return re.split('\n', string)

    def getWords(self, string) -> list:
        return re.split(r'[\s|,!\.?]', string)

    def permuteWord(self, word) -> str:
        if len(word) > 3:
            out = word[:1]
            middle = list(word[1:(len(word)-1)])
            for symbol in random.sample(middle, len(middle)):
                out = out + symbol
            return out + word[-1:]
        else:
            return word

    def saveSybols(self, string) -> list:
        symbs = [',', '!', '.', "?"]
        out = []
        for key, symb in enumerate(string):
            if symb in symbs:
                out.append({'symb': symb, 'key':key})
        return out

    def permuteString(self, string: str) -> str:
        out = ''
        saved = self.saveSybols(string)
        lines = self.getLines(string)
        for key, line in enumerate(lines):
            for word in self.getWords(line):
                out = out + self.permuteWord(word) + ' '
            if key != len(lines):
                out = out + '\n'
        out = list(out)
        for i, s in enumerate(saved, 0):
            out.insert(s['key']+i, s['symb']) #I add "i" every time because the length of the string changes.
        out2 = ''
        for s in out:
            out2 = out2 + s
        out2 = re.sub('  ', ' ', out2) #fix dubble spaces
        return out2

s = '''Hi. Have you noticed that you are calmly reading such a text without straining at all?'''
p = Permuter()
print(p.permuteString(s))