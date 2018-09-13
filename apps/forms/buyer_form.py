from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import StringField, validators, Form
from apps.model.buyer_model import BuyerUser
from apps.settings import api_redis


class BuyerRegisterForm(Form):
    '''buyer 注册 form验证表

     :parameter
     username:
     password:
     tel:
     '''
    username = StringField(validators=(validators.InputRequired(message="请输入用户名"),
                                       validators.Length(max=32, message="用户名过长"),
                                       validators.Length(min=6, message="用户名过短"),
                                       ),
                           )
    password = StringField(validators=(validators.InputRequired(message="请输入密码"),
                                       validators.Length(max=128, message="密码过长"),
                                       validators.Length(min=6, message="密码过于简单"),
                                       ),
                           )
    tel = StringField(validators=(validators.InputRequired(message="请输入手机号"),
                                  validators.Regexp(
                                      "(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\\d{8}",
                                      message="手机格式不正确"),

                                  )
                      )
    sms = StringField(validators=(validators.InputRequired(message="请输入验证码"),
                                  ),
                      )

    def validate_username(self, obj):
        username = BuyerUser.query.filter_by(username=obj.data).first()
        if username:
            raise validators.ValidationError("用户名已存在!")

    def validate_sms(self, obj):
        redis_sms = api_redis.get("reg_" + self.tel.data)

        if not redis_sms:
            raise validators.ValidationError("验证码已过期!")
        redis_sms = redis_sms.decode("utf-8")
        if redis_sms != obj.data:
            raise validators.ValidationError("验证码错误!")

    def validate_tel(self, obj):
        tel = BuyerUser.query.filter_by(tel=obj.data).first()
        if tel:
            raise validators.ValidationError("手机号已注册!")


class BuyerLoginForm(Form):
    name = StringField(validators=(validators.InputRequired(message="请输入用户名"),
                                   ),
                       )
    password = StringField(validators=(validators.InputRequired(message="请输入密码"),
                                       ),
                           )

    def validate_name(self, obj):
        password = self.password.data
        username = BuyerUser.query.filter_by(username=obj.data).first()
        if not username or not username.check_password(password):
            raise validators.ValidationError("用户名密码错误!")


class BuyerAddressForm(Form):
    name = StringField(validators=(validators.InputRequired(message="请输入收货人姓名"),
                                   ),
                       )
    tel = StringField(validators=(validators.InputRequired(message="请输入手机号"),
                                  validators.Regexp(
                                      "(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\\d{8}",
                                      message="手机格式不正确"),

                                  )
                      )
    provence = StringField(validators=(validators.InputRequired(message="请输入完整收货人地址"),
                                       ),
                           )
    city = StringField(validators=(validators.InputRequired(message="请输入完整收货人地址"),
                                   ),
                       )
    area = StringField(validators=(validators.InputRequired(message="请输入完整收货人地址"),
                                   ),
                       )
    detail_address = StringField(validators=(validators.InputRequired(message="请输入完整收货人地址"),
                                             ),
                                 )
