# -*- coding: utf-8 -*-


import re


BASE_CODE = 44032
CHOSUNG = 588
JUNGSUNG = 28

def getCharCode(word):
    return ord(word) - BASE_CODE

def getChosung(word):
    return getCharCode(word) // CHOSUNG

def getJunsung(word):
    return (getCharCode(word) - (getChosung(word) * CHOSUNG)) // JUNGSUNG

def getJongsung(word):
    return getCharCode(word) - (getChosung(word) * CHOSUNG) - (getJunsung(word) * JUNGSUNG)

def getWithoutChosung(word):
    return (getCharCode(word) % CHOSUNG) + BASE_CODE

def getWithoutJongsung(word):
    return ord(word) - getJongsung(word)


def isKorean(word):
    return re.match('.*[가-힣]+.*', word) is not None

def isKor(word):
    return re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', word) is not None

