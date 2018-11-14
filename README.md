 # 压缩文件操作 (封装了zipfile / tarfile)
   1.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0,
                 dry_run=0, owner=None, group=None, logger=None)
    #  base_name:压缩包文件名, format:格式 zip / tar / bztar / xztar / gztar, root_dir:被归档的根目录(默认当前目录)
    # base_dir:保存归档文件的目录(默认当前目录) verbose:已弃用 dry_run:True(不创建归档,但记录日志), owner:用户, group:用户组, logger:日志
    # shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
    dst = shutil.make_archive('Box', 'zip', 'temp')  # 注意:root_dir / base_dir至少写一个,不然会造成压缩包再次被打包的情况
    # 分拆归档, filename:文件名, extract_dir:解压到目录(默认当前目录), format:格式 (未提供,根据扩展名查找,未找到引发ValueError)
    # shutil.unpack_archive(filename[, extract_dir[, format]])
    shutil.unpack_archive('Box.zip')

    lists = shutil.get_archive_formats()  # 返回支持的归档格式列表[(format, info)]
    lists = shutil.get_unpack_formats()  # 返回所有注册格式的列表[(name, extensions, description)]

    # 注册压缩格式, name:格式名, function:def func(base_name, base_dir, owner, group, dry_run, logger), extra_args:额外参数, description:说明信息
    # shutil.register_archive_format(name, function[, extra_args[, description]])
    # shutil.unregister_archive_format(name) // 注销压缩格式
    # 注册解压格式 name:格式名, extensions:扩展名列表, function:实现函数 def unpack(filename, extract_dir), extra_args:额外参数(name, value), description:说明
    # shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])
    # shutil.unregister_unpack_format(name) // 注销解压格式

--------------------- 
作者：LZ_Luzhuo 
来源：CSDN 
原文：https://blog.csdn.net/rozol/article/details/72672698 
版权声明：本文为博主原创文章，转载请附上博文链接！
