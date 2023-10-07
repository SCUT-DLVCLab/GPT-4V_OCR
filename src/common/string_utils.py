# encoding: utf-8

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def char_f2h(uchar):
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:
        return uchar
    return chr(inside_code)

def string_f2h(ustring):
    return ''.join([char_f2h(uchar) for uchar in ustring])