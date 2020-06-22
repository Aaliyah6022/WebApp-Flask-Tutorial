from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')


@app.route('/', methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
      username = request.form["username"]
      password = request.form["password"]
      print("Username: {}".format(username));
      print("Password: {}".format(password));
      return render_template("response.html", username=username, password=password);
    return render_template("index.html")

if __name__ == '__main__':
    app.run("127.0.0.1", port=69, debug=True, use_reloader=False)
