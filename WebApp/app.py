from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/forecast', methods=['POST'])
def forecast():
    # Retrieve inputs from the form
    rice_consumption = float(request.form['riceConsumption'])
    num_citizens = float(request.form['numCitizens'])
    median_age_citizen = float(request.form['medianAgeCitizen'])
    median_age_resident = float(request.form['medianAgeResident'])
    ratio_65_over_citizen = float(request.form['ratio65OverCitizen'])
    ratio_65_over_resident = float(request.form['ratio65OverResident'])
    ratio_65_over_residents = float(request.form['ratio65OverResident'])
    num_residents = float(request.form['numResidents'])
    gdp_per_capita = float(request.form['gdpPerCapita'])
    gni_per_capita = float(request.form['gniPerCapita'])
    gdp_per_capita_usd = float(request.form['gdpPerCapitaUSD'])
    gni_per_capita_usd = float(request.form['gniPerCapitaUSD'])
    total_population = float(request.form['totalPopulation'])
    population_density = float(request.form['populationDensity'])
    num_non_residents = float(request.form['numNonResidents'])

    # Perform predictive analysis here

    # For example:
    # Predicted variables using a simple transformation
    predicted_rice_price = rice_consumption * 1.1
    predicted_demand = num_citizens * 0.9

    # Return the predicted values
    return jsonify(
        predictedRicePrice=predicted_rice_price,
        predictedDemand=predicted_demand,
        # Add predicted values for other variables
    )


if __name__ == '__main__':
    app.run(debug=True)
