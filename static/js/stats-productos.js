Highcharts.chart('container', {
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Total de productos por tipo de fruta y verdura'
    },
    plotOptions: {
        pie: {
            dataLabels: {
                enabled: true,
                format: '{point.name}: {point.y}'
            }
        }
    },
    series: [{
        name: 'FrutasVerduras',
        data: []
    }]
});




fetch("http://localhost:5000/get-stats-data-productos")
  .then((response) => response.json())
  .then((data) => {
    let parsedData = data.map((item) => {
        return [
          item.name,
          item.count,
        ];
      });

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));