import nacl.encoding
import nacl.signing

bob_public_key = b'3a35862a55be628ec710be3528f2495ac95b9ce9acf3bbe003b8a9d6b5c37ca1'

verify_key = nacl.signing.VerifyKey(bob_public_key, encoder=nacl.encoding.HexEncoder)
signed_message = b'5\x9b\x16X\x1dq-i\xdc\x1b\xfc\xb3d\xec\x1a9\x14y\xbf\xbd\xccp\x06\xbf/\x8e\xf8l?\x80s\xf2\xcblt\xd0Ao\xfe\x12\xe5;\x01\x98\xa3\xa6G\x9c\xc2\x1c:=\xd0*\xc9\x0edz].\x13S\xae\x0bSome important message'

v = verify_key.verify(signed_message)
print(v)