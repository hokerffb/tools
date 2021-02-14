# 配置文件

## Linux: Ubuntu 18.04/WSL/Debian 10

|配置文件|路径|
:-|:-|
| vimrc.local | /etc/ |
| proxychains.conf | /etc/ |
| gitconfig | ~/.gitconfig |
| user-dirs.dirs | ~/.config |
| interfaces.*dh*cp* | /etc/network/interfaces |

## MacOS 10.15

|配置文件|路径|
:-|:-|
|.zshrc|~/|
|proxychains.conf|/usr/local/etc/|

## FreeBSD 13

|配置文件|路径|
:-|:-|
|FreeBSD13ustc.conf|/usr/local/etc/pkg/repos/FreeBSD.conf|

## VSCode

|配置文件|说明|
:-|:-|
|markdown.css|Markdown: Styles，需要先将文件放到项目目录下或者https地址上|
|parser.js|~/.mume，自定义MPE的markdown渲染规则|
|style.less|~/.mume，自定义MPE的markdown样式|

```
vscode command:
Markdown Preview Enhanced: Extend Parser
Markdown Preview Enhanced: Customize Css
```

# 参考文档

- [扩展 Markdown Parser](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/extend-parser) ([中文](https://www.bookstack.cn/read/mpe/zh-cn-extend-parser.md))
- [自定义 CSS](https://www.bookstack.cn/read/mpe/zh-cn-customize-css.md)
