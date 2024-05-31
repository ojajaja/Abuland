document.getElementById('forecastForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    fetch('/forecast', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictedPrice').textContent = data.predictedPrice.toFixed(2);
        document.getElementById('predictedDemand').textContent = data.predictedDemand.toFixed(2);
        document.getElementById('forecastResult').style.display = 'block';
    });
});
