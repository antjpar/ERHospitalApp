var app = require('express')();
const morgan = require('morgan');

app.use(morgan('combined'));

var http = require('http').createServer(app);
var io = require('socket.io')(http);

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/send-sms', (req,res) => {
    let to=req.query.to;
    let msg=req.query.msg;
    const username = 'YOUR_SIPGATE_EMAIL';
    const password = 'YOUR_SIPGATE_PASSWORD';
    const recipient = 'RECIPIENT_PHONE_NUMBER';
    const message = 'YOUR_MESSAGE';

    const smsId = 'YOUR_SIPGATE_SMS_EXTENSION';
    return "Hello world!";

});

http.listen(80, () => {
    console.log('listening on *:80');
});
