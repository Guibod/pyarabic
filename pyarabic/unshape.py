#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Arabic unshape letters
Allow to convert standard text to forms in programs which doesn't support arabic letters rendering
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies,  Arabeyes,   Taha Zerrouki
@license: GPL
@date:2017/02/14
@version: 0.3
""" 
unshaping_table={
'\uFEA1':'\u062D',
'\uFEA3':'\u062D',
'\uFEA4':'\u062D',
'\uFEA2':'\u062D',
'\uFEA5':'\u062E',
'\uFEA7':'\u062E',
'\uFEA8':'\u062E',
'\uFEA6':'\u062E',
'\uFEA9':'\u062F',
'\uFEAA':'\u062F',
'\uFE95':'\u062A',
'\uFE97':'\u062A',
'\uFE98':'\u062A',
'\uFE96':'\u062A',
'\uFE99':'\u062B',
'\uFE9B':'\u062B',
'\uFE9C':'\u062B',
'\uFE9A':'\u062B',
'\uFE9D':'\u062C',
'\uFE9F':'\u062C',
'\uFEA0':'\u062C',
'\uFE9E':'\u062C',
'\uFEC5':'\u0638',
'\uFEC7':'\u0638',
'\uFEC8':'\u0638',
'\uFEC6':'\u0638',
'\uFEE9':'\u0647',
'\uFEEB':'\u0647',
'\uFEEC':'\u0647',
'\uFEEA':'\u0647',
'\uFEAB':'\u0630',
'\uFEAC':'\u0630',
'\uFED9':'\u0643',
'\uFEDB':'\u0643',
'\uFEDC':'\u0643',
'\uFEDA':'\u0643',
'\uFEC1':'\u0637',
'\uFEC3':'\u0637',
'\uFEC4':'\u0637',
'\uFEC2':'\u0637',
'\uFEE5':'\u0646',
'\uFEE7':'\u0646',
'\uFEE8':'\u0646',
'\uFEE6':'\u0646',
'\uFEB5':'\u0634',
'\uFEB7':'\u0634',
'\uFEB8':'\u0634',
'\uFEB6':'\u0634',
'\uFEDD':'\u0644',
'\uFEDF':'\u0644',
'\uFEE0':'\u0644',
'\uFEDE':'\u0644',
'\uFEE1':'\u0645',
'\uFEE3':'\u0645',
'\uFEE4':'\u0645',
'\uFEE2':'\u0645',
'\uFED5':'\u0642',
'\uFED7':'\u0642',
'\uFED8':'\u0642',
'\uFED6':'\u0642',
'\uFECD':'\u063A',
'\uFECF':'\u063A',
'\uFED0':'\u063A',
'\uFECE':'\u063A',
'\u0640':'\u0640',
'\uFEBD':'\u0636',
'\uFEBF':'\u0636',
'\uFEC0':'\u0636',
'\uFEBE':'\u0636',
'\uFED1':'\u0641',
'\uFED3':'\u0641',
'\uFED4':'\u0641',
'\uFED2':'\u0641',
'\uFEB9':'\u0635',
'\uFEBB':'\u0635',
'\uFEBC':'\u0635',
'\uFEBA':'\u0635',
'\uFEED':'\u0648',
'\uFEEE':'\u0648',
'\uFEEF':'\u0649',
'\uFEF0':'\u0649',
'\uFE85':'\u0624',
'\uFE86':'\u0624',
'\uFE87':'\u0625',
'\uFE88':'\u0625',
'\uFE89':'\u0626',
'\uFE8B':'\u0626',
'\uFE8C':'\u0626',
'\uFE8A':'\u0626',
'\uFE8D':'\u0627',
'\uFE8E':'\u0627',
'\uFEB1':'\u0633',
'\uFEB3':'\u0633',
'\uFEB4':'\u0633',
'\uFEB2':'\u0633',
'\uFE80':'\u0621',
'\uFE81':'\u0622',
'\uFE82':'\u0622',
'\uFE83':'\u0623',
'\uFE84':'\u0623',
'\uFEF1':'\u064A',
'\uFEF3':'\u064A',
'\uFEF4':'\u064A',
'\uFEF2':'\u064A',
'\uFEAD':'\u0631',
'\uFEAE':'\u0631',
'\uFE8F':'\u0628',
'\uFE91':'\u0628',
'\uFE92':'\u0628',
'\uFE90':'\u0628',
'\uFE93':'\u0629',
'\uFE94':'\u0629',
'\uFEC9':'\u0639',
'\uFECB':'\u0639',
'\uFECC':'\u0639',
'\uFECA':'\u0639',
'\uFEAF':'\u0632',
'\uFEB0':'\u0632',
'\uFEF5':'\u0644\u0622',#LAM_ALEF_MADDA_ABOVE
'\uFEF7':'\u0644\u0623',#LAM_ALEF_HAMZA_ABOVE
'\uFEF9':'\u0644\u0625',#LAM_ALEF_HAMZA_BELOW
'\uFEFC':'\u0644\u0627',# LAM ALEF

}
def unshaping_text(text):
    """ Unshape a text

    Example:
        >>> TEXTS = u'لو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
        >>> print unshaping_text(TEXTS).encode('utf8')
        باضغ ماـــنالاو ىضرت كتيلو   ةريرم ةاـيحلاو ولحت كتيلف
    
    @param text: input text
    @type text: unicode
    @return: unshaped text
    @rtype: unicode
    """
    unshaping_text="";
    list_line=text.splitlines();
    for line in list_line:
        unshaping_text+="\n"+unshaping_line(line);
    return unshaping_text;


def unshaping_line(line):
    """ Unshape a  line
    
    Example:
        >>> line = u'فليتك تحلو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
        >>> print unshaping_line(line).encode('utf8')
        باضغ ماـــنالاو ىضرت كتيلو   ةريرم ةاـيحلاو ولحت كتيلف
        
    @param line: input line
    @type line: unicode
    @return: unshaped line
    @rtype: unicode
    """    
    unshaping_line="";
    currentword="";
    words=line.split();
    newwordlist=[];
    for word in words:
       newwordlist.append(unshaping_word(word));
    newwordlist.reverse()
    return ' '.join(newwordlist)



def unshaping_word(word):
    """ Unshape a word
    
    Example:
        >>> word = u'العربية'
        >>> print unshaping_word(word).encode('utf8')
        ةيبرعلا
    
    @param word: input word
    @type word: unicode
    @return: unshaped word
    @rtype: unicode
    """       
    unshaping_word="";
    for c in word:
        if c in list(unshaping_table.keys()):
            unshaping_word = unshaping_table[c] + unshaping_word;
        else:
            unshaping_word = c + unshaping_word;
    return unshaping_word;


if __name__  ==  '__main__':
    TEXTS = """فليتك تحلو والحيـاة مريرة * وليتك ترضى والانـــام غضاب 
وليت الذي بيني وبينك عامر * وبيني وبين العـالمين خراب
اذا صح الود فيك فالكل هين * وكل الي فــوق التراب تراب    """
    print(unshaping_text(TEXTS).encode('utf8'))
    print("--line--")
    line = 'فليتك تحلو والحيـاة مريرة * وليتك ترضى والانـــام غضاب '
    print(unshaping_line(line).encode('utf8'))
    print("--word--")
    word = 'العربية'
    print(unshaping_word(word).encode('utf8'))


