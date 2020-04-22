var idd=document.getElementById("ID_ipu");
var id_ip=idd.getElementsByTagName("input")[0];
id_ip.onfocus = function () {
    if (this.value=="请输入ID或用户名")
        this.value="";
    this.style.color="black";

};
id_ip.onblur=function () {
    if(this.value==""){
        this.value="请输入ID或用户名";
        this.style.color ="#E2E2E2" ;//字体变灰色
    }
};

var pwd=document.getElementById("pwd_ipu");
var pwd_ip=pwd.getElementsByTagName("input")[0];
pwd_ip.onfocus = function () {
    if (this.value=="请输入密码")
        this.value="";
    this.style.color="black";

};
pwd_ip.onblur=function () {
    if(this.value==""){
        this.value="请输入密码";
        this.style.color ="#E2E2E2" ;//字体变灰色
    }
};




//初始化数据库
hhh=function () {
    // $.ajax({
    //     url: '../database/User.json',
    //     async: false,
    //     success: function (data) {
    //         UserList = data;
    //         // alert("database has been init");
    //     }
    // });
    UserList=JSON.parse(localStorage.getItem("temp"));
    var user_id=document.getElementById("ID").value;
    var user_pwd=document.getElementById("pwd").value;
    // alert(user_id+"__"+user_pwd);
    var fg=0;
        for(var i in UserList ){
            if(user_pwd===UserList[i].pwd&&(user_id===UserList[i].name||user_id===UserList[i].id)){
                fg=1;
                break;
            }
        }
        if (fg) {
            alert("登入成功");
            localStorage.setItem("User",user_id);
        window.open("../zhuye/zhuye.html","_self");}
        else alert("登入失败");
}































