# btc-pk-to-address
Python script to generate Bitcoin address from a private key.

## About
This script generate a Bitcoin address from a self produced private key in a Excel file.
Bitcoin related code is based on the example from the mastering bitcoin book:
[https://github.com/huntrontrakkr/bitcoinbook/](https://github.com/huntrontrakkr/bitcoinbook/blob/master/key-to-address-ecc-example.py) which is using the library [https://githubc.com/primal100/pybitcointools](https://githubc.com/primal100/pybitcointools).

## Disclaimer
Only test with small amounts. Depending on how you generate the key, the entropy is not sufficient to be secure.

## Install

1. Clone the repo:
   ```sh
   git clone https://github.com/f418me/btc-pk-to-address
   ```
2. Install Python Packages:
   ```sh
   pip install -r requirements.txt
   ```

## Generate private key

Rename rename-to-private_key.xlsx to private_key.xlsx and generate your private key.

## Usage
When you run the program all the keys will be printed to STOUT. After pressing "c" the address is shown as qr-code. If press another key the script exit without showing the qr-code.

 ```sh
    python generate_address_from_pk.py
   ```

