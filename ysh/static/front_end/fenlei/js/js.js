
function chose_one(e) {
    var all_index=document.getElementsByClassName("index_box");
    for(var i=0;i<all_index.length;i++){
        all_index[i].style.backgroundColor="#94A5BF";
        all_index[i].style.top="0";
        all_index[i].style.height="50px";
    }
    e.style.backgroundColor="#EBF3FF";
    e.style.top="-10px";
    e.style.height="60px";
    document.getElementsByClassName("item_wrap")[0].innerHTML="";
    init_item(e.innerHTML);
}


var ls1=JSON.parse(localStorage.getItem("item"));

var _tit='<div class="item"><div class="head"><p>';
var tit_id='</p></div><div class="user_a_detail"><div class="user"><div class="user_ico_box"><img src="image/user_ico.jpeg" alt="用户头像"></div><p><span >ID:</span>';
var id_pas='</p><a class="foucus_burtton">关注</a></div><div class="detail"><div class="text"><div class="text_left"><p class="zhenwen">';
var pas_='</p></div><a class="read_buyyon">阅读全文</a></div><div class="opt1"><div class="opt1_left"><img src="image/like_u18.png" alt=""><img src="image/remark_u38.png" alt=""><img src="image/zhaunfa_u16.png" alt=""></div><div class="opt1_right"><!--标签设置--><a class="labell">日常</a><a class="labell">吐槽</a><a class="labell">学习</a></div></div></div></div></div>';


function init_item(chlab) {
    ls=[];
    for(var i=0;i<ls1.length;i++){
        if(ls1[i].label==chlab){
            ls.push(ls1[i]);
        }
    }
    // alert(chlab+" 标签的帖子数量为  "+ls.length);
    if(ls!=null){
        // var pageSize=10;
        var main_body=document.getElementsByClassName("item_wrap")[0];
        for(var i=ls.length-1;i>=0;i--){
            var per_item=ls[i];
            var item=_tit+per_item.title+tit_id+per_item.id+id_pas+per_item.pas+pas_;
            main_body.innerHTML+=item;
        }
    }
}

