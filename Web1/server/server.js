const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors());
var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"
app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress +
':' + iPortaTcp));

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
    
app.get('/formRegistrazione', (req, res) => {
console.log("Mi hai chiesto la form di registrazione");
res.sendFile("formSemplice.html", { root: './htdoc' });
});

app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname);
    res.send("<html>Buona serata " + req.query.fname + " " + req.query.fcognome + "</html>");
    });

app.get('/sendFile', (req, res) => {
    console.log("Mi hai chiesto la form ");
    res.sendFile("sendFile.html", {root: '/htdoc'});
    });

app.post('/mansendfile', (req, res) => {
    console.log(req.body.password)
    pass_ricevuta = req.body.password;
    if (pass_ricevuta == 'paperino')
        res.send("<html> Bravo "+ req.body.email + "<br> Sono pronto a ricevere il file!</html>")
    else
        res.send("<html> Buona sera" + req.body.fname + "</html>")
});