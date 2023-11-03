# -*- coding: utf-8 -*-


from korfunc import *


BASE_CODE = 44032
CHOSUNG = 588
JUNGSUNG = 28

KOR_CHOSUNG_LIST = [ 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ' ]
KOR_JUNGSUNG_LIST = [ 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ' ]
KOR_JONGSUNG_LIST = [ '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ' ]
KOR_SPLT_LIST = [ '.', '?', '!', ',', '·', ':', ';', '/', '"', "'", '(', ')', '{', '}', '[', ']', '~', '-', '―', '*', '\\', '$']
ENG_SPLT_LIST = [ ',', ';', ':', '.', '?', '!', "'", '"', '(', ')', '[', ']', '{', '}', '-', '―', '_', '/', '*', '#', '@']
MATHMATICAL_SYMBOL_LIST = [ '+', '<', '>', '%', '^', '÷', '×', '=']

class Letter:
    def __init__(self, argv):
        self.sentence = str()
        self.sentence = argv
        self.i = 0


    def setSentence(self, argv):
        self.sentence = argv


    def decideLanguage(self):
        if self.sentence[self.i] == ' ':
            return 0;
        elif isKorean(self.sentence[self.i]):
            return 100
        elif self.sentence[self.i] in KOR_JONGSUNG_LIST and self.sentence[self.i] not in KOR_CHOSUNG_LIST:
            return 103
        elif self.sentence[self.i] in KOR_CHOSUNG_LIST:
            return 101
        elif self.sentence[self.i] in KOR_JUNGSUNG_LIST:
            return 102
        elif self.sentence[self.i].isalpha():
            return 200
        elif self.sentence[self.i].isnumeric():
            return 300
        elif self.isEngSplt():
            return 402
        elif self.isKorSplt():
            return 401
        else:
            return -1;


    def judgeException(self):
        endcode = 0
        if isKorean(self.sentence[self.i]):
            
            char_code, chosung, jungsung, jongsung, withoutChosung, withoutJongsung = self.kor_disassembleWord()

            if chr(withoutChosung) in ('걱', '건', '걸', '견', '결', '경', '곡', '곤', '공', '군', '굴', '근', '글', '긴'):
                if self.sentence[self.i] in ('셩', '쎵', '졍', '쪙', '쳥'):
                    return 0
                else:
                    return 110
            elif self.sentence[self.i] in ('성', '썽', '정', '쩡', '청'):
                return 110
            
            elif chr(withoutJongsung) in ('가', '까', '사', '싸'):
                return 120
            elif chr(withoutJongsung) in ('나', '다', '따', '마', '바', '빠', '자', '짜', '카', '타', '파', '하'):
                if self.i == len(self.sentence) - 1:
                    return 120
                elif self.i < len(self.sentence) - 1 and isKorean(self.sentence[self.i + 1]):
                    if not(jongsung == 0 and KOR_CHOSUNG_LIST[getChosung(self.sentence[self.i + 1])] == 'ㅇ') and not(self.sentence[self.i] == '팠'):
                        return 120

            elif self.sentence[self.i] in ('것', '껏'):
                return 130

            elif self.sentence[self.i] == '그' and (self.i == 0 or (self.i and self.sentence[self.i - 1] == ' ')):
                if self.wordInSentence("그래서", self.i):
                    self.i += 2
                    return 141
                elif self.wordInSentence("그러나", self.i):
                    self.i += 2
                    return 142
                elif self.wordInSentence("그러면", self.i):
                    self.i += 2
                    return 143 
                elif self.wordInSentence("그러므로", self.i):
                    self.i += 3
                    return 144 
                elif self.wordInSentence("그런데", self.i):
                    self.i += 2
                    return 145 
                elif self.wordInSentence("그리고", self.i):
                    self.i += 2
                    return 146 
                elif self.wordInSentence("그리하여", self.i):
                    self.i += 3
                    return 147 

            elif KOR_JUNGSUNG_LIST[jungsung] in ('ㅓ', 'ㅗ') and KOR_JONGSUNG_LIST[jongsung] in ('ㄲ', 'ㄳ'):
                return 151;
            elif KOR_JUNGSUNG_LIST[jungsung] in ('ㅓ', 'ㅕ', 'ㅗ', 'ㅜ', 'ㅡ', 'ㅣ') and KOR_JONGSUNG_LIST[jongsung] in ('ㄵ', 'ㄶ'):
                return 154;
            elif KOR_JUNGSUNG_LIST[jungsung] in ('ㅓ', 'ㅕ', 'ㅜ', 'ㅡ') and KOR_JONGSUNG_LIST[jongsung] in ('ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ'):
                return 158;

            elif chr(withoutJongsung) == '예':
                if self.i and getJongsung(self.sentence[self.i - 1]) == 0:
                    return 160
            elif chr(withoutJongsung) == '애':
                if self.i and getJongsung(self.sentence[self.i - 1]) == 0 and KOR_JUNGSUNG_LIST[getJunsung(self.sentence[self.i - 1])] in ('ㅑ', 'ㅘ', 'ㅜ', 'ㅝ'):
                    return 160

            else:
                return 0

        elif self.sentence[self.i].isalpha():
            if self.isStartOfRoman() and self.isEndOfRoman():
                endcode += 30
            elif self.isStartOfRoman():
                endcode += 10
            elif self.isEndOfRoman():
                endcode += 20

            if self.isOverThreeVocabUpper():
                endcode += 3
            elif self.isVocabUpper():
                endcode += 2
            elif self.sentence[self.i].isupper():
                endcode += 1

            return endcode
            
        elif self.sentence[self.i].isnumeric():
            if self.isStartOfNumber():
                endcode += 1

            if self.i < len(self.sentence) and (getChosung(self.sentence[self.i]) in ('ㄴ', 'ㄷ', 'ㅁ', 'ㅋ', 'ㅌ', 'ㅍ') or chr(getWithoutChosung(self.sentence[self.i])) == '군'): 
                endcode += 10

            return endcode

        return 0;


    def kor_disassembleWord(self):
        char_code = getCharCode(self.sentence[self.i])
        chosung = getChosung(self.sentence[self.i])
        jungsung = getJunsung(self.sentence[self.i])
        jongsung = getJongsung(self.sentence[self.i])
        withoutChosung = getWithoutChosung(self.sentence[self.i])
        withoutJongsung = getWithoutJongsung(self.sentence[self.i])
        return (char_code, chosung, jungsung, jongsung, withoutChosung, withoutJongsung)


    def wordInSentence(self, vocab, i):
        for j in vocab:
            if i < len(self.sentence) and j == self.sentence[i]:
                i += 1
                continue
            else:
                return False

        return True


    def isStartOfRoman(self):
        if self.i == 0:
            return True

        if self.i == 1 and self.sentence[0].isalpha():
            return False
        
        for j in range(self.i - 1, -1, -1):
            if self.sentence[j] == ' ' or self.sentence[j] in ENG_SPLT_LIST:
                continue
            elif self.sentence[j].isalpha():
                return False
            else:
                return True

        return True


    def isEndOfRoman(self):
        if self.i == len(self.sentence) - 1:
            return True

        for j in range(self.i + 1, len(self.sentence)):
            if self.sentence[j] == ' ' or self.sentence[j] in ENG_SPLT_LIST:
                continue
            elif self.sentence[j].isalpha() or self.sentence[j].isnumeric() or self.sentence[j] in ('.'):
                return False
            else:
                return True

        return True

    def isEndOfRoman2(self):
        if self.i == len(self.sentence) - 1:
            return True

        for j in range(self.i + 1, len(self.sentence)):
            if self.sentence[j] == ' ' or self.sentence[j] in ENG_SPLT_LIST:
                continue
            elif self.sentence[j].isalpha():
                return False
            else:
                return True

        return True


    def isVocabUpper(self):
        if not (self.isStartOfRoman() or (self.i and (self.sentence[self.i - 1] == ' ' or self.sentence[self.i - 1] in ENG_SPLT_LIST))):
            return False

        if self.isEndOfRoman2():
            return False

        if self.sentence[self.i].islower():
            return False

        for j in range(self.i, len(self.sentence)):
            if self.sentence[j].isalpha():
                if self.sentence[j].isupper():
                    continue
                elif self.sentence[j].islower():
                    return False
            else:
                break

        for j in range(self.i + 1, len(self.sentence)):
            if self.sentence[j].isupper():
                self.sentence = self.sentence[:j] + self.sentence[j].lower() + self.sentence[j+1:]
            else:
                break
            
        return True


    def isOverThreeVocabUpper(self):
        countSpace = 0

        if not self.isStartOfRoman():
            return False

        if self.isEndOfRoman2():
            return False

        if self.sentence[self.i].islower():
            return False

        Space = True
        for j in range(self.i, len(self.sentence)):
            if self.sentence[j] == ' ' or self.sentence[j] in ENG_SPLT_LIST:
                if Space:
                    countSpace += 1
                    Space = False
                    print(countSpace)
                continue
            elif self.sentence[j].isalpha():
                Space = True
                if self.sentence[j].isupper():
                    continue
                elif self.sentence[j].islower():
                    return False
            else:
                break

        if countSpace < 2:
            return False

        for j in range(self.i + 1, len(self.sentence)):
            if self.sentence[j] == ' ' or self.sentence[j] in ENG_SPLT_LIST:
                continue
            if self.sentence[j].isupper():
                self.sentence = self.sentence[:j] + self.sentence[j].lower() + self.sentence[j+1:]
            else:
                break

        return True


    def isStartOfNumber(self):
        if self.i == 0:
            return True

        if self.i == 1 and self.sentence[0].isnumeric():
            return False
        
        for j in range(self.i - 1, -1, -1):
            if self.sentence[j] == ' ':
                continue
            elif self.sentence[j].isnumeric() or self.sentence[j] in ('-', '.', '·', ':'):
                return False
            else:
                return True

        return True


    def isKorSplt(self):
        prevKor, nextKor = False, False

        if self.i == 0:
            prevKor = True

        if self.i == len(self.sentence) - 1:
            nextKor = True

        for j in range(self.i - 1, -1, -1):
            if self.sentence[j] == ' ':
                continue
            elif isKor(self.sentence[j]):
                prevKor = True
                break
            else:
                prevKor = False
                break

        for j in range(self.i + 1, len(self.sentence)):
            if self.sentence[j] == ' ':
                continue
            elif isKor(self.sentence[j]):
                nextKor = True
                break
            else:
                nextKor = False
                break

        if (prevKor, nextKor) == (False, False):
            return False 
        else:
            return True


    def isEngSplt(self):
        prevEng, nextEng = False, False

        if self.i == 0:
            prevEng = True

        if self.i == len(self.sentence) - 1:
            nextEng = True

        for j in range(self.i - 1, -1, -1):
            if self.sentence[j] == ' ' or self.sentence[j] in ENG_SPLT_LIST:
                continue
            elif self.sentence[j].isalpha():
                prevEng = True
                break
            else:
                prevEng = False
                break

        for j in range(self.i + 1, len(self.sentence)):
            if self.sentence[j] == ' ':
                continue
            elif self.sentence[j].isalpha():
                nextEng = True
                break
            else:
                nextEng = False
                break

        if (prevEng, nextEng) in ((True, False), (False, False), (False, True)):
            return False
        else:
            return True

    def splt_closingQuotes():
        pass

    def splt_apostrophe():
        pass