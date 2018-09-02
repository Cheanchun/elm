# 定义从attrs字典结构中,赋值表字段名
def set_attrs(self, attrs):
    for k, v in attrs.items():
        if hasattr(self, k) and k != 'id':
            setattr(self, k, v)
