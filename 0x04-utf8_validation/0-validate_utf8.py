#!/usr/bin/python3
"""
UTF-8 Validation Module
This module contains a function `validUTF8` that checks if a given data set
represents a valid UTF-8 encoding. UTF-8 encoding can range from 1 to 4 bytes
per character.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    A UTF-8 character can be represented by 1 to 4 bytes. Each byte in UTF-8
    follows specific patterns:
        - 1-byte character: 0xxxxxxx
        - 2-byte character: 110xxxxx 10xxxxxx
        - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
        - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Args:
        data (list of int): List of integers representing the data set,
                            where each integer is 1 byte (8 bits).

    Returns:
        bool: True if data represents a valid UTF-8 encoding, else False.
    """

    # Number of bytes remaining to complete the current UTF-8 character
    num_bytes = 0

    # Bitmask to check the leading bits of each byte
    mask1 = 1 << 7  # 10000000, to check the first bit
    mask2 = 1 << 6  # 01000000, to check the second bit

    for num in data:
        # Ensure only the 8 least significant bits are used (1 byte)
        byte = num & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's to determine byte length
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If num_bytes is 0, this is a 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 characters should be 1 to 4 bytes; otherwise, invalid
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check if this byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining for the current character
        num_bytes -= 1

    # If num_bytes is not zero, we have incomplete bytes for a character
    return num_bytes == 0
