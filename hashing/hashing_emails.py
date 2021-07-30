from hashlib import sha256

secret_phrase = "lasagna"


def get_hash_with_secret_phrase(input_data, secret_phrase):
    combined = input_data + secret_phrase
    return sha256(combined.encode()).hexdigest()


email_body = "Hey!, i think you should learn\nAbout Blockchains and stuff\nIt's really cool :)"

print(get_hash_with_secret_phrase(email_body, secret_phrase))