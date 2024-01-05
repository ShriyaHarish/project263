from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")

#initialize flask
def main():
	return render_template("index.html")

# Render HTML with count variable
@app.route('/', methods = ['POST'])

#route your webpage
def math_operations():
	equation = request.form['text']
	operation = request.form['operation']
	result = 'https://newton.now.sh/api/v2/'+operation+'/'+equation
	data = requests.get(result).json()
	answer =data['result']
	return render_template("index.html", result = answer, eqaution = equation)
if __name__ == "__main__":
	app.run()