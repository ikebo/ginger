"""
  Created by kebo on 2018/6/21
"""
from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('/get')
def get_user():
    return 'i am kebo'
