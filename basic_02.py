"""
python基础知识02
正则表达式

"""

# 如何表示空格
# '\s'

# 如何表示字母
# '\w'

# 如何表示数字
# '\d'

# 如何表示特殊字符'-'
# '\-'

# 如何表示任意字符
# '.'

#############

# 如何表示0到5和a到y的数字范围
# [0-5][a-y]

# 如何表示2个当中的任意一个
# a|bc

#############


# 如何表示0或1个
# 'a？' 可表示为空，也可表示为a

# 如何表示3到5个字符
# 'a{3,5}'

# 如何表示1-n个字符
# 'a+'，可表示a，也可表示aaaaaa


# 如何表示0-n个字符
# 'a*' 可表示空，也可表示aaaaaa

#############

# 如何表示任意多的字符
# .*
# 如何表示
# .*?

import re

# 如何从一个字符串的开头位置，匹配相应的字符内容
if re.match(r'ab{3,5}','abbbb3'):
    print("success")
else:
    print('fail!')

# 如何从一个字符串的任意位置，进行匹配相应的字符内容
if re.search(r'ab','cccab'):
    print("成功找到了")
else:
    print("fail")

# 如何对一个字符串，进行拆分(同时还可以去除空格)
str1 = "lin guoyang"
str2 = str1.split(' ')
str3 = re.split(r'\s+',str1)
str4 = str1.replace(' ','')

print(str4)

# 如何过滤掉或替换掉用户输入的不规范的字符，比如；，！？等
str1 = 'lin,  -guoy!ang'
# str2 = re.split(r'[\s\,\!\;]+',str1)
str3 = re.sub(r'[\s\,\!\;]+','',str1)

print(str3)

# 如何对一个字符串的内容，进行[分组]的提取：
str1 = 'linguoyang@gfgf.com'
obj = re.search(r'([a-z0-9]+)\@([a-z]+)\.([a-z]+)',str1)
i = 0
for i in range(0,4):
    if obj.group(i):
        print(obj.group(i))
    else:
        print('\n')
        break

# 如何找到一个字符串中的所有手机号
str1 = "13616187656,还有一个手机号15623453345"
obj_list = re.findall(r'[0-9-()（）]{7,18}',str1)
print(obj_list)