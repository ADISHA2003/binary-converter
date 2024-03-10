from flask import Flask, request, render_template
from binary_converter import decimal_to_binary, binary_to_decimal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    choice = request.form['choice']
    result = None

    if choice == '1':
        decimal = int(request.form['decimal'])
        result = decimal_to_binary(decimal)
    elif choice == '2':
        binary = request.form['binary']
        result = binary_to_decimal(binary)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
