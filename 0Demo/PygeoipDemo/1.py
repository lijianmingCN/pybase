import pygeoip
import socket

ip = socket.gethostbyname('www.iiopen.com')
print ip

query = pygeoip.GeoIP('GeoLiteCity.dat')
result = query.record_by_addr(ip)

print result