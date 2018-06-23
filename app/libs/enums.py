"""
  Created by kebo on 2018/6/22
"""

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 小程序 公众号
    USER_MINA = 200
    USER_WX = 201
