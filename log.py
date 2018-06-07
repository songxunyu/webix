import logging.config
log_config = {
    "version": 1,#版本号,必填
    "disable_existing_loggers": True,#是否禁用其他logging
    "formatters": {#格式器
        "simple": {
            "format": "%(asctime)s-[%(levelname)s]-[%(pathname)s]-[%(funcName)s_%(lineno)d]:%(message)s",
            "datefmt": "%Y/%m/%d %H:%M:%S",
        },
        "simple1": {
            "format": "simple1：%(asctime)s-ame)s_%(lineno)d]:%(message)s",
            "datefmt": "%Y/%m/%d %H:%M:%S",
        }
    },

    "handlers": {#选择日志的输出地方/日志处理器
        "console": {#创建处理器
            "class": "logging.StreamHandler",#输出到控制台，如：控制台，文件，邮件发送等
            "level": "DEBUG",
            "formatter": "simple",#配置输出的格式,formatters
            "stream": "ext://sys.stdout"
            #输入sys.stdin
            #输出sys.stdout
            #出错sys.stderr
        },

        "WARNING_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",#根据大小切分文件
            "level": "WARNING",#日志最低级别
            "formatter": "simple",#配置输出到log文件的格式
            "filename": "info.log",#日志文件名称
            "maxBytes": 1024*1024*5,#指定日志文件大小
            "backupCount": 5,#指定日志文件总数量
            "encoding": "utf8"#指定格式
        },

        "ERROR_file_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",#根据日期切分文件
            "level": "ERROR",
            "formatter": "simple",
            "filename": "WARING.log",
            'when':'S',#切分时间
            "interval": 1,#是指等待多少个单位when的时间后，Logger会自动重建文件
            "backupCount": 5,
            "encoding": "utf8"
        },
        "CRITICAL_email_handler": {
            "class": "logging.handlers.SMTPHandler",#发送邮件
            "level": "CRITICAL",
            "formatter": "simple",
            'mailhost':'mail.srv',#邮件服务器
            'fromaddr':'robot@xiaomi.com',#发件人
            'toaddrs':['songxunyu@xiaomi.com'],#收件人
            'subject':'警报！',#邮件标题

        },
        # "ERROR_http_handler": {
        #     "class": "logging.handlers.HTTPHandler",#？输出到http接口，总是报错
        #     "level": "ERROR",
        #     "formatter": "simple",
        #     "url":"http://10.232.45.250",
        #     "host":"8080",
        # }
    },

    # "loggers": {#记录器，优先级1
    #     "": {
    #         "level": "INFO",
    #         "handlers": ["console"],
    #         "propagate": 'no'
    #     }
    # },

    "root": {#根配置,优先级0
        "level": "INFO",
        "handlers": ["console",
                     "WARNING_file_handler",
                     "ERROR_file_handler",
                     "CRITICAL_email_handler",
                     ]
    }
}

logging.config.dictConfig(log_config)#从字典中获取配置
def log_fun():
    log = logging.getLogger(__file__)
    log.debug('This message should go to the log file')
    log.info('So should this')
    log.warning('And this, too')
    log.error('And this, too')
    log.critical('广告位不足')
log_fun()