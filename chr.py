#!/usr/bin/env python3

def get_unicode_char(
    code_point: int, start: int = 0, end: int = 1114111, /
) -> str:
    """
    Returns a string representing a Unicode character 
    based on the given integer code point.

    :param code_point: The Unicode code point as an integer.
    :type code_point: int
    :param start: The starting value of the allowed range. Default is 0.
    :type start: int, optional
    :param end: The ending value of the allowed range. Default is 1114111.
    :type end: int, optional
    :return: The string representing the corresponding Unicode character.
    :rtype: str
    :raises ValueError: If the provided integer 
                        value is outside the specified range.

    Example:
        >>> get_unicode_char(0x61)
        'a'
        >>> get_unicode_char(97)
        'a'
        
    """
    if (not isinstance(code_point, int) 
        or code_point < start 
        or code_point > end):
        raise ValueError(
            "O valor fornecido deve estar no intervalo de {} a {}.".format(
                start, end
            )
        )

    if code_point <= 0xFFFF:
        return chr_utf8(code_point)

    code_point -= 0x10000
    high_surrogate = 0xD800 + (code_point >> 10)
    low_surrogate = 0xDC00 + (code_point & 0x3FF)

    return chr_utf8(high_surrogate) + chr_utf8(low_surrogate)

def chr_utf8(code_point: int, /) -> str:
    """
    Returns a string representing a UTF-8 character 
    based on the given integer code point.

    :param code_point: The Unicode code point as an integer.
    :type code_point: int
    :return: The string representing the corresponding UTF-8 character.
    :rtype: str

    """
    if code_point <= 0x7F:
        return bytes([code_point]).decode('utf-8')
    elif code_point <= 0x7FF:
        return bytes([0xC0 | (code_point >> 6),
                      0x80 | (code_point & 0x3F)]).decode('utf-8')
    elif code_point <= 0xFFFF:
        return bytes([0xE0 | (code_point >> 12),
                      0x80 | ((code_point >> 6) & 0x3F),
                      0x80 | (code_point & 0x3F)]).decode('utf-8')
    elif code_point <= 0x10FFFF:
        return bytes([0xF0 | (code_point >> 18),
                      0x80 | ((code_point >> 12) & 0x3F),
                      0x80 | ((code_point >> 6) & 0x3F),
                      0x80 | (code_point & 0x3F)]).decode('utf-8')

if __name__ == '__main__':
    print(get_unicode_char(0x61)) # -> a
    print(get_unicode_char(97)) # -> a

