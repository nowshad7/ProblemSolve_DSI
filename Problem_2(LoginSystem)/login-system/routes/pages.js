const express = require('express');
const router = express.Router();

router.get("/", (req, res)=>{
    res.render("index");
});

router.get("/success", (req, res)=>{
    res.render("success");
});

router.get("/fail", (req, res)=>{
    res.render("fail");
});

module.exports = router;