#!/usr/bin/python env
#coding: utf8

from utils import apiutil

AppID = '1106858595'
AppKey = 'bNUNgOpY6AeeJjFu'

ai_obj = apiutil.AiPlat(AppID, AppKey)
type = 0
str_text = '今天天气怎么样'
rsp = ai_obj.getNlpTextTrans(str_text, type)
if rsp['ret'] == 0:
    print rsp
