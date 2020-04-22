var input = document.getElementById("txt");
input.onfocus = function () {  //鼠标点击输入框
    if (this.value == "请输入关键字...")
        this.value = "";
    this.style.color = "black"; //字体颜色为黑色
};
input.onblur = function () {
    if (this.value == "") {
        this.value = "请输入关键字...";
        this.style.color = "#F5F5F5";//字体变灰色
    }
};

submit = function () {
    var text = document.getElementById("txt").value;
    alert(text);
};

if (localStorage.length == 0)
// {alert("fuc");
    document.getElementById("show_id").innerHTML = "请登入";
else {

    (document.getElementById("realname")).innerHTML = localStorage.getItem("User");
}


var labels = (document.getElementsByClassName("choibox")[0]).getElementsByTagName("li");
for (var i in labels.length) {

    labels[i].innerHTML = labels[i].value;
    console.log(labels[i]);
}


a_tiezi = {"label": "", "pas": "", "title": "", "id": ""};

function choingthis(c) {
    a_tiezi.label = c.value;
    c.style.backgroundColor = "coral";
}

function get_a_tiezi() {
    a_tiezi.pas = $(".inputt")[0].value;
    a_tiezi.title = $(".inputt_tit")[0].value;
    a_tiezi.id = localStorage.getItem("User");


    alert("发布成功");
    window.location.reload();
}

var _tit = '<li><div class="item"><div class="head"><p>';
var tit_id = '</p></div><div class="user_a_detail"><div class="user"><img src="image/user_ico.jpeg" alt="用户头像"><p><span class="iddd">ID:</span>';
var id_pas = '</p><a class="foucus_burtton" >关注</a></div><div class="detail"><div class="text"><div class="text_left"><p>';
var pas_ = '</p></div><a class="read_buyyon">阅读全文</a></div><div class="opt1"><div class="opt1_left"><img src="image/like_u18.png" alt=""><img src="image/remark_u38.png" alt=""><img src="image/zhaunfa_u16.png" alt=""></div><div class="opt1_right"><!--标签设置--><a class="labell">日常</a><a class="labell">吐槽</a><a class="labell">学习</a></div></div></div></div></div></li>'

var start_pos = -1;//起始加载点
let page_now;
let all_page;
let per_page;
//TODO  发帖时间
let init_item = function (renew_type = 1) {
    //renew_type=1 全局刷新  =0 局部刷新
    // var ls = JSON.parse(localStorage.getItem("item"));
    alert("hhh2");
    if (renew_type == 1) {

        $.getJSON('/api/item/', function (data) {
            //先清屏
            alert("全局刷新");
            clear_item();
            add_to_html(data["content"]);
            //修改起始刷新位置
            start_pos = data["start_pos"]; //下次加载的位置
            page_now = data["page_now"]
            all_page = data["num_page"];
            per_page = data["per_page"];
            myScroll.refresh()

        });
    } else if (renew_type == 0) {
        alert("尝试局部刷新");
        $.getJSON('/api/item/?st=' + start_pos + "&pg=" + (page_now + 1) + "&itn=" + per_page, function (data) {
            alert("局部刷新");
            page_now = data["page_now"];
            add_to_html(data["content"]);
            myScroll.refresh()

        });
    }
};

let Refresh = function () {
    init_item(1);

};


let Load = function () {
    init_item(0);
};

// let Unable_load=function(){
//   let
// };

let clear_item = function () {
    $('#item_container ul').children().slice(1).html("");
};


let add_to_html = function (ls) {
    alert("添加到页面");
    if (ls != null) {
        let main_body = $("#item_container ul");
        for (let i = 0; i < ls.length; i++) {
            let per_item = ls[i];
            var item = _tit + per_item.i_title + tit_id + per_item.i_p_id + id_pas + per_item.i_content + pas_;
            main_body.append(item);
        }
    }
};

let refresh_option = {
    id: "item_container",//添加滚动检测范围
    pullDownAction: Refresh,
    pullUpAction: Load
};


$(function () {
    //加载完成就请求贴子
    init_item();
    //注册刷新器
    refresher.init(refresh_option);
});


