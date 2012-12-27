# -*- coding: utf-8 -*-

import web
import hashlib
import json
from . import account as account


app_jslink = '<script src="/static/sea-modules/seajs/1.3.0/sea-debug.js" data-main="/login/static/login-main"></script>'
jslink = '<script src="/login/static/login.js"></script>'


class login(object):
    def POST(self):
        postdata = web.input()
        username = postdata.username
        nickname = postdata.nickname
        password = postdata.password
        password = hashlib.sha1(password).hexdigest()

        if account.account_exists(username):
            result = account.login(username, password)
        else:
            result = account.register_account(username, password, nickname)
        return json.dumps(result)


class logout(object):
    def POST(self):
        return json.dumps(account.logout())


class userinfo(object):
    def GET(self):
        result = account.get_userinfo()
        return json.dumps(result)

    def POST(self):
        result = account.update_userinfo(web.input)
        return json.dumps(result)


urls = ["/login", login,
        "/logout", logout,
        "/userinfo", userinfo
        ]


web.app_extensions.is_login = account.is_login
web.app_extensions.get_userinfo = account.get_userinfo
