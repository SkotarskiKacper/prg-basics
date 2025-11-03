import random

PlainText="Moim Sdaniem to nie ma tak że dobrze, albo że nie dobrze"
EncryptedText=""
EncryptionKey=""
DecryptedText=""

def Encrypt(Character,Key):
    return chr(ord(Character)+Key)

def Decrypt(Character,Key):
    return chr(ord(Character)-Key)

for i in range(len(PlainText)):
    RandomValue=random.randrange(0,9,1)
    EncryptionKey+=str(RandomValue)
    EncryptedText+=Encrypt(PlainText[i],RandomValue)

for i in range(len(PlainText)):
    DecryptedText+=Decrypt(EncryptedText[i],int(EncryptionKey[i]))


print(PlainText)
print(EncryptionKey)
print(EncryptedText)
print(DecryptedText)
