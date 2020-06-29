# Ezviz to kml

萤石云EZVIZ行车记录仪的轨迹txt文件转换为Google Earth可用的kml文件

# 文件格式

输入：txt文件，内部为不闭合的json字符串

```
{uLatitud:10671186,uLongitude:35240374,uSpeed:3448424},{uLatitud:10671217,uLongitude:35240359,uSpeed:3781784},\0\0...
```

输出：kml文件，格式：

```
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>name.kml</name>
	<Placemark>
		<name>name</name>
		<LineString>
			<tessellate>1</tessellate>
			<coordinates>
				98.4955892273933,29.65362205776255,0 98.49075281773213,29.66370723895003,0 
			</coordinates>
		</LineString>
	</Placemark>
</Document>
</kml>
```

# 转换方法

逗号拆分，json解析，忽略全0部分。
kml文件中路径节点数据不能超过65535，否则会无法显示。