from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.widgets import HiddenInput


class MenuFoodUpdateForm(FlaskForm):
    # 对外ID model -->  goods_id

    # 菜品名称
    goods_name = StringField(label="菜品名称 :",
                             validators=(validators.DataRequired(message="请填写菜品名称"),

                                         ),
                             render_kw={"class": "form-control", "placeholder": "菜品名称!", "required": 'required'}
                             )
    # 菜品评分
    # rating = FloatField(label="菜品评分 :",
    #                     validators=(validators.DataRequired(message=""),
    #
    #                                 ),
    #                     render_kw={"class": "form-control", "placeholder": "菜品名称!", "required": 'required'}
    #                     )
    # 归属店铺
    shop_pid = SelectField(label="归属店铺 :",
                           render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                           )

    # def __init__(self, *args, **kwargs):
    #     super(MenuFoodUpdateForm, self).__init__(*args, **kwargs)
    #
    #     self.shop_pid.choices = [(x.pub_id, x.shop_name) for x in current_user.shop]
    #     cates = args[0]
    #     self.category_pid.choices = [(x.pub_id, x.name) for x in cates]

    # 归属分类
    category_pid = SelectField(label="归属分类 :",

                               render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                               )
    # 菜品价格
    goods_price = DecimalField(label="菜品价格",
                               render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                               )
    # 菜品描述
    description = StringField(label="菜品描述",
                              render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                              )
    # 月销售额
    # month_sales = IntegerField(label="月销量",
    #                            render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
    #                            )
    # 评分数量
    # rating_count = IntegerField(label="评分数量",
    #                             render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
    #                             )
    # 提示信息
    tips = StringField(label="提示信息",
                       render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                       )
    # 菜品图片
    goods_img = StringField(label="图片",
                            render_kw={"class": "form-control", "placeholder": "", "required": 'required'})


class MenuFoodForm(FlaskForm):
    # 对外ID model -->  goods_id

    # 菜品名称
    goods_name = StringField(label="菜品名称 :",
                             validators=(validators.DataRequired(message="请填写菜品名称"),

                                         ),
                             render_kw={"class": "form-control", "placeholder": "菜品名称!", "required": 'required'}
                             )
    # 菜品评分
    # rating = FloatField(label="菜品评分 :",
    #                     validators=(validators.DataRequired(message=""),
    #
    #                                 ),
    #                     render_kw={"class": "form-control", "placeholder": "菜品名称!", "required": 'required'}
    #                     )
    # 归属店铺
    shop_pid = SelectField(label="归属店铺 :",
                           render_kw={"class": "form-control", "placeholder": "", "required": 'required'},
                           )

    def __init__(self, *args, **kwargs):
        super(MenuFoodForm, self).__init__(*args, **kwargs)

        self.shop_pid.choices = [(x.pub_id, x.shop_name) for x in current_user.shop]
        cates = args[0]
        self.category_pid.choices = [(x.pub_id, x.name) for x in cates]

    # 归属分类
    category_pid = SelectField(label="归属分类 :",

                               render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                               )
    # 菜品价格
    goods_price = DecimalField(label="菜品价格",
                               render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                               )
    # 菜品描述
    description = StringField(label="菜品描述",
                              render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                              )
    # 月销售额
    # month_sales = IntegerField(label="月销量",
    #                            render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
    #                            )
    # 评分数量
    # rating_count = IntegerField(label="评分数量",
    #                             render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
    #                             )
    # 提示信息
    tips = StringField(label="提示信息",
                       render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                       )
    # 菜品图片
    goods_img = StringField(label="图片",
                            render_kw={"class": "form-control"},
                            id="image-url",
                            widget=HiddenInput(),
                            )


class MenuCategoryForm(FlaskForm):
    # pub_id = StringField(label="对外id",
    #                      validators=(validators.Length(max=16, message="至多16个字符"),
    #                                  ),
    #                      render_kw={"class": "form-control disabled", "placeholder": "", "required": 'required'}
    #                      )
    name = StringField(label="分类名称 ;",
                       validators=(validators.Length(max=32, message="至多32个字符"),
                                   ),
                       render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                       )
    description = StringField(label="分类描述 :",
                              validators=(validators.Length(max=128, message="至多128个字符"),
                                          ),
                              render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                              )
    type_accumulation = StringField(label="分类编号 :",
                                    render_kw={"class": "form-control", "placeholder": "", "required": 'required'}
                                    )

    is_default = BooleanField(label="是否默认 :",
                              default=False,
                              )

    # 归属店铺
    # shop_id = db.Column(db.Integer, db.ForeignKey('seller_shop.pub_id'))
    #
    # shop = db.relationship('SellerShop', backref='categories')

    # def __init__(self, *args, **kwargs):
    #     super(MenuCategoryForm, self).__init__(*args, **kwargs)
    #
    #     self.shop_id.choices = [(x.pub_id, x.shop_name) for x in current_user.shop]
    #     cates = args[0]
    #     self.category_id.choices = [(x.pub_id, x.name) for x in cates]

    def __repr__(self):
        return "<MenuCate {}>".format(self.name)
