import warnings
import cryptos
import qrcode
import keyboard
from openpyxl import load_workbook

# ignore some warnings by openpyxl
warnings.simplefilter(action='ignore', category=UserWarning)
c

print("  ")
print(" --------------------------------------------------- ")
print(" --------Hello, ready for Bitcoin knowledge?---------- ")
print(" --------------------------------------------------- ")
print(" -----------   Don't do that at home      ---------- ")
print(" --------------------------------------------------- ")
print(" ")


# define excel file
wb = load_workbook(filename='private_key.xlsx', data_only=True)

# which sheet is to read
work_sheet = wb['key']

# read privat key from cell E*
cell = work_sheet['E3']
private_key = cell.value


# cryptos.N = Max # Elliptic curve parameter (secp256k1) = 115792089237316195423570985008687907852837564279074904382605163141518161494337
# Max in Hex: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

decoded_private_key = cryptos.decode_privkey(private_key, 'hex')
valid_private_key = 0 < decoded_private_key < cryptos.N

if valid_private_key == False:
    print(" -----------   Private Key not valid   ---------- ")
    exit()

print("  ")
print(" --------------------------------------------------- ")
print(" -------------   Keep this Private    -------------- ")
print(" --------------------------------------------------- ")
print(" ")

print("Private Key (hex) is: ", private_key)
print("Private Key (decimal) is: ", decoded_private_key)

# Convert private key to WIF format
wif_encoded_private_key = cryptos.encode_privkey(decoded_private_key, 'wif')
print("Private Key (WIF) is: ", wif_encoded_private_key)

# Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'
print("Private Key Compressed (hex) is: ", compressed_private_key)

# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = cryptos.encode_privkey(
    cryptos.decode_privkey(compressed_private_key, 'hex_compressed'), 'wif_compressed')
print("Private Key (WIF-Compressed) is: ", wif_compressed_private_key)

# Multiply the EC generator point G with the private key to get a public key point
public_key = cryptos.fast_multiply(cryptos.G, decoded_private_key)
print("Public Key (x,y) coordinates is:", public_key)

# Encode as hex, prefix 04
hex_encoded_public_key = cryptos.encode_pubkey(public_key, 'hex')
print("Public Key (hex) is:", hex_encoded_public_key)

# Compress public key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key
compressed_prefix = '02' if (public_key_y % 2) == 0 else '03'
hex_compressed_public_key = compressed_prefix + (cryptos.encode(public_key_x, 16).zfill(64))
print("Compressed Public Key (hex) is:", hex_compressed_public_key)

# Generate bitcoin address from public key
print("Bitcoin Address (b58check) is:", cryptos.pubkey_to_address(public_key))

print("  ")
print(" --------------------------------------------------- ")
print(" ---------------  Thats for public   --------------- ")
print(" --------------------------------------------------- ")
print(" ")

# generate Bitcoin address from compressed public key
bitcoin_address = cryptos.pubkey_to_address(hex_compressed_public_key)

print("Compressed Bitcoin Address (b58check) is:",bitcoin_address)
print(" ")
print(" --------------------------------------------------- ")
print(" ")

# Generate qr-code which contains the address with the prefix "bitcoin:"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('bitcoin:'+bitcoin_address)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color="black", back_color="white")

# Read from keyboard
taste = keyboard.read_key()

# Show qr-code of address if c is pressed
if taste == 'c':
    img.show()
