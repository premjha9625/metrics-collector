function callAPI() {
    const ip_address = document.getElementById('ip_address').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Make a POST request to the Flask API
    fetch('http://127.0.0.1:5000/run_script', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
            //'Access-Control-Allow-Origin': '*',
            //origins':'*'
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
        //document.getElementById('output').innerText = JSON.stringify(data, null, 2);
        document.getElementById('output').innerText = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}