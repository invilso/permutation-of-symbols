import random
import re


class Permuter:
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
        symbs = [',', '!', '.', "?", '\n']
        out = []
        for key, symb in enumerate(string):
            if symb in symbs:
                out.append({'symb': symb, 'key':key})
        return out

    def permuteString(self, string: str) -> str:
        out = ''
        saved = self.saveSybols(string)
        for word in self.getWords(string):
            out = out + self.permuteWord(word) + ' '
        out = list(out)
        for i, s in enumerate(saved, 0):
            out.insert(s['key']+i, s['symb']) #I add "i" every time because the length of the string changes.
        out2 = ''
        for s in out:
            out2 = out2 + s
        out2 = re.sub('  ', ' ', out2) #fix dubble spaces
        out2 = re.sub('\n ', '\n', out2) #fix \n + space
        return out2

s = '''Воторй пнукт не свсеом пянол.

Рвзае за квноямои не сядeлт?
P.S. Вы заелмити что эотт тсeкт вы сгомли без побрелм пчортиать? Нжнуо вегсо чобты првеая и плодесняя бквуы блыи на соивх мстеах.'''
p = Permuter()
print(p.permuteString(s))