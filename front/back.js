// function callAPI() {
//     const ip_address = document.getElementById('ip_address').value;
//     const username = document.getElementById('username').value;
//     const password = document.getElementById('password').value;

//     // Make a POST request to the Flask API
//     fetch('http://127.0.0.1:5000/run_script', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json; charset=UTF-8',
//             //'Access-Control-Allow-Origin': '*',
//             //origins':'*'
//         },
//         body: JSON.stringify({
//             ip_address: ip_address,
//             user: username,
//             password: password
//         })
//     })
//     .then(response => response.text())
//     .then(data => {
//         // Display the API response
//         //document.getElementById('output').innerText = JSON.stringify(data, null, 2);
//         document.getElementById('output').innerText = data;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// function getCV() {
//     // const ip_address = document.getElementById('ip_address').value;
//     // const username = document.getElementById('username').value;
//     // const password = document.getElementById('password').value;

//     // Make a POST request to the Flask API
//     fetch('http://127.0.0.1:5000/csv', {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json; charset=UTF-8',
//             //'Access-Control-Allow-Origin': '*',
//             //origins':'*'
//         },
//         // body: JSON.stringify({
//         //     ip_address: ip_address,
//         //     user: username,
//         //     password: password
//         // })
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Display the API response
//         //document.getElementById('output').innerText = JSON.stringify(data, null, 2);
//         var data = [data];
//         function displayTable(data) {
//             var output = document.getElementById("output");
//             var table = output.createElement("table");
//             var thead = output.createElement("thead");
//             var tbody = output.createElement("tbody");

//             // Create table header
//             var headerRow = document.createElement("tr");
//             for (var key in data[0]) {
//                 var th = document.createElement("th");
//                 th.textContent = key;
//                 headerRow.appendChild(th);
//             }
//             thead.appendChild(headerRow);
//             table.appendChild(thead);

//             // Create table rows
//             data.forEach(function(rowData) {
//                 var tr = document.createElement("tr");
//                 for (var key in rowData) {
//                     var td = document.createElement("td");
//                     td.textContent = rowData[key];
//                     tr.appendChild(td);
//                 }
//                 tbody.appendChild(tr);
//             });
//             table.appendChild(tbody);

//             // Append table to output div
//             output.appendChild(table);
//         }
//         displayTable(data);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

function callAPI() {
    const ip_address = document.getElementById('ip_address').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Make a POST request to the Flask API
    fetch('http://127.0.0.1:5000/run_script', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify({
            ip_address: ip_address,
            user: username,
            password: password
        })
    })
    .then(response => response.text())
    .then(data => {
        // Display the API response
        document.getElementById('output').innerText = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function getDisk() {
    fetch('http://127.0.0.1:5000/getDisk', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
            'Access-Control-Allow-Origin': '*'
        }
    })
    .then(response => response.json())
    .then(data => {
        function displayTable(data) {
            var output = document.getElementById("output");
            output.innerHTML = ''; // Clear existing content
        
            var table = document.createElement("table");
            var thead = document.createElement("thead");
            var tbody = document.createElement("tbody");
        
            // Define the desired column order
            var columnOrder = ["Filesystem", "Type", "Size", "Used", "Available", "Use%", "Mounted on"];
        
            // Create table header
            var headerRow = document.createElement("tr");
            columnOrder.forEach(function(key) {
                var th = document.createElement("th");
                th.textContent = key;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);
        
            // Create table rows
            data.forEach(function(rowData) {
                var tr = document.createElement("tr");
                columnOrder.forEach(function(key) {
                    var td = document.createElement("td");
                    td.textContent = rowData[key] || ''; // Handle missing data
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);
        
            // Append table to output div
            output.appendChild(table);
        }
        
        displayTable(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
