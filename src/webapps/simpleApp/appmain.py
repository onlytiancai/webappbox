# -*- coding: utf-8 -*-

import os
import web

curdir = os.path.dirname(__file__)

app_desc = "世界末日倒计时"
app_jslink = '<script src="/simpleApp/static/require.js" data-main="/simpleApp/static/main"></script>'

from . import endoftheworld


class showmetime(object):
    def GET(self):
        return endoftheworld.countdown()


class userinfo():
    def GET(self):
        if web.is_login():
            return web.get_userinfo()
        else:
            return 'you not login'


urls = ["/showmetime", showmetime,
        "/userinfo", userinfo
        ]
