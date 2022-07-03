# self 类似于其他语言中的 this
# 重写 __str__ 类似于 java 里面的 toString()
class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def __str__(self):
    return 'name: %s, score: %s' % (self.name, self.score)


if __name__ == "__main__":
  student = Student("zhangsan", 14)
  print(student)
