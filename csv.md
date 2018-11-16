# <center>CSV Module<center>
## 一.Constants
```
这几个Constants的值分别为0,1,2,3.用来指定quoting参数.
csv.QUOTE_MINIMAL:field里面含有delimiter,quotechar才用quotechar括起来
csv.QUOTE_ALL:all field写入的时候用quotechar括起来
QUOTE_NONNUMERIC:field为非数字的时候才用quotechar括起来
QUOTE_NONE：all field都不括起来
Note:
括起来的field中含有quotechar优先使用double quotechar,如果doublequote=False则需要指定espacechar,去escape quotechar,否则raise exception
```
## 二.Common Functions
### 1. csv.reader(csvfile, dialect='excel', **fmtparams)
* params：
  * csvfile 可以是任何的可迭代对象，并且要求该对象的\__next__()返回字符串  
  (一般是file和list对象，如果是file对象，open的时候需要指定newline="")
  * dialect 一个csv format attr class，默认有["excel", "excel-tab", "unix"],也可以自己注册
  * fmtparams Dialect类中的属性设置。一般为:  
  delimiter = ','  
  quotechar = '"'  
  doublequote = True  
  escapechar = None(excel中没重新赋值)  
  skipinitialspace = False  
  lineterminator = '\r\n'  
  quoting = QUOTE_MINIMAL  
  strict = False(excel中没有给出定义,如果为True,则在csv文件的格式不对的时候raise exception.否则不raise)
* return
  * 返回一个可迭代的reader对象,迭代csvfile中每行的内容

```
Example:
1) csv_list = ["1,2,3,4", "2,3,4,5", "3,4,5,6", "4,5,6,7"]
   reader = csv.reader(csv_list)
   for element in reader:
      print(element)
2) path = "C:\wqj\linux.csv"
   with open(path, "r", encoding="utf8") as f:
      reader = csv.reader(f)
      for line in reader:
          print(line)
```
### 2. csv.writer(csvfile, dialect='excel', **fmtparams)
* params:
  * csvfile 可以是任何具有wirte方法的对象.(如果是file对象，open的时候需要指定newline="")
  * dialect 同reader方法
  * fmtparams 同reader方法
* return
  * 返回一个writer对象，它负责把用户的数据转化为分隔符字符串  

```
Example:  
with open(file=path, mode="w", newline="") as f:
  writer = csv.writer(f, quoting=csv.QUOTE_NONE, quotechar="|", doublequote=True, escapechar="?")
  writer.writerow(["1", str(2.3), 3, 4, "12,|?3"])
```
### 3. csv.get_dialect(name)  
* description:  
根据name返回一个不可变的Dialect object,如果给出的name没有注册，则raise _csv.ERROR

### 4. csv.list_dialects()
* description:
返回所有注册的dialect的name(list)

### 5. csv.field_size_limit([new_limit])
返回能分析的最大的field size，如果new_limit赋值，则它成为新的limit(64bit 下windows为131072)

### 6. csv.register_dialect(name[, dialect[, **fmtparams]])
* params:
  * name 注册的name
  * dialect/fmtparams 一个Dialect的子类或者指定关键字参数或者两者同时指定,如果同时指定，关键字参数将覆盖Dialect子类中的属性值

```
Example:  
register_dialect("excel", excel)
```

### 7. csv.unregister_dialect(name)
* 注销一个dialect，如果给出的name未被注册，则raise _csv.ERROR

## 三. classes
### 1. class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
* description:
  创建一个reader对象，但是每行的信息都会map到一个OrderDict,fieldnames提供sequence为dict的key.
* params:
  * filednames: 是一个list，用来指定dict的key，如果filednames omitted则会使用f的第一行作为key
  * restkey: 当f中的一行多于filednames,会使用restkey作为剩下的filed的key(剩下的filed会放到一个list中)
  * restval: 当f中的一行少于filednames，则用restval填充
  * other  : 其他的params作为基本的reader参数
```
Example:
>>> import csv
>>> with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
```

### 2. class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
* description:
  创建一个writer对象，
* params:
  * filednames: 是一个list,用来标识传递给writerow()方法中的植被写入f的顺序
  * restval   : 当写入的dict对于fieldnames缺失key，就用restval来填充
  * extrasaction: 当传入writerow()中的dict的key在filednames中没有找到，用来设置行为，如果设置为raise，会raise ValueError,如果设置为ignore，将会被忽略
  * other     ：其他的params作为基本的writer的参数

```
Example:
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```
### 3. class csv.Dialect
* 定义csv format的一些基本的attr

### 4. class csv.excel
* 定义基于excel的Dialect(默认分隔符为， 换行符为\r\n)

### 5. class csv.excel_tar
* 定义基于excel的Dialect(默认分隔符为tab 换行符为\r\n)

### 6. class csv.unix_dialect
* 定义基于unix的Dialect(默认分割符为， 换行符为\n)

### 7. class csv.Sniffer
* description:
Sniffer是嗅探的意思，用于推断csv format
* method:
```
  1.sniff(sample, delimiters=None)
  分析给定的sample，返回Dialect子类
  2.has_header(sample)
  分析给定的sample文本，如果第一行看起来是一系列的标题，则返回True
```
```
Example：
with open('example.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
```

## 四. Exception
exception csv.Error
```
class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""
```

## 五. Advanced
### 1.reader对象(一个DictReader的实例，或者是reader()函数返回的对象)
```
method：
  1) csvreader.__next__()
  * description:
  reader将根据dialect分析，把下一行的内容以一个列表的形式返回，如果是DictReader的实例，将返回一个dict
attr：
  1）csvreader.dialect
  返回一个只读的dialect的描述
  2）csvreader.line_num
  返回从源iter读的line num
  3）csvreader.fieldnames
  返回filednames,如果在创建对象的时候未传递filednames,将在首次访问或者从文件的第一行初始化此属性
```
### 2.writer对象(一个DictWriter的实例，或者是writer()函数返回的对象)
```
method:
  1）csvwriter.writerow(row)
  根据当前的dialect format 写入文件对象，row可以是任意的可迭代对象
  2）csvwriter.writerows(rows)
attr:
  1）dialect
DictWriter:
  1) DictWriter.writeheader()
```
