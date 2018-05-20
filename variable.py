print '===================================';
# list
list = [1, '2', 0xA, 0XDEADBEAF];
print 'printing some lists';
print list * 2;
print list[1:3];
print '===================================';
# tuple
tuple = (1, '2', 0X3, 4.0);
print 'printing tutple';
print tuple;
#tuple[0] = 1.0; # invalid. throw error
print '===================================';
# dictionary
dict = {'int': 1, 'float': 1.0, 'str': 'hello, world'};
print 'printing dictionary';
print dict;
# print dict[0:1]; # invalid
print dict['int'];
# print dict['DNE']; # invalid. throw error
print dict.keys();
print dict.values();
print '===================================';
# type conversion
print 'convert 0x42 to base 10'
print int('42', 16);
print 'convert 65 to char';
print chr(65);
print 'convert 10 to base 8';
print oct(10);
print '===================================';
