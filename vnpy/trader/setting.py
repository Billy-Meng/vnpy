# -*- coding:utf-8 -*-
"""
Global setting of VN Trader.
"""

from logging import INFO    # 控制日志输出的级别，日志输出从频繁到精简可以分成DEBUG、INFO、WARNING、ERROR、CRITICAL五个级别，分别对应10、20、30、40、50的整数值。
from typing import Dict, Any
from tzlocal import get_localzone

from .utility import load_json

SETTINGS: Dict[str, Any] = {
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": INFO,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",
    "dingding.url": "",
    "weixin.sckey": "",

    "datasource.api": "",    
    "jqdata.username": "",
    "jqdata.password": "",
    "rqdata.username": "",
    "rqdata.password": "",
    "jjdata.token": "",

    "database.timezone": get_localzone().zone,
    "database.driver": "sqlite",                # see database.Driver
    "database.database": "database.db",         # for sqlite, use this as filepath
    "database.host": "localhost",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "",
    "database.authentication_source": "admin",  # for mongodb

    "genus.parent_host": "",
    "genus.parent_port": "",
    "genus.parent_sender": "",
    "genus.parent_target": "",
    "genus.child_host": "",
    "genus.child_port": "",
    "genus.child_sender": "",
    "genus.child_target": "",
}

# Load global setting from json file.
SETTING_FILENAME: str = "vt_setting.json"
SETTINGS.update(load_json(SETTING_FILENAME))


def get_settings(prefix: str = "") -> Dict[str, Any]:
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}
