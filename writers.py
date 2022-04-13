import nsq
import tornado.ioloop
import json

f = open('data.json')
d = json.load(f)
print(type(d))
f.close()

def check_data(d):
    return d["HN"] == "1234" and "12" in d["Test code"]
    
def pub_message():
    writer.pub('json_test', str(d).encode(), finish_pub)

def finish_pub(conn, data):
    print(data)

if check_data(d) is True:
    writer = nsq.Writer(['127.0.0.1:4150'])
    tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
    nsq.run()