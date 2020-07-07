# 步骤

1. 循环获取分页列表
```buildoutcfg
https://blog.csdn.net/nickname/article/list/1
https://blog.csdn.net/nickname/article/list/2
...
最后一页会出现"空空如也"
```

2. 获取博客内容

```buildoutcfg
<div class="article-item-box csdn-tracking-statistics" data-articleid="76034032">
        <h4 class="">
        <a href="https://blog.csdn.net/ffb/article/details/76034032" target="_blank">
        <span class="article-type type-1 float-none">原创</span>        Excel无法vlookup事件              </a> 
    </h4>
    <p class="content">
      <a href="https://blog.csdn.net/ffb/article/details/76034032" target="_blank">
        数据明明就在那里，却为什么vlookup不到呢？      </a>
    </p>
    <div class="info-box d-flex align-content-center">
    <p>
        <span class="date">
        2017-07-24 18:20:00</span>
                <span class="read-num"><img src="https://csdnimg.cn/release/phoenix/template/new_img/readCountWhite.png" alt="">1005</span>
                <span class="read-num"><img src="https://csdnimg.cn/release/phoenix/template/new_img/commentCountWhite.png" alt="">0</span>
      </p>
    </div>
</div>
```

多条评论
```buildoutcfg
<div class="comment-list-box" style="max-height: none;">
<ul class="comment-list">
<li class="comment-line-box d-flex" data-commentid="2363171" data-replyname="wukongwu">
<a target="_blank" href="https://me.csdn.net/wukongwu"><img src="https://profile.csdnimg.cn/5/E/0/3_wukongwu" username="wukongwu" alt="wukongwu" class="avatar"></a><div class="right-box "><div class="new-info-box clearfix">
<a target="_blank" href="https://me.csdn.net/wukongwu">
<span class="name ">wukongwu</span></a><span class="colon">:</span>
<span class="floor-num"></span><span class="new-comment">哥们确实不行啊   我就是照你的说法做的 不好用 我在vbs里运行 报错</span>
<span class="date" title="2012-09-05 14:10:25">8年前</span><span class="new-opt-box new-opt-box-bg"><a class="btn  btn-report" data-type="report">举报</a>
<span class="btn-bar"></span><a class="btn  btn-reply" data-type="reply">
<img src="https://blog.csdn.net/static_files/template/new_img/replyOtherComment.png" title="回复">回复</a>
<a class="btn  btn-heart" data-type="heart"><div class="comment-like " data-commentid="2363171">
<img class="comment-like-img unclickImg" src="https://blog.csdn.net/static_files/template/new_img/commentUnHeart.png" title="点赞">
<img class="comment-like-img comment-like-img-hover" style="display:none" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞">
<img class="comment-like-img clickedImg" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><span></span></div></a></span></div>
<div class="comment-like " data-commentid="2363171"><img class="comment-like-img unclickImg" src="https://blog.csdn.net/static_files/template/new_img/commentUnHeart.png" title="点赞"><img class="comment-like-img comment-like-img-hover" style="display:none" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><img class="comment-like-img clickedImg" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><span></span></div></div></li></ul><ul class="comment-list"><li class="comment-line-box d-flex" data-commentid="1252352" data-replyname="ffb">      <a target="_blank" href="https://me.csdn.net/ffb"><img src="https://profile.csdnimg.cn/1/7/4/3_ffb" username="ffb" alt="ffb" class="avatar"></a>        <div class="right-box ">          <div class="new-info-box clearfix">            <a target="_blank" href="https://me.csdn.net/ffb"><span class="name ">ffb<img class="is_bloger" src="https://blog.csdn.net/static_files/static_blog/images/bloger@2x.png" "=""></span></a><span class="colon">:</span><span class="floor-num"></span><span class="new-comment">怎么骗人，我都是试验通过才发的贴</span><span class="date" title="2010-01-29 11:18:07">10年前</span><span class="new-opt-box new-opt-box-bg"><a class="btn  btn-report" data-type="report">举报</a><span class="btn-bar"></span><a class="btn  btn-reply" data-type="reply"><img src="https://blog.csdn.net/static_files/template/new_img/replyOtherComment.png" title="回复">回复</a><a class="btn  btn-heart" data-type="heart"><div class="comment-like " data-commentid="1252352"><img class="comment-like-img unclickImg" src="https://blog.csdn.net/static_files/template/new_img/commentUnHeart.png" title="点赞"><img class="comment-like-img comment-like-img-hover" style="display:none" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><img class="comment-like-img clickedImg" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><span></span></div></a></span></div><div class="comment-like " data-commentid="1252352"><img class="comment-like-img unclickImg" src="https://blog.csdn.net/static_files/template/new_img/commentUnHeart.png" title="点赞"><img class="comment-like-img comment-like-img-hover" style="display:none" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><img class="comment-like-img clickedImg" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><span></span></div></div></li></ul><ul class="comment-list"><li class="comment-line-box d-flex" data-commentid="1233719" data-replyname="newbeginning_bjl">      <a target="_blank" href="https://me.csdn.net/newbeginning_bjl"><img src="https://profile.csdnimg.cn/3/4/4/3_newbeginning_bjl" username="newbeginning_bjl" alt="newbeginning_bjl" class="avatar"></a>        <div class="right-box ">          <div class="new-info-box clearfix">            <a target="_blank" href="https://me.csdn.net/newbeginning_bjl"><span class="name ">BB_OA</span></a><span class="colon">:</span><span class="floor-num"></span><span class="new-comment">骗人的，都不行的</span><span class="date" title="2010-01-19 11:33:34">10年前</span><span class="new-opt-box new-opt-box-bg"><a class="btn  btn-report" data-type="report">举报</a><span class="btn-bar"></span><a class="btn  btn-reply" data-type="reply"><img src="https://blog.csdn.net/static_files/template/new_img/replyOtherComment.png" title="回复">回复</a><a class="btn  btn-heart" data-type="heart"><div class="comment-like " data-commentid="1233719"><img class="comment-like-img unclickImg" src="https://blog.csdn.net/static_files/template/new_img/commentUnHeart.png" title="点赞"><img class="comment-like-img comment-like-img-hover" style="display:none" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><img class="comment-like-img clickedImg" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><span></span></div></a></span></div><div class="comment-like " data-commentid="1233719"><img class="comment-like-img unclickImg" src="https://blog.csdn.net/static_files/template/new_img/commentUnHeart.png" title="点赞"><img class="comment-like-img comment-like-img-hover" style="display:none" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><img class="comment-like-img clickedImg" src="https://blog.csdn.net/static_files/template/new_img/commentActiveHeart.png" title="点赞"><span>
</span></div></div></li></ul></div>
```