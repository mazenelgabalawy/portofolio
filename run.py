import csv
from os import name, write
from flask import Flask , render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(f'{page_name}')

def write_to_database(data):
    with open('database.txt', 'a') as database:
          name = data['name']
          email = data['email']
          subject = data['subject']
          message = data['message']
          database.write(f'\n{name}, {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)