# 字符串中既有双引号也有单引号
print('I\'m \"OK\"!')
# 转义字符
print('I\'m learning\nPython.')
# 简化转义字符
print(r'\\\t\\')
print(r"\\\t\\")
#多行内容
print('''line1
line2
line3''')
# 多行字符串取消转义
print(r'''hello,\n
world''')
#包含中文的字符串
print('包含中文')
#字符和整数的转换
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
# 十六进制写str
print( '\u4e2d\u6587') #中文
x = b'ABC'
print(x)
# 在 bytes 中，无法显示为ASCII字符的字节，用 \x## 显示
print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'
# 统计字符数
print(len('ABC'))   #3
print(len('中文'))   #2
# 统计字节数
print(len(b'ABC'))                      #3
print(len(b'\ex4\xb8\xe6\x96\x87'))     #8
print(len('中文'.encode('utf-8')))      #6
# 格式化
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
s1 = 72
s2 = 85
r = (85 - 72) / 72
print('%.1f%%' % r)
