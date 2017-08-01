# -*- coding: utf-8 -*-
'''
pyExcelerator 主要通过两个 对 象 对 Excel 进 行 操 作 ：Workbook 和 Worksheet，分别对应 Excel 的 Book 和 Sheet，一个 Workbook 可以包含多个 Worksheet。
pyExcelerator 最主要的特色在于其能够灵活产生各种带格式的 Excel 文件，但也能够读取已经存在的 Excel 文件，美中不足的是只能读取 Excel 单元格的值，而不能读取各个单元格的格式。
pyExcelerator 读取 Excel 文件只需一个函数： parse_xls。此函数在 ImportXLS.py 文件中定义，函数原型为 parse_xls(filename, encoding = None)。filename 为要打开的 Excel 文件，
encoding 指定此 Excel 文件使用的编码方法。返回值为一个列表，每条目存放一个 Sheet 的数据，它是一个二元组 （表名，单元格数据），其中单元格数据又是一个字典，键值就是单元格的索引 （row，co）l。
如果某个单元格无数据，那么就不存在这个值。假设 book1.xls 文件共有 3 个 sheet，名称分别为Sheet1、Sheet2、Sheet3；Sheet1 数据为 A1=11，A2=12，A3=13；Sheet2 数据为 A1=21，A2 为空，A3=23；Sheet3 为空。
用pyExcelerator 读取方法如下：
from pyExcelerator import *
sheets = parse_xls ('book1.xls')
print sheets
得到的结果：
[
(u'Sheet1', {(2, 0) : 13.0, (1, 0) : 12.0, (0, 0) : 11.0}) ,
(u'Sheet2', {(2, 0) : 23.0, (0, 0) : 21.0}) ,
(u'Sheet3', {})
]
可以看出，由于 Sheet2 的 A2 不存在，所以得到 Sheet2 数据中不存在 （1，0） 单元格。所以，使用返回的数据时一定要先判断单元格是否存在再去读取，否则会出现 KeyError 的异常。
3 生成 Excel 文件
pyExcelerator 中有多个类用于产生 Excel 文件，其中常用的有 3 个：Workbook，Worksheet，XFStyle。
Workbook 代表一个 Excel 文件，Worksheet 代表一个 Excel 文件中的一页，XFStyle 用于确定产生单元格的格式。
3.1 生成简单的 Excel 文件
生成简单 Excel 文件的代码如下：
#coding=utf-8
from pyExcelerator import *
w = Workbook () # 生成 Workbook 对象
ws = w.add_sheet ('Hey, Dude') # 生成 Worksheet 对象
ws.write (0, 0, 'The first cell') # 向 Worksheet 对象的 A1
w.save ('mini.xls') # 将 Workbook 对象存盘
可以看出主要是用 Worksheet 对象的 write 方法写入数据的，此函数定义：write (r, c, label="" , style=Style.XFStyle ())。
r、c 是要写入数据的单元格的行、列坐标，从 0 开始，如 A1 单元就是 （0，0），B2 单元就是 （1，1）。Label 参数是要写入的具体内容。
3.2 设置单元格字体
设置单元格的字体格式就要使用 Font 对象，代码如下：
font0 = Font ()
font0.name = 'Arial'# 字体的名称
font0.bold = True# 是否加粗
font0.italic = True# 是否斜体
font0.height = 200 # 字体的高度，200:相当于 10 点高
font0.struck_out = True# 是否在字之间划删除线
font0.outline = False# 是否采用 outline 字体
font0.shadow = False# 是否加阴影
font0.colour_index = 2# 字体颜色的索引
font0.escapement = font0.ESCAPEMENT_SUBSCRIPT
# 指定字体的上、下标
font0.underline = font0.UNDERLINE_SINGLE_ACC
# 是否使用下划线
font0.family = font0.FAMILY_NONE# 指定字体集
font0.charset = font0.CHARSET_ANSI_CYRILLIC
# 指定字符集
style0 = XFStyle ()
style0.font = font0
wb = Workbook ()
ws0 = wb.add_sheet ('Sheet1')
ws0.write (1, 1, 'Test', style0)
wb.save ('font.xls')
可以看到通过 Font 对象可以设置各种字体格式，大部分使用方法都在注释中给出，其中比较特殊的两个：escapement用于设置字体的上下标，ESCAPEMENT_NONE 不使用上下
标 ， ESCAPEMENT_SUPERSCRIPT 使 用 上 标 ， ESCAPEMENT_SUBSCRIPT 使用下标。underline 用于设置字体的下划线，UNDERLINE_NONE 不使用下划线，UNDERLINE_SIN
GLE 使用单下划线，UNDERLINE_SINGLE_ACC 使用会计用单下划线，UNDERLINE_DOUBLE 使用双下划线，UNDERLINE_DOUBLE_ACC 使用会计用双下划线。另外，通过设置一行上某个单元格字体的高度 （heigh）t 就可以间接地设置此行的行高。
3.3 设置列宽
w = Workbook ()
ws = w.add_sheet ('Sheet1')
ws.write (1, 1, 'Test')
ws.col (1) .width = 8000#8000:400 点
w.save ('col_width.xls')
ws.col (colnum) 函数返回代表第 colnum 列的列对象，可以设置它的 width 属性来设置此列的宽度。
3.4 设置单元格边框
每个单元格都可以设置其边框，这要通过 Borders 对象。
borders = Borders ()
borders.left = borders.DOUBLE # 设置左边框
borders.right = borders.DOUBLE # 设置右边框
borders.top = borders.NO_LINE # 设置上边框
borders.bottom = borders.NO_LINE # 设置下边框
borders.diag = borders.DOUBLE # 设置对角线
borders.left_colour = 0x40 # 设置左边框颜色
borders.right_colour = 0x40 # 设置右边框颜色
borders.top_colour = 0x40 # 设置上边框颜色
borders.bottom_colour = 0x40 # 设置下边框颜色
borders.diag_colour = 0x40 # 设置对角线颜色
borders.need_diag1 = borders.NEED_DIAG1# 设置是否显示左上->右下对角线
borders.need_diag2 = borders.NO_NEED_DIAG2# 设置是否显示左下->右上对角线
style0 = XFStyle ()
style0.borders = borders
wb = Workbook ()
ws0 = wb.add_sheet ('Sheet1')
ws0.write (1, 1, 'Test borders! ', style0)
wb.save ('borders.xls')
可以看出 Borders 是格式 （XFStyle） 的一种，它的 left、right、top、bottom、diag 属性分别设置左、右、上、下、对角五条线的类型，
类型共有 14 种：NO_LINE、THIN、MEDIUM、DASHED、DOTTED、THICK、DOUBLE、HAIR、MEDIUM_DASHED、THIN_DASH_DOTTED、MEDIDOTTED、THIN_DASH_DOT_DOTTED、
MEDIUM_DASH_DOT_DOTTED、SLANTED_MEDIUM_DASH_DOTTED。其中 NO_LINE 为不显示相应的边框，其他值显示对应线形样式的边框，但 diag 除外。
它的 left_colour 等以 _colour 结尾的属性是对应的线的颜色的索引。need_diag1、need_diag2 设置是否需要对角线：NEED_DIAG1 (或 2) 需要、
NO_NEED_DIAG1 (或 2) 不需要。上面的 diag 属性只是设置对角线的线形，只有设置 need_diag 属性为 NEED 才真正显示对角线。
3.5 设置单元格底纹
设置单元格的底纹要通过 Pattern 对象。
pattern = Pattern ()
pattern.pattern = 2 # 设置底纹的图案索引
pattern.pattern_fore_colour = 20 # 设置底纹的前景色
pattern.pattern_back_colour = 10 # 设置底纹的背景色
style0 = XFStyle ()
style0.pattern = pattern
wb = Workbook ()
ws0 = wb.add_sheet ('Sheet1')
ws0.write (1, 1, 'Test pattern! ', style0)
wb.save ('pattern.xls')
Pattern 的 pattern 属性指示底纹的图案索引，0 为实心，1为 75%灰色，2 为 50%灰色，依次类推，可以参考 Excel 的帮助文档。pattern_fore_colour、pattern_back_colour 指示底纹前景色、背景色的颜色索引。
3.6 生成合并的单元格
生 成 合 并 的 单 元 格 要 通 过 Worksheet 的 write_merge、merge 方法，write_merge 的定义：
write_merge ( r1, r2, c1, c2,label="" , style)，merge 的定义：merge (r1, r2, c1, c2, style)，其中 r1，r2 指示要合并单元格的起始行、终止行 （0 为第一行）；
c1、c2 指示要合并单元格的起始列、终止列 （0 为第一列）；label 是写入的数据内容；style 指示合并后单元格的格式。可以看出 merge 是 write_merge 的特殊情况，merge 只能执行写入内容为空的合并操作。示例代码如下：
wb = Workbook ()
ws0 = wb.add_sheet ('Sheet1')
ws0.write_merge (3, 3, 1, 5, 'test1')
# 合并第 4 行，第 2 列到 6 列，并写入 test1。
ws0.write_merge (4, 10, 1, 5, 'test2')
# 合并第 5 行到 11 行，第 2 列到 6 列，并写入 test2。
ws0.merge (12, 15, 1, 5)
# 合并第 13 行到 16 行，第 2 列到 6 列，并写入空白。
wb.save ('merged.xls')
3.7 插入图片
w = Workbook ()
ws = w.add_sheet ('Image')
# 在单元格 （2，2） 偏移为 （10，10） 像素处，横向、纵
# 向伸缩一半
# 插入 python.bmp 图片
ws.insert_bitmap ('python.bmp', 2, 2, 10, 10, 0.5, 0.5)
ws.insert_bitmap ( 'python.bmp', 10, 2) # 在单元格 （10，
插入 python.bmp 图片
w.save ('image.xls')
insert_bitmap 的定义为 insert_bitmap (filename, row, col, x= 0, y = 0, scale_x = 1, scale_y = 1)，filename 为要插入图片的文件名，
本版本只能插入位图文件 (bmp)；row、col 为要插入的行列，x、y 为插入的位置偏移量，缺省为 0，不偏移；
scale_x、scale_y 为横向、纵向的伸缩比，缺省为 1。

'''
