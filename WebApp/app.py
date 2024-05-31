from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/forecast', methods=['POST'])
def forecast():
    rice_price = float(request.form['ricePrice'])
    rice_demand = float(request.form['riceDemand'])

    # Perform predictive analysis here
    predicted_price = rice_price * 1.1
    predicted_demand = rice_demand * 0.9

    return jsonify(predictedPrice=predicted_price, predictedDemand=predicted_demand)


if __name__ == '__main__':
    app.run(debug=True)
