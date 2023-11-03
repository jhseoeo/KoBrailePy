# -*- coding: utf-8 -*-


# 0, 0 >>>> 쉼표(쌍점)
# 000,000 >>>> 자릿수 구분 쉼표 


from letter import *
from korfunc import *
    

class Braille:
    def __init__(self):
        self.brailleList = [[], [], []]


    def clear(self):
        self.brailleList = [[], [], []]


    def makeSpace(self):
        self.brailleList[0] += ['s']
        self.brailleList[1] += ['s']
        self.brailleList[2] += ['s']


    def export(self):
        return self.brailleList


    def process(self, word, languageCode, exceptionCode, sentence, i):

        print("{} / {} : {} | {}-{}".format(i, len(sentence), word, languageCode, exceptionCode))

        if languageCode == 0:
            self.makeSpace()

        elif languageCode == 100:
            if exceptionCode == 0:
                self.kor_chosung(KOR_CHOSUNG_LIST[getChosung(word)])
                self.kor_jungsung(KOR_JUNGSUNG_LIST[getJunsung(word)])
                if KOR_JONGSUNG_LIST[getJongsung(word)] != 0:
                    self.kor_jongsung(KOR_JONGSUNG_LIST[getJongsung(word)])

            elif exceptionCode == 110:
                self.kor_chosung(KOR_CHOSUNG_LIST[getChosung(word)])
                self.kor_exception1(chr(getWithoutChosung(word)))

            elif exceptionCode == 120:
                self.kor_exception2(chr(getWithoutJongsung(word)))
                if KOR_JONGSUNG_LIST[getJongsung(word)] != ' ':
                    self.kor_jongsung(KOR_JONGSUNG_LIST[getJongsung(word)])

            elif exceptionCode == 130:
                self.kor_exception3(word)

            elif exceptionCode == 141:
                self.kor_exception4('서')
            elif exceptionCode == 142:
                self.kor_exception4('나')
            elif exceptionCode == 143:
                self.kor_exception4('면')
            elif exceptionCode == 144:
                self.kor_exception4('로')
            elif exceptionCode == 145:
                self.kor_exception4('데')
            elif exceptionCode == 146:
                self.kor_exception4('고')
            elif exceptionCode == 147:
                self.kor_exception4('여')

            elif exceptionCode == 151:
                self.kor_chosung(KOR_CHOSUNG_LIST[getChosung(word)])
                self.kor_exception1(chr(getJunsung(word)*JUNGSUNG + 1 + BASE_CODE))
                self.kor_exception5(KOR_JONGSUNG_LIST[getJongsung(word)])
            elif exceptionCode == 154:
                self.kor_chosung(KOR_CHOSUNG_LIST[getChosung(word)])
                self.kor_exception1(chr(getJunsung(word)*JUNGSUNG + 4 + BASE_CODE))
                self.kor_exception5(KOR_JONGSUNG_LIST[getJongsung(word)])
            elif exceptionCode == 158:
                self.kor_chosung(KOR_CHOSUNG_LIST[getChosung(word)])
                self.kor_exception1(chr(getJunsung(word)*JUNGSUNG + 8 + BASE_CODE))
                self.kor_exception5(KOR_JONGSUNG_LIST[getJongsung(word)])

            elif exceptionCode == 160:
                self.kor_exception6()
                self.kor_chosung(KOR_CHOSUNG_LIST[getChosung(word)])
                self.kor_jungsung(KOR_JUNGSUNG_LIST[getJunsung(word)])
                if KOR_JONGSUNG_LIST[getJongsung(word)] != 0:
                    self.kor_jongsung(KOR_JONGSUNG_LIST[getJongsung(word)])
            
            else:
                print("오류났나")

        elif languageCode == 101:
            self.kor_chosung(word, True)
        elif languageCode == 102:
            self.kor_jungsung(word, True)
        elif languageCode == 103:
            self.kor_jongsung(word, False)

        elif languageCode == 200:

            if (exceptionCode // 10) in (1, 3):
                self.eng_sp('s')
            if exceptionCode % 10 == 1:
                self.eng_sp('u')
            elif exceptionCode % 10 == 2:
                self.eng_sp('U')
            elif exceptionCode % 10 == 3:
                self.eng_sp('UU')

            self.eng_alphabet(word)

            if (exceptionCode // 10) in (2, 3):
                self.eng_sp('e')

        elif languageCode == 300:
            if exceptionCode % 10:
                self.num(word, True)
            else:
                self.num(word)

            if exceptionCode // 10:
                self.makeSpace()

        elif languageCode == 401:
            self.splt_kor(word)

        #elif languageCode == -1:
           

    def kor_chosung(self, word, only = False):
        if only:
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]

        if word == 'ㄱ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㄲ':
            self.brailleList[0] += [False, False, False, True]
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, True, False, False]
        elif word == 'ㄴ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㄷ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㄸ':
            self.brailleList[0] += [False, False, False, True] 
            self.brailleList[1] += [False, False, True, False]
            self.brailleList[2] += [False, True, False, False]
        elif word == 'ㄹ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == 'ㅁ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]    
        elif word == 'ㅂ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == 'ㅃ':
            self.brailleList[0] += [False, False, False, True]
            self.brailleList[1] += [False, False, False, True]
            self.brailleList[2] += [False, True, False, False]
        elif word == 'ㅅ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㅆ':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, True, False, True]
        elif word == 'ㅇ':
            if only == True:
                self.brailleList[0] += [True, True]
                self.brailleList[1] += [True, True]
                self.brailleList[2] += [False, False]
        elif word == 'ㅈ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]    
        elif word == 'ㅉ':
            self.brailleList[0] += [False, False, False, True] 
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, True, False, True]
        elif word == 'ㅊ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, True]
        elif word == 'ㅋ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㅌ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == 'ㅍ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == 'ㅎ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]


    def kor_jungsung(self, word, only = False):
        if only:
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]
        
        if word == 'ㅏ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㅑ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, False]
        elif word == 'ㅓ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]  
        elif word == 'ㅕ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, True]
        elif word == 'ㅗ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, True]
        elif word == 'ㅛ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, True]    
        elif word == 'ㅜ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㅠ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㅡ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㅣ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, False]
        elif word == 'ㅐ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == 'ㅒ':
            self.brailleList[0] += [False, True, True, False]
            self.brailleList[1] += [False, True, True, True] 
            self.brailleList[2] += [True, False, True, False]
        elif word == 'ㅔ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, False]  
        elif word == 'ㅖ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㅘ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]   
        elif word == 'ㅙ':
            self.brailleList[0] += [True, False, True, False] 
            self.brailleList[1] += [True, False, True, True] 
            self.brailleList[2] += [True, True, True, False]
        elif word == 'ㅚ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]
        elif word == 'ㅝ':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㅞ':
            self.brailleList[0] += [True, True, True, False] 
            self.brailleList[1] += [True, False, True, False]
            self.brailleList[2] += [True, False, True, False]
        elif word == 'ㅟ':
            self.brailleList[0] += [True, True, True, False] 
            self.brailleList[1] += [False, False, True, True]
            self.brailleList[2] += [True, False, True, False]
        elif word == 'ㅢ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]


    def kor_jongsung(self, word, only = False):
        if only:
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]
        if word == 'ㄱ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㄴ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == 'ㄷ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, False]
        elif word == 'ㄹ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㅁ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㅂ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㅅ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㅇ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]  
        elif word == 'ㅈ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㅊ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㅋ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == 'ㅌ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]
        elif word == 'ㅍ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]
        elif word == 'ㅎ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True] 
        elif word == 'ㅆ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㄲ':
            self.brailleList[0] += [True, False, True, False]
            self.brailleList[1] += [False, False, False, False] 
            self.brailleList[2] += [False, False, False, False] 
        elif word == 'ㄳ':
            self.brailleList[0] += [True, False, False, False] 
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, False, True, False]  
        elif word == 'ㄵ':
            self.brailleList[0] += [False, False, True, False]
            self.brailleList[1] += [True, True, False, False] 
            self.brailleList[2] += [False, False, True, False]
        elif word == 'ㄶ':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [True, True, False, True] 
            self.brailleList[2] += [False, False, True, True]
        elif word == 'ㄺ':
            self.brailleList[0] += [False, False, True, False] 
            self.brailleList[1] += [True, False, False, False] 
            self.brailleList[2] += [False, False, False, False] 
        elif word == 'ㄻ':
            self.brailleList[0] += [False, False, True, False]
            self.brailleList[1] += [True, False, True, False]
            self.brailleList[2] += [False, False, False, False]
        elif word == 'ㄼ':
            self.brailleList[0] += [False, False, True, False]
            self.brailleList[1] += [True, False, True, False] 
            self.brailleList[2] += [False, False, False, False] 
        elif word == 'ㄽ':
            self.brailleList[0] += [False, False, False, False] 
            self.brailleList[1] += [True, False, False, False] 
            self.brailleList[2] += [False, False, True, False] 
        elif word == 'ㄾ':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [True, False, True, False]
            self.brailleList[2] += [False, False, True, False]
        elif word == 'ㄿ':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [True, False, True, True] 
            self.brailleList[2] += [False, False, False, True]
        elif word == 'ㅀ':
            self.brailleList[0] += [False, False, False, False] 
            self.brailleList[1] += [True, False, False, True]
            self.brailleList[2] += [False, False, True, True]
        elif word == 'ㅄ':
            self.brailleList[0] += [True, False, False, False]
            self.brailleList[1] += [True, False, False, False]
            self.brailleList[2] += [False, False, True, False]
        
    def kor_exception1(self, word):
        if word == '걱':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, True]
        elif word == '건':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]
        elif word == '걸':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == '견':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]
        elif word == '결':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]
        elif word in ('경', '겅'):
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]
        elif word == '곡':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, True]
        elif word == '곤':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]
        elif word == '공':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, True]
        elif word == '군':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == '굴':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]
        elif word == '근':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]
        elif word == '글':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]
        elif word == '긴':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]


    def kor_exception2(self, word):
        if word == '가':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, True]
        elif word == '까':
            self.brailleList[0] += [False, False, True, True] 
            self.brailleList[1] += [False, False, True, False]
            self.brailleList[2] += [False, True, False, True] 
        elif word == '나':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == '다':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == '따':
            self.brailleList[0] += [False, False, False, True]
            self.brailleList[1] += [False, False, True, False]
            self.brailleList[2] += [False, True, False, False]
        elif word == '마':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == '바':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == '빠':
            self.brailleList[0] += [False, False, False, True] 
            self.brailleList[1] += [False, False, False, True] 
            self.brailleList[2] += [False, True, False, False] 
        elif word == '사':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]
        elif word == '싸':
            self.brailleList[0] += [False, False, True, False] 
            self.brailleList[1] += [False, False, True, False] 
            self.brailleList[2] += [False, True, True, False] 
        elif word == '자':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]
        elif word == '짜':
            self.brailleList[0] += [False, False, False, True] 
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, True, False, True]
        elif word == '카':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == '타':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == '파':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == '하':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]

        
    def kor_exception3(self, word):
        if word == '것':
            self.brailleList[0] += [False, True, False, True] 
            self.brailleList[1] += [False, True, True, False] 
            self.brailleList[2] += [False, True, True, False] 
        elif word == '껏':
            self.brailleList[0] += [False, False, False, True, False, True]
            self.brailleList[1] += [False, False, False, True, True, False]
            self.brailleList[2] += [False, True, False, True, True, False] 
        

    def kor_exception4(self, lastword):
        if lastword == '서':
            self.brailleList[0] += [True, False, False, True]
            self.brailleList[1] += [False, False, True, False]
            self.brailleList[2] += [False, False, True, False]
        elif lastword == '나':
            self.brailleList[0] += [True, False, True, True] 
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, False, False, False]
        elif lastword == '면':
            self.brailleList[0] += [True, False, False, False] 
            self.brailleList[1] += [False, False, True, True] 
            self.brailleList[2] += [False, False, False, False] 
        elif lastword == '로':
            self.brailleList[0] += [True, False, False, False] 
            self.brailleList[1] += [False, False, True, False] 
            self.brailleList[2] += [False, False, False, True]       
        elif lastword == '데':
            self.brailleList[0] += [True, False, False, True] 
            self.brailleList[1] += [False, False, True, False]
            self.brailleList[2] += [False, False, True, False]
        elif lastword == '고':
            self.brailleList[0] += [True, False, True, True] 
            self.brailleList[1] += [False, False, False, True]
            self.brailleList[2] += [False, False, True, False]
        elif lastword == '여':
            self.brailleList[0] += [True, False, True, False]
            self.brailleList[1] += [False, False, False, True]
            self.brailleList[2] += [False, False, False, True]


    def kor_exception5(self, word):
        if word == 'ㄲ' or word == 'ㄺ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㄳ' or word == 'ㄽ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'ㄵ':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㄶ' or word == 'ㅀ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]
        elif word == 'ㄻ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, True]
        elif word == 'ㄼ':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'ㄾ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]
        elif word == 'ㄿ':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]


    def kor_exception6(self):
        self.brailleList[0] += [False, False]
        self.brailleList[1] += [False, False]
        self.brailleList[2] += [True, True]
    

    def eng_alphabet(self, word):
        if word == 'a' or word == 'A':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == 'b' or word == 'B':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'c' or word == 'C':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == 'd' or word == 'D':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == 'e' or word == 'E':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == 'f' or word == 'F':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'g' or word == 'G':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == 'h' or word == 'H':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == 'i' or word == 'I':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == 'j' or word == 'J':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == 'k' or word == 'K':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'l' or word == 'L':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]
        elif word == 'm' or word == 'M':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, False]
        elif word == 'n' or word == 'N':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, False]
        elif word == 'o' or word == 'O':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, False]
        elif word == 'p' or word == 'P':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]
        elif word == 'q' or word == 'Q':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == 'r' or word == 'R':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == 's' or word == 'S':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, False]
        elif word == 't' or word == 'T':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == 'u' or word == 'U':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, True]
        elif word == 'v' or word == 'V':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]
        elif word == 'w' or word == 'W':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]
        elif word == 'x' or word == 'X':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, True]
        elif word == 'y' or word == 'Y':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]
        elif word == 'z' or word == 'Z':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]


    def eng_sp(self, word):
        if word == 'u':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, True]
        elif word == 'U':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, True, False, True]
        elif word == 'UU':
            self.brailleList[0] += [False, False, False, False, False, False]
            self.brailleList[1] += [False, False, False, False, False, False]
            self.brailleList[2] += [False, True, False, True, False, True]
        elif word == 's':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]
        elif word == 'e':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]
        
    

    def num(self, word, first = False):
        if first:
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [True, True]
    
        if word == '0':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == '1':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == '2':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == '3':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [False, False]
        elif word == '4':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == '5':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == '6':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == '7':
            self.brailleList[0] += [True, True]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == '8':
            self.brailleList[0] += [True, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, False]
        elif word == '9':
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]
        elif word == ',':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [False, False]

    def splt_kor(self, word, closingQuotes = False, apostrophe = False):
        if emphasize:
            self.brailleList[0] += [False, True]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, True]
        if word == '.':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [False, True]
        elif word == '?':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, False]
            self.brailleList[2] += [True, True]
        elif word == '!':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [True, True]
            self.brailleList[2] += [True, False]
        elif word == ',':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, True]
            self.brailleList[2] += [False, False]
        elif word == '·':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, True, True, False]
            self.brailleList[2] += [False, False, True, False]
        elif word == ':':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, True, True, False]
            self.brailleList[2] += [False, False, False ,False]
        elif word == ';':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, True, True, False]
            self.brailleList[2] += [False, True, True, False]
        elif word == '/':
            self.brailleList[0] += [False, True, False, True]
            self.brailleList[1] += [False, True, False, False]
            self.brailleList[2] += [False, True, True, False]
        elif word == '"':
            if closingQuotes:
                self.brailleList[0] += [False, False]
                self.brailleList[1] += [False, True]
                self.brailleList[2] += [True, True]
            else:
                self.brailleList[0] += [False, False]
                self.brailleList[1] += [True, False]
                self.brailleList[2] += [True, True]
        elif word == "'":
            if apostrophe:
                self.brailleList[0] += [False, False]
                self.brailleList[1] += [False, False]
                self.brailleList[2] += [True, False]
            elif closingQuotes:
                self.brailleList[0] += [False, False, False, False]
                self.brailleList[1] += [False, True, False, False]
                self.brailleList[2] += [True, True, True, False]
            else:
                self.brailleList[0] += [False, False, False, False]
                self.brailleList[1] += [False, False, True, False]
                self.brailleList[2] += [False, True, True, True]
        elif word == '(':
            self.brailleList[0] += [False, False, False, True]
            self.brailleList[1] += [True, False, False, False]
            self.brailleList[2] += [True, True, True, False]
        elif word == ')':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, False, False, True]
            self.brailleList[2] += [False, True, True, True]
        elif word == '{':
            self.brailleList[0] += [False, False, False, True]
            self.brailleList[1] += [True, False, True, False]
            self.brailleList[2] += [True, True, False, False]
        elif word == '}':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, True, False, True]
            self.brailleList[2] += [False, False, True, True]
        elif word == '[':
            self.brailleList[0] += [False, False, False, True]
            self.brailleList[1] += [True, False, True, False]
            self.brailleList[2] += [True, True, True, False]
        elif word == ']':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, True, False, True]
            self.brailleList[2] += [False, True, True, True]
        elif word == '~':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [True, True, True, True]
        elif word == '-':
            self.brailleList[0] += [False, False]
            self.brailleList[1] += [False, False]
            self.brailleList[2] += [True, True]
        elif word == '―':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [True, True, True, True]
        elif word == '*':
            self.brailleList[0] += [False, False, False, False]
            self.brailleList[1] += [False, True, False, True]
            self.brailleList[2] += [True, False, True, False]
        elif word == '\\':
            self.brailleList[0] += [False, True, False, False]
            self.brailleList[1] += [False, False, False, False]
            self.brailleList[2] += [False, False, False, False]
        elif word == '$':
            self.brailleList[0] += [False, True, True, True]
            self.brailleList[1] += [False, False, False, True]
            self.brailleList[2] += [False, False, False, False]
        elif word == '%':
            self.brailleList[0] += [False, False, True, True]
            self.brailleList[1] += [False, True, True, False]
            self.brailleList[2] += [True, True, True, False]
    

    def splt_eng(self, word, closingQuotes = False, apostrophe = False):
        pass



def makeBrailleBlock(argv, statebar):
    braille = Braille()
    letter = Letter(argv)
    print()
    letter.i = 0
    while letter.i < len(letter.sentence):
        braille.process(letter.sentence[letter.i], letter.decideLanguage(), letter.judgeException(), letter.sentence, letter.i)
        letter.i += 1
    print()
    return braille.export()


def getBrailleStr(braille):
    s = 0
    result = str()
    for i in braille:
        for j in i:
            if j == 's':
                result += '  '
                continue
            elif j == False:
                result += '○'
            elif j == True:
                result += '●'

            if s == 1:
                result += ' '
                s = 0
            else:
                s += 1
        result += '\n'
    return result