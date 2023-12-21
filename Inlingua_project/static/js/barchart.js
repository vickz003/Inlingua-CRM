// Bar chart with custom tooltip
const dataBarCustomTooltip = {
    labels: ['Office Name', 'Office Name', 'Office Name', 'Office Name', 'Office Name', 'Office Name', 'Office Name','Office Name','Office Name','Office Name'],
    datasets: [
        {
            label: 'Traffic',
            data: [30, 15, 62, 65, 61, 65, 40, 61, 65, 90],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
        },
    ],
};

const optionsBarCustomTooltip = {
    scales: {
        y: {
            beginAtZero: true,
        },
    },
    plugins: {
        legend: {
            display: true,
            position: 'top',
        },
        tooltip: {
            callbacks: {
                label: function (context) {
                    let label = context.dataset.label || '';
                    label = `${label}: ${context.formattedValue} users`;
                    return label;
                },
            },
        },
    },
};

// Get the context of the canvas element
const ctx = document.getElementById('bar-chart-custom-tooltip').getContext('2d');

// Set the width and height for the canvas
ctx.canvas.width = window.innerWidth * 0.75; // Set to 75vw
ctx.canvas.height = window.innerHeight * 0.5; // Set to 50vh

// Create the chart using native Chart.js
new Chart(ctx, {
    type: 'bar',
    data: dataBarCustomTooltip,
    options: optionsBarCustomTooltip,
});