import nacl.encoding
import nacl.signing


bob_priv_key = nacl.signing.SigningKey.generate()
bob_pub_key = bob_priv_key.verify_key

bob_pub_key_hex = bob_pub_key.encode(encoder=nacl.encoding.HexEncoder)
print(f"Bob Public Key: {bob_pub_key_hex}")

signed = bob_priv_key.sign(b"Some important message")
print(signed)