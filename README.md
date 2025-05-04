# Network Traffic Visualizer

## Project Description
A cybersecurity analysis tool that:
- Processes Wireshark packet capture (PCAP) files
- Maps network connections geographically using IP geolocation
- Generates KML files for visualization in Google Maps/Earth
- Provides insights into network traffic patterns

## Installation Guide

### Prerequisites
- Python 3.8+
- Wireshark (for packet capture)

### Setup and Run
1. Install required packages:
   pip install dpkt geoip2

2. Download GeoLite2 database:
   https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
  
3. Run the visualizer:
   Just run the code in your IDE and go to Google My Maps (https://www.google.com/maps/d/), Click "Create New Map" → "Import", Upload your .kml file

## Features
- Packet Analysis:
  - Reads standard Wireshark PCAP format
  - Extracts source/destination IP pairs

- Geolocation:
  - Converts IPs to physical coordinates
  - Uses MaxMind's GeoLite2 city database

- Visualization:
  - Generates standards-compliant KML files
  - Customizable path styling
  - Google Maps/Earth compatible

## File Format Specifications
### Input Requirements
- PCAP files captured with Wireshark/tcpdump
- Contains IPv4 traffic (TCP/UDP/ICMP)

### Output Specifications
- KML 2.2 format
- Contains:
  - Source/Destination coordinates
  - Connection paths
  
## Troubleshooting
### No Paths Appear
- Verify PCAP contains public IP traffic
- Check KML validity at https://kmlvalidator.com

### GeoIP Lookup Fails
- Ensure GeoLite2 database is current
- Register for free license at MaxMind

## Credits
Developed by Ziad
