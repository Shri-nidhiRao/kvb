const http = require('http');

const data = JSON.stringify({
    from_name: 'Test Node',
    reply_to: 'zainabhullur2003@gmail.com',
    phone: '1234567890',
    city: 'Test City',
    state: 'Test State',
    message: 'This is a test from a script'
});

const options = {
    hostname: 'localhost',
    port: 5000,
    path: '/send-email',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': data.length
    }
};

const req = http.request(options, (res) => {
    console.log(`Status: ${res.statusCode}`);
    res.on('data', (d) => {
        process.stdout.write(d);
    });
});

req.on('error', (error) => {
    console.error('Error:', error);
});

req.write(data);
req.end();
