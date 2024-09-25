
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
key_pair = RSA.generate(2048)
print(key_pair.export_key())
public_key = key_pair.publickey()
print(public_key.export_key())
exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA1tzTsZc4ESIO8nviUf0XycTyfD3NxvzaoxpIDI3jcPRekGKj\nrIzfXpVZFjgF8R+BFd1INScVPFecY250MalVG4mxKB3tQW72KDBOMASJEJoOLp7P\n5ZpRUkW+Cmo97G52A1CmHtCVdpjNBvtcuOtcOZSyswsG77CxpKvkBHO0X4tV2oH4\nS/8E+LxAmojxpmk4P6soQ6L9+8YyZtI6OxEJLPKdNhoqc7Pf6h2DGMCOLlUcM9YR\nM4wAP8J4xerYKeWR5Yb+XPpJyTncR0PmvyQLbW+TZody3r2tAWHvf19R1lU9bO+x\nRVkUN3TqPpJMfWP7C8VdiYC+dTKJJ/Vcc+xGJQIDAQABAoIBACoFO/2CVnu7TnML\n2WIxfkJ+mvHDYIgnEVdOn4KdCTsg/5F7SQlI77JewPKAeGEEyUkOYr3Ka/PGKpaj\nlmPT+woMrrHq0Gi4m7mWYOQxLuEpT9a8Rmpf+MF/VEBTMNMZc0kIr8RdBK4SCh7w\nb9zWYs38D8rGQFAGHWfYGhroygDZMm3uNN6Pf9F+dR5O3NKZWV7uhnbv5b7Ofg2O\nk2wQ2vTNm9JCzC0ukDFwGETWgegG8ranp4xvgQOL7oaTRAzOZaATnFsG4A+7pQgd\nKAjMI0QvFODTHouIm1Mq8LZLVsezj0UEE3+H2FkreA6OecmHv9ROif1XPNBN2DL3\n/u5Dr2ECgYEA536Ld+z69ZG2XyEWSvHTBsAWqKdkCbPtb4o8vlSnNRjuTt/Xjlnf\nXWX0xI4KG+3cetC2/XlJFT0Tonxr30h7d4fRRHMo+YO4yBBFOU/9firSVH1nL4Nl\n2+YQftEyfStR7a9TD5CGj5LeklSA5KSxDtKJrpLNoEcmwmu1jf0suWkCgYEA7ZuQ\n0gweW4+5MLvcKx7NXFX6NyhFz7wv/PaoHqGPLaqBcoLyzpggqUPHZkKsPrWokmo+\nnHG3eWZ90ho+L4vmK2n4B462yXp1suOP13qxG0PitlV7b0PzeRFyKLsyYcKD0kaa\nXUj6jCH25AH8Too7foIWyVndCgQMcgL4rtc1M10CgYEAnJ7tVXIsSMERFkOYhZQf\nJk4IBotaD4aAehqZBlzX1ADOGucvO8xqZxJ4DBPdmw/PP/i+FbhdTdVI14I+qY6s\nmi51003mxwnrltALRb9szlPCgg9mJKtN2v1I48Q92JnakGkyVTF/GNxRYcdyfT8/\n27tuE4KXRH1fJ+MfrrU/8SECgYBNtNeq6g2vkhRVjMqXS46LyQ54pXIXWwsyppQa\n2GlT3PRSt+Kij/v2f1Uh62IbbBuCLr7lOQdw64TwhmaZ9B3FSvWzuweqYqNFasir\nBtQO/6eQS+p/W/CvQnZcPcRfVlb4GOD46xoNZDozHTcflHOajv7WwM3aLbLIQpKD\n05vxfQKBgQCcJifd7xvjn6uKfiuHjEQ3LyXCSnewD5VW6aXOm6zmP1NmVAoItIgN\nUSq9fsfXRLCC1k+CM7UvCDhgTjMpNSfwFveU3ZK/CT3MPbRhbCzYay/ksRwAg3w1\nh5m4qnhX8g1x8Z7ePWoNhVthIDL6+fSMpowDi2PvIV5KP5wGPl+LOQ==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1tzTsZc4ESIO8nviUf0X\nycTyfD3NxvzaoxpIDI3jcPRekGKjrIzfXpVZFjgF8R+BFd1INScVPFecY250MalV\nG4mxKB3tQW72KDBOMASJEJoOLp7P5ZpRUkW+Cmo97G52A1CmHtCVdpjNBvtcuOtc\nOZSyswsG77CxpKvkBHO0X4tV2oH4S/8E+LxAmojxpmk4P6soQ6L9+8YyZtI6OxEJ\nLPKdNhoqc7Pf6h2DGMCOLlUcM9YRM4wAP8J4xerYKeWR5Yb+XPpJyTncR0PmvyQL\nbW+TZody3r2tAWHvf19R1lU9bO+xRVkUN3TqPpJMfWP7C8VdiYC+dTKJJ/Vcc+xG\nJQIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

# sPubCollega = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvM+fu7IuRLyBgcEZ3yHL\ntn9ECFRMVOg/Mb+VE712rK8v68T+JhzFLA2dO94+/559wFx4mdYeF0DxhVetUTTF\nka7b0B2jVEogG2gOIdaQ56ll5zrIHn/S/2lcx/rt4DbT5tJKW3YNGfKkrQDIisz8\nICKlnle+IAPRLlJpFf4TfNQBjOPQjc0tQApNXMtVmKgDx7uVsvOKKRAH6rsyndT4\nHeqWz1ajqFYYFqDpCzPqYG3Q+1dYgBRtqOn/+QxzoA/X/svezyyJ+yNA8akqtv+S\n1Q/ibp2fCHNBICtEU3+pybmNEtONQXYD7gt+AQnmB4rFHoKxKfJHDQJuK+CaQhG6\nywIDAQAB\n-----END PUBLIC KEY-----"

"""public_key_collega = RSA.import_key(sPubCollega)
message = "Di che squadra sei?"
encrypted_message = encrypt_message(message, public_key_collega)
print("Encrypted Message:", encrypted_message)

cifrato = "WcGcdBVd8dV4a/V/iE9JtHne+0i9dXXZj6Y+CD47iADoQ2+UK0320MSTvX6s+UKF1g9EAdaYfgyt2EQ0ETGYA1l2ZwbYf++6kxyIjKDdqH/6nDfecgTBYXbBhrrm2c2t5TJWj2ME6LTAV1D3xizPYBS2dldtG/B02U6h3pMaK99eaBxzB76e0GuV5ddxiRlSEP0L7kyYFAGmkzXVJQ3WShydnUVReB2aQsyx+G/HxzYxKJqxuCgLzBmEJR4VZqjSzd9EODMc4NQBq3J8x3Q9E4gEflhDBbGAqbVpDusHqinoAQj6eKE91+4e8IuNUPvpz8qWz87pNpKiqD7tyoK9sw=="
decifrato = decrypt_message(cifrato, key_pair)
print("Il messaggio decifrato: ", decifrato)"""