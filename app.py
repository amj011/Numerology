from flask import Flask, render_template, request
from lucky_numbers import Numerology  

app = Flask(__name__)
numerology = Numerology()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        birthdate = request.form['birthdate']
        name = request.form['name']  

        numerology.set_birthdate(birthdate)
        numerology.set_name(name)
        summary_info = numerology.print_summary()

        return render_template('result.html', summary_info=summary_info)


if __name__ == '__main__':
    app.run(debug=True)
