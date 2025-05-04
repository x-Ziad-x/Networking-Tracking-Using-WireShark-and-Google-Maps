import dpkt
import socket
import geoip2.database

#Initialize GeoIP2 Reader
gi = geoip2.database.Reader('GeoLite2-City.mmdb')

def retKML(dstip, srcip):
  try:
    dst = gi.city(dstip) #Lookup Destination IP
    src = gi.city('x.x.x.x') #Lookup Source IP (Replace x.x.x.x With Your Actual IP)

    #Extract The Coordinates
    dstlongitude = dst.location.longitude
    dstlatitude = dst.location.latitude
    srclongitude = src.location.longitude
    srclatitude = src.location.latitude

    #Create KML Placemark With A Line Between SRC and DST
    kml = (
        '<Placemark>\n'
        '<name>%s</name>\n'
        '<extrude>1</extrude>\n'
        '<tessellate>1</tessellate>\n'
        '<styleUrl>#transBluePoly</styleUrl>\n'
        '<LineString>\n'
        '<coordinates>%.6f,%.6f %.6f,%.6f</coordinates>\n'
        '</LineString>\n'
        '</Placemark>\n'
    ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
    return kml
  except:
    return ''

def plotIPs(pcap):
  kmlPts = ''
  for (ts, buf) in pcap: #Loop Through Packets in PCAP
    try:
      eth = dpkt.ethernet.Ethernet(buf) #Parse Ethernet Frame
      ip = eth.data #Get IP Layer
      #Convert Binary IP Addresses To Dotted-quad Strings
      src = socket.inet_ntoa(ip.src)
      dst = socket.inet_ntoa(ip.dst)
      #Generate KML Connection
      KML = retKML(dst, src)
      kmlPts += KML
    except:
      pass
  return kmlPts

def main():
  f = open('xxxx', 'rb')  #Replace xxx With Your .pcap File
  pcap = dpkt.pcap.Reader(f)

  # KML File To Import In Google Maps
  kmlheader = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
<Style id="transBluePoly">
<LineStyle>
<width>1.5</width>
<color>501400E6</color>
</LineStyle>
</Style>
'''
  kmlfooter = '</Document>\n</kml>\n'

  #Save Output In KML File
  with open('network_paths.kml', 'w') as kml_file:
    kml_file.write(kmlheader + plotIPs(pcap) + kmlfooter)
  print("KML file saved as 'network_paths.kml'")

main()