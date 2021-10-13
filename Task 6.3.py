import string

class Cipher:

    def __init__(self, keyword):
        self.base = list(string.ascii_uppercase)
        self.mask = []
        self.d_direct = {}
        self.d_return = {}
        self.kwd = list(keyword.upper())
        for i in range(len(self.base)):
            if self.base[i] not in self.kwd:
                self.kwd.append(self.base[i])
        for i in range(len(self.base)):
            self.d_direct[self.base[i]] = self.kwd[i]
            self.d_return[self.kwd[i]] = self.base[i]

    def encode(self, sentence):
        for i in sentence:
            if (i == i.upper()) and (i.isalpha()):
                self.mask.append(1)
            else:
                self.mask.append(0)
        self.sntc = sentence.upper()
        self.tmp = []
        self.count = 0
        for i in self.sntc:
            if i in self.d_direct.keys():
                if self.mask[self.count] != 1:
                    self.tmp.append(self.d_direct[i].lower())
                else:
                    self.tmp.append(self.d_direct[i])
            else:
                self.tmp.append(i)
            self.count += 1
        self.mask.clear()
        return ''.join(self.tmp)

    def decode(self, sentence):
        for i in sentence:
            if (i == i.upper()) and (i.isalpha()):
                self.mask.append(1)
            else:
                self.mask.append(0)
        self.sntc = sentence.upper()
        self.tmp = []
        self.count = 0
        for i in self.sntc:
            if i in self.d_return.keys():
                if self.mask[self.count] != 1:
                    self.tmp.append(self.d_return[i].lower())
                else:
                    self.tmp.append(self.d_return[i])
            else:
                self.tmp.append(i)
            self.count += 1
        self.mask.clear()
        return ''.join(self.tmp)


cipher = Cipher("crypto")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))