const mysql = require("mysql");

const db = mysql.createConnection({
    host: process.env.HOST,
    user: process.env.USER,
    password: process.env.PASSWORD,
    database: process.env.DATABASE
});

db.connect( (error) =>{
    if(error){
        console.log(error)
    }
    else{
        console.log("mysql connected...")
    }
})


exports.login = async (req, res) => {
    try {
        var email = req.body.email;
        var password = req.body.password;

        db.query("SELECT * FROM user WHERE email = ? AND password = ?", [email, password], (err, results)=>{
            if(!err){
                if(results.length>0){
                    res.render('success');
                }
                else{
                    res.render('fail');
                }
            }
            else{
                console.log(err);
            }
        })


    } catch (error) {
        console.log(error);
    }

}

