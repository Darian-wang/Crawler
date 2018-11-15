# CSV
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
