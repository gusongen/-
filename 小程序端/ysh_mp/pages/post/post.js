// pages/post/post.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tags:[
      {
        id:0,
        text:"交友",
        isSelected:false
      },{
        id:1,
        text:"征婚",
        isSelected:false
      },
      {
        id:2,
        text:"拼车",
        isSelected:false
      },
      {
        id:3,
        text:"巡课",
        isSelected:false
      },
      {
        id:4,
        text:"寻人",
        isSelected:false
      },
      {
        id:5,
        text:"吐槽",
        isSelected:false
      }
    ]
  },
  //点击tag
  select_tag(e){
    // console.log(e);
    const {id}=e.currentTarget.dataset;
    let chosen_obj=this.data.tags;
    chosen_obj[id].isSelected=!chosen_obj[id].isSelected;
    this.setData({
      tags:chosen_obj
    })
  },

  post_item(e){
    console.log("hello");
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})