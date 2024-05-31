document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('forecastForm');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch('/forecast', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('forecastResult').style.display = 'block';
            document.getElementById('predictedRicePrice').textContent = data.predictedRicePrice.toFixed(2);
            document.getElementById('predictedDemand').textContent = data.predictedDemand.toFixed(2);
        })
        .catch(error => console.error('Error:', error));
    });
});
