# 初始化日志
# 为什么要在api.__init__.py中初始化日志
# 因为,我们后面的进行接口测试时,会调用
import app
import logging
# 调用方法
app.init_logging()
logging.info("日志可以打印")


