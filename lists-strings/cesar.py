# -*- coding: utf-8 -*-

class CesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plainText):
        j = 0
        encoded_text = ""
        for i in plainText:
            if self._alphabet.find(plainText[j]) == -1:
                encoded_text += plainText[j]
            else:
                if self._alphabet.find(plainText[j])+self._shift > len(self._alphabet)-1:
                    encoded_text += self._alphabet[(self._alphabet.find(plainText[j])+self._shift) - (len(self._alphabet))]
                else:
                    encoded_text += self._alphabet[self._alphabet.find(plainText[j])+self._shift]
            j += 1
        return encoded_text


cesar = CesarCipher()

cesar.set_alphabet("abcdefghijklmnopqrstuvwxyz")
cesar.set_shift(3)

print cesar.encode("The quick brown fox jumps over the lazy dog")

# - Алфавит: “abcdefghijklmnopqrstuvwxyz”. 
# - Сдвиг: 3. 
# - Исходный текст: “The quick brown fox jumps over the lazy dog”, 
# - Зашифрованный текст: “Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj”.