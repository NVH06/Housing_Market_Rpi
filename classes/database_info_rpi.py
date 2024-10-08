import os


class RpiHost:
    host = os.environ["HOST"]
    database = "hm"
    user = "botuser"
    pwd = os.environ["MYSQL_PWD"]
    tables = ["financial", "location", "property"]


class RpiHostTest:
    host = os.environ["HOST"]
    database = "hm_test"
    user = "botuser"
    pwd = os.environ["MYSQL_PWD"]
    tables = ["financial", "location", "property"]


class SshInfo:
    host = os.environ["HOST"]
    user = 'nvh'
    pwd = os.environ["SSH_PWD"]
