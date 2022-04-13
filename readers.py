import nsq

def handler(message):
    print(message.body.decode())
    return True

nsq.Reader(message_handler=handler,
    lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic='json_test', channel='asdf', lookupd_poll_interval=15)
nsq.run()