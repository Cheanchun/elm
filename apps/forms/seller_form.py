from flask_wtf import FlaskForm  # 需要flask上下文
from wtforms import StringField, validators, PasswordField
from apps.model.seller_model import User

# 用户注册form验证
class RegisterForm(FlaskForm):
    '''
    后台用户管理注册数据效验
    '''

    username = StringField(label="用户名 :",
                           validators=(validators.DataRequired(message="请输入用户名"),
                                       validators.Length(max=16, message="用户名字符数太多"),
                                       validators.Length(min=3, message="用户名不能少于3个字符"),
                                       ),
                           render_kw={"class": "form-control", "placeholder": "请输入账号!", "required": 'required'}
                           )
    password = PasswordField(label="密  码:",
                             validators=(validators.DataRequired(message="请填写密码"),
                                         ),
                             render_kw={"class": "form-control", "placeholder": "请输入密码!", "required": 'required'}
                             )
    password1 = PasswordField(label="确认密码:",
                              validators=(validators.EqualTo("password", message="两次密码不一致"),
                                          ),
                              render_kw={"class": "form-control", "placeholder": "确认密码!", "required": 'required'}

                              )

    # 验证用户是否注册
    def validate_username(self, obj):
        username = obj.data
        if User.query.filter_by(username=username).first():
            raise validators.ValidationError(message="用户名已被注册")


# 用户登陆form验证
class UserLogin(FlaskForm):


    username = StringField(label="用户名 :",
                           validators=(validators.DataRequired(message="请填写用户名"),
                                       ),
                           render_kw={"class": "form-control", "placeholder": "请输入账号!", "required": 'required'}
                           )
    password = PasswordField(label="密  码:",
                             validators=(validators.DataRequired(message="请填写密码"),
                                         ),
                             render_kw={"class": "form-control", "placeholder": "请输入密码!"}
                             )

    # 用户密码验证
    # def validate_password(self,password):
    #     if check_password_hash(self.password, password):
    #         return True
    #     else:
    #         raise validators.ValidationError(message="用户或者密码错误!")







