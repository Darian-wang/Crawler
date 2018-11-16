## <center>configparser</center>
* Description:
配置/解析 类似windows ini文件格式的配置文件(不解析/写入 windows注册表扩展版本的ini语法中使用的值类型前缀),格式如下:
[section]
key = value //也可以是":";section区分大小写，key不区分大小写;"#",";"为注释内容;一个value跨越多行时需要缩进，没有value直接不写,整个section也可以一起被缩进
1.default部分为其他部分提供默认值
2.section中的key不区分大小写并且以小写形式存储
3.config parser不会去猜测配置文件中值的数据类型，始终会以字符串的形式存储，这意味着如果你需要数据类型，你需要自己转换
getboolean()
由于bool("False")还是True，所以模块提供了getboolean(),这个方法不区分大小写并且可以识别"yes/no","on/off","true/false","1/0";
config.getboolean('bitbucket.org', 'Compression')
getint()
getfloat()
你还可以注册自己的转换器
4.可以使用section的get方法去获取值,如果get指定了默认值，会优先使用default section中的值，如果没有就取用get指定的值
此外get,getboolean,getint,getfloat中有fallback参数



```
  Extension:
  * 类似Unix shell使用shlex
  * json
```
* Example:

```
    1.configparser write
    import configparser

    config = configparser.ConfigParser()
    config["DEFAULT"] = {
        "ServerAliveInterval": 45,
        "Compression": "yes",
        "CompressionLevel": "9",
        "ForwardX11": "yes"
    }
    config["bitbucket.org"] = {}
    config["bitbucket.org"]["User"] = "hg"
    config["topsecret.server.com"] = {}
    config["topsecret.server.com"]["Port"] = "50022"
    config["topsecret.server.com"]["ForwardX11"] = "no"

    with open("test.ini", "w") as configfile:
        config.write(configfile)
    2.configparser read
      1)从配置文件中读
        config = configparser.ConfigParser()
        config.read("config.ini")
      2)从字典中读
        config = configparser.configParser()
        config.read_dict({'section1': {'key1': 'value1',
                                       'key2': 'value2',
                                       'key3': 'value3'},
                          'section2': {'keyA': 'valueA',
                                       'keyB': 'valueB',
                                       'keyC': 'valueC'},
                          'section3': {'foo': 'x',
                                       'bar': 'y',
                                       'baz': 'z'}
                          }
      3)获取所有的section
        config.sections() # 会过滤掉[default]
      4)获取指定的section的所有key&value
        config.items("topsecret.com")
      5)获取指定section的所有key
        config.options("topsecret.com")
      6)获取指定section&key的value
        config["topsecret.com"]["User"]
        config.get("topsecret.com", "User")
        config.getint("topsecret.com", "Port")
      7)检查是否有section,key,value
        "DEFAULT" in config
        "test" in config["section_test"]
        "Tom" in config["bitbucket.org"]["User"]
        config.has_section("topsecret.com")
        config.has_option("topsecret", "User")
      8)添加
        config.add_section("section_1")
        config.set("section_1", "key_1", "value_1")
      9)删除
        config.remove_option("section_1", "key_1")
        config.remove_section("section_1")
        config.clear() # 清除除[default]之外的所有内容
      
```
    

### 1. class configparser.BasicInterpolation
* 除核心功能外，ConfigParser还支持插值。 这意味着可以在从get（）调用返回值之前对值进行预处理
