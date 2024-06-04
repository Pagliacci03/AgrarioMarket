Highcharts.chart('container_2', {
    chart: {
        type: 'pie',
        backgroundColor: 'lightgreen'
    },
    title: {
        text: 'Total de pedidos por comuna'
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
        name: 'Comunas',
        data: []
    }]
});




fetch("http://localhost:5000/get-stats-data-pedidos")
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
      (chart) => chart && chart.renderTo.id === "container_2"
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