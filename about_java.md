# Study Java
#### **IntelliJ IDEA**
 注释快捷键
  Ctrl + /
  Alt + Enter
___
1. 有小数点的数，默认为 double 所以float f= 1.0会报错，应改为 double f=1.0

2. 默认情况下，小数被看作double型，若使用float型小数，需要在小数后添加F或f;
  可以使用d或者D表明这是一个double类型数据,但声明float型变量时如果不加f，系统会
  认为变量是double类型而出错。

3. 将浮点数转为整数 int x = (int) 24.6；

4. 's'与"s"的区别:'s'表示一个字符；"s"表示一个字符串

5. 一直不变的量称为常量(constant),通常也称为"final变量"。常量名通常使用大写字母

6. 类型前面加上关键字static，这样的成员变量称为静态变量。静态变量的有效范围可以跨
类，甚至可以达到整个应用程序之内。还能直接以"类名.静态变量"的方式在其他类内使用

7. 自增和自减
    假设a=4
    b = ++a; //先将a的值加1,此时a =5,b的值为5;
    b = a++; //先将a的值赋b,再将a的值变为5,b值为4;

    System.out.print("Hello World");

1. this is a test
> go or dead

# About 基本数据类型(primitive data type)
byte,short,int,long
float,double
char 2个字节
boolean 1位

# 变量
# 局部变量 需要初始化才能使用
# 成员变量 可以不初始化，它会根据数据类型自动初始化
# 静态变量 static variable

# 常量 Constant 一量被初始化就不能被修改；也叫符号常量

# About 变量和常量命名规范
1.所有变量、方法、类名：见名知意
2.类成员变量：首字母小写和驼峰原则：monthSalary
3.局部变量：首字母小写和驼峰原则
4.常量：大写字母和下划线：MAX___VALUE
5.类名：首字母大写和驼峰原则:Man,GoodMan
6.方法名：首字母小写和驼峰原则:run(),runRun()

# 整数运算
1，如果两个操作数有一个为Long,则结果也为long
2，没有long时，结果为int.即使操作全为short，byte,结果也是int
浮点运算：
3，如果两个操作数有一个为double，则结果为double
4，只有两个操作数是float,则结果才为float

# 取模运算
”余数”符号和左边操作数相同。如：
7%3=1;7%-3=1;-7%3=-1;