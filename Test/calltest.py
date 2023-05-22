import ctypes

#get your functions from importing the dll
userstuff = ctypes.WinDLL("C:\\Windows\\System32\\user32.dll")

#enums/flags its not predefined so you must define it your self.
NULL = 0x0
MB_OK = 0x0

userstuff.MessageBoxA(NULL, ctypes.c_char_p(b"Hello hi"), ctypes.c_char_p(b"Alerto!"), MB_OK)

