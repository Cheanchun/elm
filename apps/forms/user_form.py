from flask_wtf import FlaskForm  # 需要flask上下文
from werkzeug.security import check_password_hash
from wtforms import StringField, validators, PasswordField
from apps.model.user_model import User

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
                           render_kw={"class": "form-control"}
                           )
    password = PasswordField(label="密  码:",
                             validators=(validators.DataRequired(message="请填写密码"),
                                         ),
                             render_kw={"class": "form-control"}
                             )
    password1 = PasswordField(label="确认密码:",
                              validators=(validators.EqualTo("password", message="两次密码不一致"),
                                          ),
                              render_kw={"class": "form-control"}

                              )

    # 验证用户是否注册
    def validate_username(self, obj):
        username = obj.data
        if User.query.filter_by(username=username).first():
            raise validators.ValidationError(message="用户名已被注册")


# 用户登陆form验证
class UserLogin(FlaskForm):
    # try   要求用户名格式
    # validators = [
    #     DataRequired(), Length(1, 64), '^[A-Za-z][A-Za-z0-9_.]*$', 0, u'用户名必须由字母、数字、下划线或 . 组成']

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







