# coding:utf-8
import urllib

from django.db.models import Q
from functools import reduce
import re

from stock.models import AppStock
from utils.service import pagecal

stock_url = 'http://qt.gtimg.cn/q={}'


class StockService():
    def get_stocks(self, keyword, sorttype, sortno, pindex, psize):
        stocks = AppStock.objects.filter(isdisabled=True)

        psize = psize if psize <= 30 else 30
        # 关键字搜索
        if len(keyword) > 0:
            stocks = stocks.filter(Q(stockname__contains=keyword) | Q(pk_stock__contains=keyword))

        stocks = list(stocks)
        stockcodes = [s.pk_stock for s in stocks]
        stock_dtos = self.get_response(stockcodes)

        stock_dtos = stock_dtos[pagecal.start(pindex, psize): pagecal.end(pindex, psize)]

        reverse = sortno == 'desc'
        sort = ['lastprice', 'changeamount', 'changerate']
        # 排序
        sorttype = sorttype if sorttype in sort else 'lastprice'

        stock_dtos = sorted(stock_dtos, key=lambda s: s[sorttype], reverse=reverse)
        # stock_dtos = stock_dtos.sort(key=key, reverse=reverse)

        return stock_dtos

    # def get_response(self, stockname, stockcode, tradetype):
    #     '''发送网络请求获取股票数据'''
    #     response = urllib.request.urlopen(stock_url.format(tradetype + stockcode))
    #     # result=bytes.decode(response.read())
    #     result = response.read().decode('gbk')
    #
    #     stockinfo = result.split('~')
    #     stock_dto = {}
    #
    #     stock_dto['stockname'] = stockname
    #     stock_dto['stockcode'] = stockcode
    #     stock_dto['lastprice'] = convert_to_float(stockinfo[3])
    #     stock_dto['prevclose'] = convert_to_float(stockinfo[4])
    #     stock_dto['open'] = convert_to_float(stockinfo[5])
    #     stock_dto['changeamount'] = convert_to_float(stockinfo[31])
    #     stock_dto['changerate'] = convert_to_float(stockinfo[32])
    #     stock_dto['highest'] = convert_to_float(stockinfo[33])
    #     stock_dto['lowest'] = convert_to_float(stockinfo[34])
    #     stock_dto['tradingvolume'] = convert_to_float(stockinfo[36])
    #     stock_dto['changingover'] = convert_to_float(stockinfo[37])
    #     stock_dto['turnoverrate'] = convert_to_float(stockinfo[38])
    #     stock_dto['peratio'] = convert_to_float(stockinfo[39])
    #     stock_dto['circulatecap'] = convert_to_float(stockinfo[44])
    #     stock_dto['totalcap'] = convert_to_float(stockinfo[45])
    #     stock_dto['pbratio'] = convert_to_float(stockinfo[46])
    #
    #     return stock_dto 注释代码


    def get_response(self, stockcodes):
        '''发送网络请求获取股票数据'''

        stockdtos = []
        if len(stockcodes) == 0:
            return stockdtos

        stockcodes = reduce(lambda s1, s2: s1.lower() + ',' + s2.lower(), stockcodes)
        response = urllib.request.urlopen(stock_url.format(stockcodes))
        # result=bytes.decode(response.read())
        result = response.read().decode('gbk')

        stocks = result.split(';')
        if len(stocks) < 1: return stockdtos

        for item in stocks:
            stockinfo = item.split('~')
            if len(stockinfo) <= 1:
                continue

            match = re.match('\w+?_(\w+)=', stockinfo[0].strip('\n'))
            # stockcode = match.groups()[0]
            stockcode = match.group(1)
            stockdto = {}

            stockdto['stockname'] = stockinfo[1].replace(' ', '')
            stockdto['stockcode'] = stockcode
            stockdto['lastprice'] = convert_to_float(stockinfo[3])
            stockdto['prevclose'] = convert_to_float(stockinfo[4])
            stockdto['open'] = convert_to_float(stockinfo[5])
            stockdto['changeamount'] = convert_to_float(stockinfo[31])
            stockdto['changerate'] = convert_to_float(stockinfo[32])
            stockdto['highest'] = convert_to_float(stockinfo[33])
            stockdto['lowest'] = convert_to_float(stockinfo[34])
            stockdto['tradingvolume'] = convert_to_float(stockinfo[36])
            stockdto['changingover'] = convert_to_float(stockinfo[37])
            stockdto['turnoverrate'] = convert_to_float(stockinfo[38])
            stockdto['peratio'] = convert_to_float(stockinfo[39])
            stockdto['circulatecap'] = convert_to_float(stockinfo[44])
            stockdto['totalcap'] = convert_to_float(stockinfo[45])
            stockdto['pbratio'] = convert_to_float(stockinfo[46])
            stockdtos.append(stockdto)
        return stockdtos


def convert_to_float(source):
    return float(source) if source else 0
