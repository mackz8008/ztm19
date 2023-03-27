from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)



@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<page>")
def my_home2(page):
    page_names = ['index', 'works', 'contact', 'about', 'thankyou2']
    if page.split('.')[0] in page_names:
        return render_template(f'{page}')
    else:
        return render_template('index_old.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        file = database.write(f"\n{data['email']},{data['subject']},{data['message']}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        # csv_writer = database2.write(f"\n{data['email']},{data['subject']},{data['message']}")
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thankyou2.html')
        except:
            return 'did not save to database'
    else:
        return 'There was an error'
    return 'Finished'

