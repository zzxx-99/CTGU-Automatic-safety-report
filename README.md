# auto_yiqing_ctgu

**CTGU疫情自动报平安**

**增加qq推送消息**

## 使用方式

- Fork我的项目,然后去项目的Settings里添加Secrets
- name填users,内容填一个二维数组,就是学号及密码以及消息key(没有也要填个空格)
- 需要找到免费的代理https://ip.jiangxianli.com/ （github ip好像被封了）

> [['2019112404', '666666', '','http://116.117.134.134:81']]

- 添加多个人格式如下

```
[['2019112404', '666666', '49bdbxxxxxxxxxxxxxxx2','http://116.117.134.134:81'], 
 ['2019112405', '666666', '49bdbxxxxxxxxxxxxxxx2','http://116.117.134.134:81'], 
 ['2019112406', '666666', '49bdbxxxxxxxxxxxxxxx2','http://116.117.134.134:81'],
 ['2019112407', '666666', '49bdbxxxxxxxxxxxxxxx2','http://116.117.134.134:81']]
```

- 添加完点击action 看着绿色的选项一直确认点的去就完成了

## 说明：

1. Qmsg，Api的注册

2. 1. https://qmsg.zendee.cn/index.html
   2. 登录控制台
   3. 获取key
   4. 控制台-我的-qq号码  里面添加你的qq
   5. 添加msg酱为好友
   6. 记住api回来填写即可

3. 启动方式： 

4. 1. 默认启动:  8/20点明天默认启动两次防止没报上
   2. 追加启动：手动在action界面点收藏(已经点过了就取消再次点击)
   3. 更新代码： 会每次update后也会启动一次
   
参考： https://github.com/szh1213/auto_yiqing_ctgu
参考： https://github.com/Baymax-Zhu/yiqing.ctgu
改进为能直接使用
