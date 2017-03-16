#coding:utf-8

from rest_framework.response import Response
from functools import wraps
from utils.response import retcode, retmsg


def  request_validate(serializer):
    '''请求参数校验'''

    def decorator(func):
        @wraps(func)
        def in_decorator(self, request, *args, **kwargs):
            # 通用处理
            params=request.GET if request.method=='GET' else request.POST
            command = serializer(data=params)
            if not command.is_valid():
                retmsg['recode'] = retcode['error']
                retmsg['errmsg'] = command.errors
                return Response(retmsg)
            kwargs['command'] = command.validated_data
            return func(self, request, *args, **kwargs)
        return in_decorator
    return decorator