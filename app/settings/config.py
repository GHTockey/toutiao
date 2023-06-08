# 默认配置
class DefaultConfig:
    # 数据库地址 [mysql://用户:密码@地址/数据库]
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.35.128:3306/toutiao'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪数据变化
    SQLALCHEMY_ECHO = False  # 是否打印底层执行的SQL
    pass


config_dict = {
    'dev': DefaultConfig
}
