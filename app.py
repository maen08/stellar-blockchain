from traceback import print_tb
from stellar_sdk import Keypair
from flask import Flask, Response, request, jsonify
import json
import requests

app = Flask(__name__)


@app.route('/generate-address', methods=['GET'])
def generate_address():
    '''
    endpoint to generate random keypairs for public_key(site address) and private_key(seed)
    '''
    keypair = Keypair.random()
    public_key = keypair.public_key
    private_key = keypair.secret

    keys = {
        'public_key': public_key,
        'secret_seed': private_key
    }

    data = jsonify(keys)
    return data


@app.route('/get-xlm', methods=['POST'])
def get_testing_xlm():
    '''
    endpoint which get the testing xlm from testnetwork using the Stellar bot
    called friendbot which 
    '''

    xlm_link = 'https://horizon-testnet.stellar.org/friendbot?addr='
    headers = {
        'Content-Type': 'application/json'
    }

    address = request.get_json(force=True)
    url = xlm_link + address['address']

    res = requests.get(
        url=url,
        headers=headers

    )

    xlm = {
        'response': str(res.content)
    }

    return json.dumps(xlm)


# def make_payment(amount, item, asset='XLM'):

    # status = False
    # try:
    #     builder = Builder(secret=)




if __name__ == '__main__':
    app.run(debug=True)

    MEMBER_ADDR = "GD6JAEDLB7TWW62JLSX4J3H3NLMQB6LUCMECKSSMIEPLNGZIVRTRYBVN"
    MEMBER_SEED = "SC65XVZN2OCCYJEA22U6IDR5A74CL5WZSU7MZTNZQ7VLYE2AYXDJKB7Q"

    WALLET_ADDR = "GDJPJFRNLXOUVFEGV6H63MSWMO3CJZLDLMUREGM2LDHTIOACV3SMQV7L"
    WALLET_SEED = "SCJPDHOG2JB4ZAF5KJCYAWPM2SP6W7DEDYGJQF4M46MICGJBKALCWVEA"
