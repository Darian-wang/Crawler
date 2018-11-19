# <center>Linux下一些常见的错误</center>
## 1. /bin/bash^M: bad interpreter
```
Root cause:windows&linux下换行符不一样导致(windows:\r\n;linux:\n)
Solutions :用vim编辑器打开，可以查看文件格式 :set ff?,修改格式为unix.即:set ff=unix
```

