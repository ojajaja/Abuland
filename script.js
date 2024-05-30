document.getElementById('forecastForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const ricePrice = parseFloat(document.getElementById('ricePrice').value);
    const riceDemand = parseFloat(document.getElementById('riceDemand').value);
    // Perform predictive analysis here (This is just a placeholder)
    const predictedPrice = ricePrice * 1.1; // Example: Predicting a 10% increase
    const predictedDemand = riceDemand * 0.9; // Example: Predicting a 10% decrease
    document.getElementById('predictedPrice').textContent = predictedPrice.toFixed(2);
    document.getElementById('predictedDemand').textContent = predictedDemand.toFixed(2);
    document.getElementById('forecastResult').style.display = 'block';
});
