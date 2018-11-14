# CSV
### 1. csv.reader(csvfile, dialect='excel', **fmtparams)
```
* params
  * csvfile 可以是任何的可迭代对象，并且该对象的__next__()每次被调用返回字符串(一般是file和list对象，如果是file对象，open的时候需要指定newline="")
  * dialect
  * fmtparams
* return
  * 对于给定的csvfile，返回一个可迭代的reader对象
```
```
Example:


```
