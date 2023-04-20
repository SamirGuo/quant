import tushare as ts

ts.set_token('a07c8fbe4327622d843470a4fe8ced6166158a2b4e7f345f48de22d5')

ts_pro = ts.pro_api()


def get_stock_list():
    """ 获取所有A股股票列表
    :return: stock_list
    """
    stocks = ts_pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    return stocks


# 获取A股股票列表

# 输出股票代码和名称
print(get_stock_list())
