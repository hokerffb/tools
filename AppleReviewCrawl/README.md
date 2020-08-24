## AppleReviewCrawl

苹果应用商店评论抓取工具

```
arcgo -id <appid>
```



## 协议

评论抓取地址：

```
https://itunes.apple.com/rss/customerreviews/page={index}/id={appid}/sortby=mostrecent/json?l=en&&cc=cn
```

结构
```
feed
    |__link:[{attributes:{rel:"alternate/self/first/last/previous/next",type:"",href:""}}] 
    |__updated:{label:""} 更新时间
    |__entry: [{author/name/label:"名字",title/label:"标题",content/label:"评论内容"}]
```

* link：用于索引页面，如果数据为空，则没有entry字段
* entry：评论内容
* updated：rss的更新时间，用于判断是否需要抓取