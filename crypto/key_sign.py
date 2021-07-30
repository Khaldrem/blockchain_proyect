from nacl.public import Box, PrivateKey

alices_private_key = PrivateKey.generate()
bob_private_key = PrivateKey.generate()

alices_public_key = alices_private_key.public_key
bob_public_key = bob_private_key.public_key

bobs_box = Box(bob_private_key, alices_public_key)
encrypted = bobs_box.encrypt(b"Hello Alice!")

alices_box = Box(alices_private_key, bob_public_key)

plaintext = alices_box.decrypt(encrypted)
print(plaintext.decode('utf-8'))