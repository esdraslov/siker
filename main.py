from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('index.html', location = 'home')

app.run(debug = True)
