# -*- coding: utf-8 -*-
import re
'''
at|home at, home
bat|bet|bit bat, bet, bit
f.o 在"f"和"o"中间的任何字符，如fao, f9o, f#o 等
.. 任意两个字符
.end 匹配在字符串end 前面的任意一个字符
^From 匹配任何以From 开始的字符串
/bin/tcsh$ 匹配任何以 /bin/tcsh 结束的字符串
^Subject: hi$ 匹配仅由 Subject: hi 组成的字符串
b[aeiu]t bat, bet, bit, but
[cr][23][dp][o2] 一个包含4 个字符的字符串: c2do, r3p2, r2d2, c3po, 等等
z.[0-9] 字符"z"，后面跟任意一个字符，然后是一个十进制数字[r-u][env-y][us] “r” “s,” “t” 或 “u” 中的任意一个字符，后面跟的是 “e,”“n,” “v,” “w,” “x,” 或 “y”中的任意一个字符，再后面是字符“u” 或 “s”.
[^aeiou] 一个非元音字符
[^\t\n] 除TAB 制表符和换行符以外的任意一个字符
["-a] 在使用ASCII 字符集的系统中，顺序值在‘"‘ 和 “a”之间 的任意一个字符，即，顺序号在34 和97 之间的某一个字符。
[dn]ot? 字符"d"或"o", 后面是一个"o", 最后是最多一个字符"t"，即，do, no, dot,not
0?[1-9] 从1 到9 中的任意一位数字，前面可能还有一个"0". 例如：可以把它看成一月到九月的数字表示形式，不管是一位数字还是两位数字的表示形式。
[0-9]{15,16} 15 或16 位数字表示，例如：信用卡号码
</?[^>]+> 匹配所有合法(和无效的)HTML 标签的字符串
[KQRBNP][a-h][1-8]-[a-h][1-8] 在“长代数”记谱法中，表示的国际象棋合法的棋盘。
即， “K,” “Q,” “R,” “B,” “N,” 或 “P” 等字母后面加上两个用连字符连在一起的"a1"到"h8"之间的棋盘坐标。前面的编号表示从哪里开始走棋，后面的编号代表走到哪个位置(棋格)去。
\w+-\d+ 一个由字母或数字组成的字符串，和至少一个数字，两部分中间由连字符连接
[A-Za-z]\w* 第一个字符是字母，其余字符(如果存在的话)，是字母或数字
\d{3}-\d{3}-\d{4} (美国)电话号码，前面带区号前缀，例如 800-555-1212
\w+@\w+\.com 简单的XXX@YYY.com 格式的电子邮件地址
\d+(\.\d*)? 表示简单的浮点数，即， 任意个十进制数字，后面跟一个可选的小数点，然后再接零或多个十进制数字。例如：“0.004,” “2,” “75.”,等等。
(Mr?s?\. )?[A-Z][a-z]* [ A-Za-z-]+ 名字和姓氏，对名字的限制(首字母大写，其它字母(如果存在)小写), 全名前有可选的称谓(“Mr.,”“Mrs.,” “Ms.,” 或 “M.,”)，姓氏没有什么限制，允许有多个单词、横线、大写字母。
'''

#compile(pattern,flags=0) 对正则表达式 模对正则表达式 模pattern 进行编译，并返回一个 是可选标志符，并返回一个 regex对象
regex = re.compile('A\d+A')

#match(pattern,string, flags=0) 尝试用正则表达式 模pattern 匹配字符串 string，如果匹配成功则返回一 个匹配对象；否则返回 None。
#（pattern、string从第一个字符开始匹配，如果 从第一个字符开始匹配，如果 pattern在string中间位置，则匹配失败）
text = 'A1A2A3A4A5A6'
match = re.match(regex,text)
print match.group()
print '......'
#search(pattern,string, flags=0) 在字符串 string中查找正则表达式 模中查找正则表达式 模pattern的第一次出现， 如果匹配成 功，则返回 一个匹配对象；否None
match = re.search(regex,text)
print match.group()
print '......'
#findall(pattern,string[,flags]) 在字符串 string 中查找正则表达式 模中查找正则表达式 模pattern的所有 (非重复 )出现；返回一个匹配对象的列表
match = re.findall(regex,text)
for m in match:
    print m

#finditer(pattern,string[, flags]) 和findall()相同，但返回的不是列表而迭代器；对于每个匹配该一象 相同，但返回的不是列表而迭代器；对于每个匹配该一象

    
#split(pattern,string, max=0) 根据正则表达式 pattern中的分隔符 把字string分割 为一个列表，返回成功匹配的最多max次(默认是分割所有匹配的地方 默认是分割所有匹配的地方 )。
#sub(pattern, repl, string, max= 0) 把字符串 string中所有匹配正则表达式 pattern的地方替换成字符串 repl, 如果 max的值没有给 出，则对所有匹配的地方进行替换 (另外，请参考 subn(), 它还会返回一个表示替换次数的值 )。
#group(num=0) 返回全部匹配对象 (或指定编号是 num 的子组 的子组 )
#groups()返回一个包含全部匹配的子组 元(如果没有成功匹配，就返回一个空元组 )