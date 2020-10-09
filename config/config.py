import logging
import os
import time

send_email_run = True #自定义发送邮件开关
#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前文件的上一级的上一级目录（增加一级）
#print(prj_path)

data_path = os.path.join(prj_path,'data') #测试数据目录
data_file = os.path.join(prj_path,'data','test-gongfupay_data.xlsx') #云考测试数据存放文件
#print(data_path)
test_case_path = os.path.join(prj_path,'test','user') #用例目录

today = time.strftime('%Y%m%d',time.localtime()) #获取今天的时间
now = time.strftime('%Y%m%d_%H%M%S',time.localtime()) #获取现在的时间

#log_file = os.path.join(prj_path,'log','log.txt'.format(today))  # 更改路径到log目录下
log_file = os.path.join(prj_path,'log','log_{}.txt'.format(today))  # 日历路径+日志文件名，可以按天生成log
#print(log_file)
report_file = os.path.join(prj_path,'report','report_{}.html'.format(now)) # 测试报告路径+文件名
#print(report_file)
result_file = os.path.join(prj_path,'report','result.txt') # 文本路径+文件名
#print(result_file)

caselist_file = os.path.join(prj_path,'test','caselist.txt') #测试用例名称文件SSS

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  #log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  #日期格式
                    filename=log_file,  #日志输出文件
                    filemode='a') #a为写入方式是追加模式

if __name__ == '__main__':
    logging.info("hello liangqian")