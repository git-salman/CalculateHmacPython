from hashlib import sha256
import hmac


message = "Some message"
token = "a152d6b41875459893c1303707cfe386"

def create_hmac(token,message):
    tokenarray =  bytearray(token,'utf-8')
    string_to_sign = message.encode('utf-8')
    hashed = hmac.new(tokenarray,string_to_sign, sha256)

    return hashed

digest = create_hmac(token,message).digest()

print(digest)
