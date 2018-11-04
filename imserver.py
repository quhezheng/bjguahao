#!/usr/bin/env python
#-*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
from tornado.escape import json_decode

im_code = ''

class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        global im_code    
        im_code = ''
        #print(self.request.body)
        data=json_decode(self.request.body)
        content=data['content']
        #content = self.get_argument("content")
        nTitle = content.find('预约挂号')
        if nTitle < 0 :
            print(content +'中没有找到　预约挂号　关键字')
            return
            
        nDigitStart = content.find('【', nTitle, -1)
        if nDigitStart < 0 :
            print(content  +'中没有找到【　关键字')
            return
            
        nDigitStart=nDigitStart+1 
        code = content[nDigitStart:nDigitStart+6]
        if not code.isdigit():
            print(content  +'中没有找到6位数字')
            return
            
        im_code = code
        #print('找到验证码:'+code)
        tornado.ioloop.IOLoop.instance().stop()
    
class IMServer:
    def start(self):
        app = tornado.web.Application([(r"/", IndexHandler)])
        app.listen(80)
        tornado.ioloop.IOLoop.current().start()
        
        
        
if __name__ == "__main__":
    server = IMServer()
    server.start()
    print('找到验证码:'+im_code)



