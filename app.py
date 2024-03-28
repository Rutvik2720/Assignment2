from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return 'Rutvik Shah 100886648'

app.run(host='0.0.0.0')
