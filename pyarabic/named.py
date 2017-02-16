#!/usr/bin/python
# -*- coding=utf-8 -*-
#
"""
Arabic Named enteties recognation pyarabic.named
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies,  Arabeyes,   Taha Zerrouki
@license: GPL
@date:2017/02/14
@version: 0.3
"""

import sys
if __name__  ==  '__main__':
    sys.path.append('../')
    import pyarabic.arabrepr as arabrepr
sys.path.append('../../lib')
import pyarabic.araby as araby
import pyarabic.named_const as named_const
import pyarabic.propernouns as propernouns
# from number import *
DINENAMED = (
'شمس',
'تقي',
'علاء',
'نجم',
'نور',
'سيف',

)
def is_proper_noun(word):
    """
    Test if the word is a proper noun
    @param word: given word
    @type word: unicode
    @return: True if is properword
    @rtype: Boolean
    """
    # return word in named_const.ProperNouns    
    return word in propernouns.ProperNouns       

def detect_named_position(wordlist):
    """
    Detect named enteties words in a text and return positions of each phrase.
    
    Example:
        >>> detect_named_position(u"قال خالد بن رافع  حدثني أحمد بن عنبر عن خاله")    
        ((1,3), (6,8))    
    
    @param wordlist: wordlist
    @type wordlist: unicode list
    @return: list of numbers clause positions [(start,end),(start2,end2),]
    @rtype: list of tuple
    """
    #~ wordlist#=text.split(u' ')    
    #print words    
    positions = []    
    startnamed = -1    
    endnamed   = False    
    # print u":".join(wordlist).encode('utf8')    
    for i in range(len(wordlist)):
        word = wordlist[i]    
        if i+1 < len(wordlist):
            nextword = araby.strip_tashkeel(wordlist[i+1])    
        else: nextword = ''
        if i-1 >= 0: 
            previous = araby.strip_tashkeel(wordlist[i-1])    
            if previous and startnamed < 0  and\
               previous[0] in ('و', 'ف', 'ل', 'ب', 'ك'):
                previous = previous[1:]    
        else: 
            previous = ''
        #save the original word with possible harakat if exist
        word_nm = araby.strip_tashkeel(word)    
        key = word_nm    
        # the first word can have prefixes 
        if word_nm and startnamed < 0  and\
          word_nm[0] in ('و', 'ف', 'ل', 'ب', 'ك'):
            key = word_nm[1:]    
        if startnamed < 0 and key in ('ابن', ):
            startnamed = i    
            endnamed = i

        elif key in ('ابن', 'بن', 'أبو', 'أبا', \
            'أبي', 'عبد' , 'عبيد' , 'بنو', 'بني', 'بنت'):
            if startnamed < 0:
                startnamed = i    
            endnamed = i
    
        elif previous in ('بن', 'ابن', 'أبو', 'أبا', \
           'أبي', 'عبد', 'عبيد', 'بنو', 'بني', 'بنت'):
            if startnamed < 0:
                startnamed = i-1    
            endnamed = i
        elif nextword in ('بن', 'بنت',): 
            #  u'أبو', u'أبي', u'ابا',) :#or word in (u'الدين',):
            if startnamed < 0:
                startnamed = i    
            endnamed = i
        # if the word is a proper noun
        elif startnamed < 0 and is_proper_noun(key):
            startnamed = i    
            endnamed = i
        else:
            if startnamed >= 0: #There are a previous number phrase.
                if word_nm.startswith('ال') and word_nm.endswith('ي'):
                    # add family name إضافة الكنية
                    endnamed = i

                positions.append((startnamed, endnamed))    
            startnamed = -1    
    # add the final phrases 
    if startnamed >= 0: #There are a previous number phrase.
        positions.append((startnamed, endnamed))    
    return positions

