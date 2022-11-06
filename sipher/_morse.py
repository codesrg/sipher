from __future__ import annotations

from os import PathLike
from typing import AnyStr, Optional

from ._sipher import Sipher
from . import sipherutil as su


class Morse(Sipher):
    def __init__(self):
        self.__MORSE_CODE = {'A': '.-', 'B': '-...',
                             'C': '-.-.', 'D': '-..', 'E': '.',
                             'F': '..-.', 'G': '--.', 'H': '....',
                             'I': '..', 'J': '.---', 'K': '-.-',
                             'L': '.-..', 'M': '--', 'N': '-.',
                             'O': '---', 'P': '.--.', 'Q': '--.-',
                             'R': '.-.', 'S': '...', 'T': '-',
                             'U': '..-', 'V': '...-', 'W': '.--',
                             'X': '-..-', 'Y': '-.--', 'Z': '--..',
                             '1': '.----', '2': '..---', '3': '...--',
                             '4': '....-', '5': '.....', '6': '-....',
                             '7': '--...', '8': '---..', '9': '----.',
                             '0': '-----', ', ': '--..--', '.': '.-.-.-',
                             '?': '..--..', '/': '-..-.', '-': '-....-',
                             '(': '-.--.', ')': '-.--.-', ' ': ''}
        self.__em = ''
        self.__dm = ''

    def encrypt(self, data: AnyStr | PathLike[AnyStr], key=None, copy_to_clipboard: bool = False, store: bool = False,
                store_path: Optional[str] = None):
        if isinstance(data, PathLike):
            data = self._get_data_from_file(data)
        for letter in data:
            self.__em += self.__MORSE_CODE[letter.upper()] + " "
        if copy_to_clipboard is True:
            is_copied = su.copy_to_clipboard(self.__em)
            if is_copied:
                print("Encrypted message copied to clipboard.")
        if store is True:
            path = su.store(data=self.__em, path=store_path, alg=self.__class__.__name__.lower())
            if path.exists():
                print("Encrypted message stored in '" + path.__str__() + "'")
        return self.__em

    def decrypt(self, data: AnyStr | PathLike[AnyStr], key=None, copy_to_clipboard: bool = False, store: bool = False,
                store_path: Optional[str] = None):
        if isinstance(data, PathLike):
            data = self._get_data_from_file(data)
        word_list = [word for word in data.split("  ")]
        for word in word_list:
            for char in word.split():
                index = list(self.__MORSE_CODE.values()).index(char)
                self.__dm += list(self.__MORSE_CODE.keys()).pop(index)
            self.__dm += " "
        self.__dm = self.__dm.strip()
        if copy_to_clipboard is True:
            is_copied = su.copy_to_clipboard(self.__dm)
            if is_copied:
                print("Decrypted message copied to clipboard.")
        if store is True:
            path = su.store(data=self.__dm, path=store_path, alg=self.__class__.__name__.lower())
            if path.exists():
                print("Decrypted message stored in '" + path.__str__() + "'")
        return self.__dm