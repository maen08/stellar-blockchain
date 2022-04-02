from traceback import print_tb
from stellar_sdk import Keypair
from flask import Flask, Response, request
import json


app = Flask(__name__)

@app.route('/gen-address', methods=['GET'])
def generate_address():

    keypair = Keypair.random()
    public_key = keypair.public_key
    private_key = keypair.secret

    # print(public_key)

    keys = {
        'public_key': public_key,
        'secret_seed': private_key
    }

    data = json.dumps(keys)
    return data







if __name__ == '__main__':
    app.run(debug=True)