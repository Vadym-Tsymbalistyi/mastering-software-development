# 18.1 If you haven?t installed flask yet, do so now. This will also install werkzeug,
# jinja2, and possibly other packages.
# 18.2 Build a skeleton website, using Flask?s debug/reload development web server.
# Ensure that the server starts up for hostname localhost on default port 5000. If your
# computer is already using port 5000 for something else, use another port number.
# 18.3 Add a home() function to handle requests for the home page. Set it up to return
# the string It's alive!.
# 18.5 Modify your server?s home() function to use the home.html template. Provide it
# with three GET parameters: thing, height, and color.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    thing = request.args.get('thing', 'bilding')
    height = request.args.get('height', '20')
    color = request.args.get('color', 'black')
    return render_template('home.html', thing=thing, height=height, color=color)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
