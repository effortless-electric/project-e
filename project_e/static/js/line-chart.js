console.log("Ajax is working")
var endpoint = '/dealers/analytics/api/chart/data'
var defaultData = []
var labels = [];
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function(data){
            labels = data.labels
            defaultData = data.default
            setChart()
        
        },
        error: function(error_data){
        console.log("error")
        console.log(error_data)
        } 
    
    })

function setChart(){
    var ctx = document.getElementById('myChart');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Year view',
                        data: defaultData,
                        pointBackgroundColor: 'CornflowerBlue',
                        pointRadius: 4,
                        lineTension: 0,
                        backgroundColor: 'rgb(65,105,225, 0.3)',
                        pointHitRadius: 12
                        }],
                    
                    
                    
                    },
                    options: {
                        title:{
                            display: true,
                            text: 'Completed Jobs',
                            fontSize: 18
                        },
                        scales:{
                            yAxes: [{
                                ticks:{
                                    fontSize: 16,
                                    fontColor: 'black',
                                }
                            }],
                            xAxes:[{
                                ticks: {
                                    fontSize: 20,
                                    fontColor: 'black',
                                    fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif"
        
                                }
                            }]
                        }
                    }
                    
                })
}