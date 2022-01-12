from flask import Flask, render_template, request, redirect
import csv

app2 = Flask(__name__)


@app2.route("/")
def my_home():  # put aplication's code here
    return render_template("index.html")


@app2.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)


def write_to_txt(data):
    with open("database.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database2.csv", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database)
        csv_writer.writerow([email, subject, message])


@app2.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            #write_to_txt(data)
            write_to_csv(data)
            #print(data)
            return redirect("thankyou.html")
        except:
            return "didn't save to database"
    else:
        return "something went wrong"

if __name__ == "__main__":
    app2.run()