def extract_named(text):
    """
    Extract named enteties words in a text.
    
    Example:
        >>> extract_named(u"قال خالد بن رافع  حدثني أحمد بن عنبر عن خاله")    
        ("خالد بن رافع"، "أحمد بن عنبر ")
    
    @param text: input text
    @type text: unicode
    @return: named enteties words extracted from text
    @rtype: integer
    """
    phrases = []    
    wordlist = araby.tokenize(text)    
    positions =  detect_named_position(wordlist)    

    for pos in positions:
        if len(pos) >= 2:
            if pos[0] <= len(wordlist) and pos[1] <= len(wordlist):
                phrases.append(' '.join(wordlist[pos[0]: pos[1]+1]))
    return phrases    
    

def extract_named_within_context(text):
    """
    Extract number words in a text.
    Example:
        >>> extract_named_within_context(u"تصدق عبد الله بن عمر بدينار")    
        ("تصدق"، "عبد الله بن عمر"، "بدينار")
        
    @param text: input text
    @type text: unicode
    @return: number words extracted from text
    @rtype: integer
    """
    phrases = []    
    wordlist = araby.tokenize(text)    
    positions =  detect_named_position(wordlist)       
    for pos in positions:
        # print pos    
        if len(pos) >= 2:
            if pos[0] <= len(wordlist) and pos[1] <= len(wordlist):
                if pos[0]-1 >= 0: 
                    previous = wordlist[pos[0]-1]    
                else: previous = ''    
                if pos[1]+1 < len(wordlist): 
                    nextword = wordlist[pos[1]+1]    
                else: nextword = ''    
                phrases.append((previous, \
                   ' '.join(wordlist[pos[0]: pos[1]+1]), nextword))
    return phrases    


    
def get_previous_tag(word):
    """Get the word tags
    @param word: given word
    @type word: unicode
    @return: word tag
    @rtype: unicode
    """
    word = araby.strip_tashkeel(word)    
    #~ tags = u''    
    if word in named_const.NOUN_NASEB_LIST:
        return 'منصوب'    
    elif word in named_const.JAR_LIST:
        return 'مجرور'    
    elif word in named_const.RAFE3_LIST:
        return 'مرفوع'    
    else:
        return ''    


def vocalize_named(wordlist, syn_tags = ""):
    """ Vocalize a number words
    @param wordlist: words to vocalize
    @type wordlist: unicode list
    @param syn_tags: tags about the clause
    @type syn_tags: unicode
    @return: the vocalized wordlist.
    @rtype: unicode
    """
    newlist = []    
    #~ prefix = u""    
    #~ nextword = u""    
    #detect tags 
    # we can pass tags to this number word
    tags =  syn_tags    
    bin_count = 0    
    for i in range(len(wordlist)):
        #save the original word with possible harakat if exist
        word = wordlist[i]    
        word_nm = araby.strip_tashkeel(word)    
        # the first word can have prefixes 
        if i == 0 and word_nm:  
            # word to get majrour tag
            if word_nm in ('أبي', 'بنو', 'آل', 'ابن',):
                tags += "مجرور"    
            elif word_nm in ('أبو', ):
                tags += "مرفوع"    
            elif word_nm in ('أبا', ):
                tags += "منصوب"    
        # select vocalization
        if word_nm == 'بن':
            bin_count += 1    
            #treat first bin according to tags
            if bin_count == 1:
                if 'مجرور' in tags:
                    voc = 'بْنِ'
                elif 'مرفوع' in tags:
                    voc = 'بْنُ'
                elif 'منصوب' in tags:
                    voc = 'بْنَ'
                else:
                    voc = 'بْن'
            else:
                #  u'مجرور' 
                voc = 'بْنِ'
        #Todo Vocalize names
        else:
            voc = word    
        newlist.append(voc)    
    return newlist    

