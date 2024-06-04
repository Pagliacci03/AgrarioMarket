/**
 * Crea un gráfico de torta sin datos de momento
 */
Highcharts.chart('container_1', {
    chart: {
        type: 'pie',
        backgroundColor: 'lightgreen'
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




/**
 * Enlaza los datos del gráfico anterior con el total de productos por tipo de verdura y fruta
 * enviados desde una API en el servidor
 */
fetch("http://localhost:5000/get-stats-data-productos")
  .then((response) => response.json())
  .then((data) => {
    // Parsear datos entregados por la API
    let parsedData = data.map((item) => {
        return [
          item.name,
          item.count,
        ];
      });

    // Obtener el gráfico por el id
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container_1"
    );

    // Actualizar los datos del gráfico
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));