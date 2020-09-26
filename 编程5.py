#Caesar Cipher
MAX_KEY_SIZE = 26
def getMode( ):
    while True:
        print("你想加密还是解密？(encryprt/decrypt)")
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("请输入'encrypt','e','decrypt','d'")

def getMessage( ):
    print("输入你的消息:")
    return input()

def getKey():
    key = 0
    while True:
        print('请输入密钥数字（1-%s）%（MAX_KEY_SIZE )')
        key = int(input())
        if (key >=1 and key <= MAX_KEY_SIZE ):
            return key
def getTranslatedMessage(mode,message,key):
    if mode[0] =='d':
        key = -key
    translated = ''

    for symbol in message :
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print("你转换的密文是:")
print(getTranslatedMessage(mode,message,key))

