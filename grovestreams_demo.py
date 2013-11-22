import time
from time import sleep
from datetime import datetime
from simplejson import encoder as jsonEncoder
import httplib
import StringIO
import gzip

def compressBuf(buf):
    zbuf = StringIO.StringIO()
    zfile = gzip.GzipFile(mode = 'wb',  fileobj = zbuf, compresslevel = 9)
    zfile.write(buf)
    zfile.close()
    return zbuf.getvalue()

if __name__ == '__main__':
    org = "5d1b9b08-d67f-3510-9b0c-33cb6b84bd8c"; #Change this!!
    api_key = "9b614b5f-8dc0-3fae-aa12-98ffbb9a02af"; #Change this!!
    
    component_id = "myOrg.myComponent";
    stream_id = "myOrg.myComponent.helloWorld";
    
    while True:

        #assemble feed and convert it to a JSON string
        feed = {};
        feed['feed'] = {}
        feed['feed']['component'] = []
        
        comp = {}
        comp['stream'] = []
        comp['componentId'] = component_id
        feed['feed']['component'].append(comp)
        
        stream = {}
        stream['streamId'] = stream_id
        stream['time'] = [] 
        stream['data'] = []
        comp['stream'].append(stream)
        
        #get the millis since epoch
        now = datetime.now()
        nowEpoch = int(time.mktime(now.timetuple())) * 1000
        
        stream['time'].append(nowEpoch)
        stream['data'].append("Hello World. The current time is: " + str(now))
        
        encoder = jsonEncoder.JSONEncoder()
        json = encoder.encode(feed);
        
        #Upload the feed
        try:      
            conn = httplib.HTTPConnection('www.grovestreams.com')
            
            url = '/api/feed?&org=%s&api_key=%s' % (org, api_key)
            
            compress = True
            if compress:
                body = compressBuf(json)
                headers = {"Content-type": "application/json", "Content-Encoding" : "gzip"}
            else:
                body = json
                headers = {"Content-type": "application/json", "charset":"UTF-8"}
            
            conn.request("PUT", url, body, headers)
                    
            response = conn.getresponse()
            status = response.status
                    
            if status != 200 and status != 201:
                try:
                    if (response.reason != None):
                        print('reason: ' + response.reason + ' body: ' + response.read())
                    else:
                        print('body: ' + response.read())
                except Exception:
                    print('HTTP Fail Status: %d' % (status) )
                
        except Exception as e:
            print('HTTP Send Error: ' + str(e))
        
        finally:
            if conn != None:
                conn.close()

        sleep(10)  
 
    # quit
    exit(0)
