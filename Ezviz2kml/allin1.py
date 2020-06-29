#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#coding=utf8

import sys
import json
import os

out_start = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>2020-06-21西藏日环食</name>
	<open>1</open>
	<description><![CDATA[2020-06-21西藏日环食]]></description>
	<Style id="s_ylw-pushpin">
		<IconStyle>
			<scale>1.1</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00ffff</color>
			<width>5</width>
		</LineStyle>
	</Style>
	<Style id="s_ylw-pushpin_hl">
		<IconStyle>
			<scale>1.3</scale>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
			</Icon>
			<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
		</IconStyle>
		<LineStyle>
			<color>ff00ffff</color>
			<width>5</width>
		</LineStyle>
	</Style>
	<StyleMap id="m_ylw-pushpin">
		<Pair>
			<key>normal</key>
			<styleUrl>#s_ylw-pushpin</styleUrl>
		</Pair>
		<Pair>
			<key>highlight</key>
			<styleUrl>#s_ylw-pushpin_hl</styleUrl>
		</Pair>
	</StyleMap>
	<Folder id="TbuluTrackFolder">
		<name>轨迹</name>
		<open>1</open>
        <Placemark>
            <styleUrl>#m_ylw-pushpin</styleUrl>
            <gx:Track>
"""

out_end = """
			</gx:Track>
		</Placemark>
	</Folder>
</Document>
</kml>
"""

out_kml = ""

skip = 0

def main():
  global out_kml
  for root, dirs, files in os.walk("./data/"):
    for f in files:
      sourceFile = os.path.join(root, f)
      kml = toKml(sourceFile)
      out_kml += kml
  with open("output/20200621.kml", 'w') as fw:
    fw.write(out_start + out_kml + out_end)

def toKml(sourceFile):
  global skip
  kml = ""
  source = ""
  with open(sourceFile, 'r') as f:
    source = f.read()
  markPoint = source.split("},")
  for itor in markPoint:
    if itor[0] == '\0':
      break
    itor += '}'
    itor = itor.replace("uLatitud", '"uLatitud"');
    itor = itor.replace("uLongitude", '"uLongitude"');
    itor = itor.replace("uSpeed", '"uSpeed"');
    mark = json.loads(itor)
    if mark["uLongitude"] == 0 or mark["uLongitude"] ==0:
      continue
    else:
      kml += "<gx:coord>{0} {1}</gx:coord>\n".format(mark["uLongitude"] / 360000.0, mark["uLatitud"] / 360000.0)

  return kml

if __name__ == "__main__":
  main()