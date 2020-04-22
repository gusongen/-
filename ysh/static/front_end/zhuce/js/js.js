var hhh={ "id":"ID","name":"姓名","pwd":"密码","tele":"电话","qq":"QQ"}

function wtf(str,str2) {
    var id_ip=document.getElementById(str);
    id_ip.value=str2;
        id_ip.onfocus = function ()
        {
            if (this.value==str2)
                this.value="";
            this.style.color="black";
        };
        id_ip.onblur=function () {
            if(this.value==""){
            this.value=str2;
            this.style.color ="#E2E2E2" ;//字体变灰色
                }
            }

}

for(var key in hhh){

    wtf(key,hhh[key]);
}


// 初始化数据库
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
    if(!UserList) UserList=[
    ];
    fg=1;
    var ID=(document.getElementById('id')).value;
    for(var i in UserList ){
        if(ID===UserList[i].id){
            fg=0;
            break;
        }
    }
    //添加注册用户
    if(fg){
       var id_val=document.getElementById("id").value;
       var name_val=document.getElementById("name").value;
        var pwd_val=document.getElementById("pwd").value;
        var tele_val=document.getElementById("tele").value;
        var qq_val=document.getElementById("qq").value;
        let new_user={"id":id_val,"name":name_val,"pwd":pwd_val,"tele":tele_val,"qq":qq_val};
        UserList.push(new_user);

        localStorage.setItem("temp",JSON.stringify(UserList));
        // JSON.stringify(new_user)
        // var blob = new Blob([UserList], {type: "text/plain;charset=utf-8"});
        // saveAs(blob, "../database/User.json");
        alert("注册成功");
        window.open("../dengru/dengru.html","_self");
    }
    else alert("注册失败");

}




