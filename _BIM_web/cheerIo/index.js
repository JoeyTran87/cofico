//https://www.youtube.com/watch?v=RyH5v7QRm7o
var express = require("express");
var app = express();

app.use(express.static("pulic"));
app.set("view engine","ejs");
app.set("views","./views");

app.listen(4000);


var request = require("request");
var cheerio = require("cheerio");


app.get("/",function(req,res){
    request("http://vnexpress.net",function(error, response, body){
        if (error){
            console.log(error);
            res.render("trangchu",{html: "Có lỗi xảy ra"});
        }
        else{
            //console.log(body);
            $ = cheerio.load(body);
            var ds = $(body).find("h1.title-detail"); // css class = . id = #
            console.log(ds);
            ds.each(function(e,i){
                console.log( $(this).text() );
            }),

            res.render("trangchu",{html: body});
        }
    })
    
});
//contrl + c ngắt ket noi server