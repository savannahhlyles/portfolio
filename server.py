from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# ROUTES

@app.route('/')
def default():
   return render_template('home.html')   

@app.route('/resume')
def resume():
   return render_template('resume.html')   



if __name__ == '__main__':
   app.run(debug = True, port=5001)