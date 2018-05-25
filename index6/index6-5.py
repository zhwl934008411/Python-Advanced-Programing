# coding:utf8
import xlrd, xlwt
# 在python中如何读写excel文件
import xlrd

# 利用Python读写excel,添加'总分'列,计算每人总分

''''''

'''
解决方案:
#使用pip安装, pip install xlrd,xlwt
使用easy-install tool安装
sudo apt install python-setuptools
sudo easy_install xlrd

使用第三方库xlrd(读取excel)和xlwt(写入数据到excel),这两个库分别用于excel读和写
'''
rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)

'''
import xlrd,xlwt
ls
rook = xlrd.open_workbook('demo.xlsx')
rsheet = rook.sheet_by_index(0)
nc = rsheet.ncols?
nc = rsheet.ncols
nc
rsheet.put_cell?
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,u'总分',None)
rsheet.cell_value?
rsheet.cell_value(0,4)
print rsheet.cell_value(0,4)
rsheet.name
rsheet.number
rsheet.nrows
for row in xrange(1,rsheet.nrows):
    rsheet.row_values?
    t = sum(rsheet.row_values(row,1,3))
    rsheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None)
for row in xrange(1,rsheet.nrows):
    print row_values(row,1,nc)
for row in xrange(1,rsheet.nrows):
    print row_values(row,nc)
for row in xrange(1,rsheet.nrows):
    print rsheet.row_values(row,nc)
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
wsheet
wsheet.name
for r in xrange(rsheet.nrows):

    
    
    
    
    print r
wsheet.write?
style = xlwt.easyxf('align:vertical center,horizontal center')
for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r,c,sheet.cell_value(r,c),style)
for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)
for r in xrange(rsheet.nrows):
    for c in xrange(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)
history
wsheet
wsheet.ce
wsheet.n
wsheet.ncols
wbook.save('output1.xlsx')
wbook = xlrd.open_workbook('output1.xlsx')
wsheet = wbook.sheet_by_index(0)
for r in xrange(wsheet.nrows):
    print(wsheet.row_values(r,1,wsheet.ncols))
nc = wsheet.ncols
nc
wsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,u'平均分',None)
print wsheet.row_values(0,0)
print wsheet.row_values(0,0,5)
print wsheet.row_values(0,0,6)
print wsheet.row_values(0,0,nc)
wsheet.row_values?
print wsheet.row_values(0,nc,nc)
print wsheet.row_values(0,nc-1,nc-1)
print wsheet.row_values(0,nc-1)
print wsheet.row_values(0,nc-1,nc)
print u'\u603b\u5206'
print u'\u5e73\u5747\u5206'
print wsheet.row_values(0,nc,nc)
for r in xrange(1,wsheet.nrows):
    t = wsheet.cell_value?
for r in xrange(1,wsheet.nrows):
    t = wsheet.cell_value(r,5)/3
    wsheet.put_cell(r,6,xlrd.XL-CELL_TEXT,t,None)
wsheet.rows
wsheet.nrows
wsheet.ncols
for r in xrange(1,wsheet.nrows):
    t = wsheet.cell_value(r,5)/3
    print t
wsheet.cell_value(1,5)
wsheet.cell_value(1,4)
for r in xrange(1,wsheet.nrows):
    t = wsheet.cell_value(r,4)/3
    wsheet.put_cell(r,5,xlrd.XL_CELL_NUMBER,t,None)
wsheet.cell_value(1,5)
for r in xrange(1,wsheet.nrows):
    t = round(wsheet.cell_value(r,5),2)
    wsheet.put_cell(r,5,xlrd.XL_CELL_NUMBER,t,None)
wsheet.cell_value(1,5)
min = wsheet.cell_value(1,5)
for r in xrange(wsheet.nrows):
    s = sorted(wsheet.row_values(r,1))
    print s
wsheet.row_values?
wsheet.row?
wsheet.col?
wsheet.col_values?
wsheet.col_values(wheet.ncols,1)
r = wsheet.col_values(wsheet.ncols,1)
r = wsheet.col_values(wsheet.ncols-1,1)
r
s = sorted(r)
s
history


'''
