# coding:utf8
from urllib import urlretrieve
import csv

# 如何读写csv数据
''''''

'''
实际案例:
http://table.finance.yahoo.com/table.csv?s=000001.sz
我们可以通过雅虎网站获取了中国股市(深圳市)数据集,它以csv数据
格式存储:
......

请将平安银行这只股票,在2016年中成交量超过500000000的记录
存储到另一个csv文件中.

'''
'''
解决方案:
使用标准库的csv模块,可以使用其中reader和writer完成csv文件读写
'''

# urlretrieve('https://finance.yahoo.com/quote/000001.SZ?p=000001.SZ','pingan.csv')
# urlretrieve('http://finance.yahoo.com/d/quotes.csv?s=000001.sz','pingan.csv')
# urlretrieve('http://finance.yahoo.com/table.csv?s=000001.sz','pingan.csv')
# urlretrieve('http://table.finance.yahoo.com/table.csv?table.csv?s=000001.sz','pingan.csv')
'''urlretrieve('http://quotes.money.163.com/service/chd'
            'data.html?code=1000001&start=19910102&e'
            'nd=20180523&fields=TCLOSE;HIGH;LOW;TOPE'
            'N;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;V'
            'ATURNOVER;TCAP;MCAP','pingan1.csv')

f1 = open('pingan1.csv','rb')
data = f1.read()
s = data.decode('GB2312')
f = open('pingan.csv','wb')
f.write(s.encode('utf8'))
f1.close()
f.close()
f = open('pingan.csv','rb')
data = f.read(200)
print data.decode('utf8')'''

with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)

    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        if __name__ == '__main__':
            headers = reader.next()
            writer.writerow(headers)
            for row in reader:
                if row[0] < "2018-01-01":
                    break
                if int(row[11], 10) >= 50000000:
                    writer.writerow(row)
print('end')
