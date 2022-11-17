from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    language = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']
    return f'''
           The language value is: {language}
          '''


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

