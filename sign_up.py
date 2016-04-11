from flask import Flask, request, render_template

app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)

users =  ["mohamed","admin"]
emails = ["mohamed@gmail.com","admin@admin.com"]

def serve_forever():
    app.run(host, port)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
	
@app.route('/')
def main():
     return render_template("regs.html")


@app.route('/signup', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username not in users and email not in emails:
            return "Success"
        else:
            return "Fail"
    else:
        return render_template("regs.html")


if __name__ == '__main__':
    serve_forever()