def detect_named(wordlist):
    """
    Detect named enteties words in a text and return positions of each phrase.
    
    Example:
        >>> detect_named_position(u"قال خالد بن رافع  حدثني أحمد بن عنبر عن خاله")    
        ((1,3), (6,8))
    
    @param wordlist: wordlist
    @type wordlist: unicode list
    @return: list of numbers clause positions [(start,end),(start2,end2),]
    @rtype: list of tuple

    """
    #~ wordlist#=text.split(u' ')    
    #print words    
    positions = []    
    startnamed = False
    taglist = []    
    endnamed   = False    
    previous = ""
    for i in range(len(wordlist)):
        word = wordlist[i]
        #save the original word with possle harakat if exist
        word_nm = araby.strip_tashkeel(word)
        key = word_nm  # make a key 
        if i+1 < len(wordlist):
            nextword = araby.strip_tashkeel(wordlist[i+1])    
        else: nextword = ''
        if previous and not startnamed  and previous[0] in ('و', 'ف', 'ل', 'ب', 'ك'):
            previous = previous[1:]    
        # the first word can have prefixes 
        if word_nm and not startnamed and word_nm[0] in ('و', 'ف', 'ل', 'ب', 'ك'):
            key = word_nm[1:]    
        if not startnamed and key in ('ابن', ):
            startnamed = True
            taglist.append("NB")   
        elif key in ('ابن', 'بن', 'أبو', 'أبا', \
            'أبي', 'عبد' , 'عبيد' , 'بنو', 'بني', 'بنت'):
            if not startnamed:
                startnamed = True
                taglist.append("NB")   
            else:
                taglist.append("NI")
    
        elif previous in ('بن', 'ابن', 'أبو', 'أبا', \
           'أبي', 'عبد', 'عبيد', 'بنو', 'بني', 'بنت'):
            if not startnamed:
                startnamed = True
                taglist.pop()
                taglist.append("NB")   
            else:
                taglist.append("NI")
        elif nextword in ('بن', 'بنت',): 
            #  u'أبو', u'أبي', u'ابا',) :#or word in (u'الدين',):
            if not startnamed:
                startnamed = True
                taglist.append("NB")   
            else:
                taglist.append("NI")
        # if the word is a proper noun
        elif not startnamed and is_proper_noun(key):
            startnamed = True
            taglist.append("NB")   
        else:
            if startnamed >= 0: #There are a previous number phrase.
                if word_nm.startswith('ال') and word_nm.endswith('ي'):
                    # add family name إضافة الكنية
                    taglist.append("NI")
                else:
                    taglist.append("O")
                    startnamed = False
            else:
                taglist.append("O")
                startnamed = False
                                  
        previous = word_nm
    return taglist
def pretashkeel_named(wordlist):
    """
    Detect named words in a text.
    @param wordlist: input text
    @type wordlist: unicode
    @return: wordlist with vocalized named clause
    @rtype: list
    """
    taglist = detect_named(wordlist)
    previous = ""
    vocalized_list = []
    chunk = []
    previous_tag = ""
    for word, tag in zip(wordlist, taglist):
        if tag in ("NB", "NI"):
            chunk.append(word)
        else:
            if chunk:
              #get the tag of previous word
              previous_tag = get_previous_tag(previous)
              vocalized = vocalize_named( chunk, previous_tag)
              vocalized_list.extend(vocalized)
              chunk =[]
            vocalized_list.append(word)
            previous = word
        
    return vocalized_list


if __name__ == '__main__':
    #import number as ArabicNumberToLetters
    TEXTS = [
    "وجد عبد الله بن عمر دينارا",
    
    "جاء  خالد بن الوليد وقاتل مسيلمة بن حذام الكذاب في موقعة الحديقة", 
    '''روى أحمد بن عقيل الشامي عن أبي طلحة
 المغربي أنّ عقابا بن مسعود بن أبي سعاد قال''',
     "قال مُحَمَّدُ بْنُ خَالِدُ بْنُ إسماعيلفي حديثه",
    "ِنْصَرَفْنَا إِلَى أَنَسُ بْنُ مَالِكَ الْحَديثِ"
    ]    
    for text1 in TEXTS:
        positions_named = detect_named_position(text1.split(' '))    
        print(positions_named)    
        text1 = araby.strip_tashkeel(text1)

   
        result = pretashkeel_named(araby.tokenize(text1))    
        print(' '.join(result).encode('utf8'))
        
        wordlist = araby.tokenize(text1)
        taglist = detect_named(wordlist)

        arepr = arabrepr.ArabicRepr()
        print(arepr.repr(list(zip(taglist, wordlist))).encode('utf8'))  
   

