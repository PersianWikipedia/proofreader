#!/usr/bin/env python3
# -*- coding: utf-8  -*-
#
# Huji (User:Huji), 2025
#
# Distributed under the terms of the MIT license.
import os

try:
    import hunspell

    hunspell_available = True
except Exception:
    hunspell_available = False


def suggest(word: str) -> list[str]:
    """Using the Persian hunspell dictionary, suggest alternative words that
    are similar in spelling to the provided word. The provided words doesn't
    have to be in the dictionary. If hunspell module is not installed, this
    function will return an empty list.

    Args:
        word (str): Provided words

    Returns:
        list[str]: A list of words
    """
    if hunspell_available is False:
        return []

    base_path = os.getcwd() + "/dict/"
    hobj = hunspell.HunSpell(base_path + "fa_IR.dic", base_path + "fa_IR.aff")

    return hobj.suggest(word)


def valid(word: str) -> bool:
    """Using the Persian hunspell dictionary, determines if the provided
    word is valid (i.e., exists in the dictionary). If hunspell modue is
    not installed, this function will return True for any input.

    Args:
        word (str): Provided words

    Returns:
        bool: True or False
    """
    if hunspell_available is False:
        return True

    base_path = os.getcwd() + "/dict/"
    hobj = hunspell.HunSpell(base_path + "fa_IR.dic", base_path + "fa_IR.aff")

    return hobj.spell(word)


if __name__ == "__main__":
    print(valid("ثیت"))
