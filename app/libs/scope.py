"""
  Created by kebo on 2018/6/23
"""


class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    pass


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
