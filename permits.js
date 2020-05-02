// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received                                                              
function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function get_graphs() {
  ajaxGetRequest("/scatter_plot", showScatter);

  ajaxGetRequest("/pie_chart", showPie);

  ajaxGetRequest("/line_graph", showLine);
}

function showScatter(response) {                                                                                                              
    let scatter_data = JSON.parse(response); 
    let data = 
        [{
            x: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            y: scatter_data,
            mode: 'markers',
            type: 'scatter'
        }];

    let layout = 
        {
            title: 'Tows by Day of the Month',
            xaxis: {title: 'Day of the Month'},
            yaxis: {title: '# Tows'}
        };

Plotly.newPlot('scatter_plot', data, layout);
}

function showPie(response2) {                                                                                                               
    let pie_data = JSON.parse(response2);
    let data = 
        [{
            values: pie_data,
            labels: ["District A","District B","District C","District D","District E"],
            type: 'pie'
        }];

    let layout = {title: 'Tows by District'};
Plotly.newPlot('pie_chart', data, layout);
}                                                                             

// function showLine(response3){
// 	let data = []
//   let line_data = JSON.parse(response3)
//   let index = 0
//   let trace_names = ['ILLEGAL VEHICLE', 'ACCIDENT', 'ABANDONED VEHICLE', 'STOLEN VEHICLE', 'ILLEGALLY PARKED', 'IMPOUNDED', 'GONE ON ARRIVAL']
// 	for(let i of line_data){
//     let trace = 
//         {
//           x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
//           y: i,
//           type : 'scatter'
//         };
//     data.push(trace);
//   }
//     let layout = 
//         {
//             title: '# Tows by Month and Description',
//             xaxis: {title: 'Month'},
//             yaxis: {title: '# Tows'}
//         };

// Plotly.newPlot('line_graph', data, layout);
// }

function showLine(response3){
  let line_data = JSON.parse(response3)
  let trace_names = ['ILLEGAL VEHICLE', 'ACCIDENT', 'ABANDONED VEHICLE', 'STOLEN VEHICLE', 'ILLEGALLY PARKED', 'IMPOUNDED', 'GONE ON ARRIVAL']
    let trace0 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[0],
          type : 'scatter',
          name : trace_names[0]
        };

    let trace1 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[1],
          type : 'scatter',
          name : trace_names[1]
        };

    let trace2 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[2],
          type : 'scatter',
          name : trace_names[2]
        };

    let trace3 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[3],
          type : 'scatter',
          name : trace_names[3]
        };

    let trace4 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[4],
          type : 'scatter',
          name : trace_names[4]
        };

    let trace5 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[5],
          type : 'scatter',
          name : trace_names[5]
        };

    let trace6 = 
        {
          x: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
          y: line_data[6],
          type : 'scatter',
          name : trace_names[6]
        };

    let layout = 
        {
            title: '# Tows by Month and Description',
            xaxis: {title: 'Month'},
            yaxis: {title: '# Tows'}
        };

    let data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6];

Plotly.newPlot('line_graph', data, layout);
}

