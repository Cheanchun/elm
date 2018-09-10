from wtforms import *

from flask_wtf import FlaskForm

from apps.model.shop_model import SellerShop


class ShopForm(FlaskForm):

    shop_name = StringField(label="店铺名称 :",
                            validators=(validators.DataRequired(message="请填写店铺名称"),

                                        ),
                            render_kw={"class": "form-control", "placeholder": "请填写店铺名称!", "required": 'required'}
                            )
    brand = BooleanField(label="是否是品牌 :",
                         default=False,
                         render_kw={"class": "radio"}
                         )
    on_time = BooleanField(label="是否准时送达 :",

                           default=False,
                           render_kw={"class": "radio"}
                           )
    fengniao = BooleanField(label="是否蜂鸟配送 :",
                            default=False,
                            render_kw={"class": "radio"}
                            )
    bao = BooleanField(label="是否保险 :",
                       default=False,
                       render_kw={"class": "radio"}
                       )
    piao = BooleanField(label="是否有发票 :",
                        default=True,
                        render_kw={"class": "radio"}
                        )
    zhun = BooleanField(label="是否准标识 :",
                        default=False,
                        render_kw={"class": "radio ", "placeholder": "是否是品牌!"}
                        )
    start_send = StringField(label="起送价格 :",
                             render_kw={"class": "form-control", "placeholder": "起送价格!"}
                             )
    send_cost = StringField(label="配送费 :",
                            render_kw={"class": "form-control", "placeholder": "配送费!"}
                            )
    notice = StringField(label="店铺公告 :",
                         render_kw={"class": "form-control", "placeholder": "店铺公告!"}
                         )
    discount = StringField(label="优惠信息 :",
                           render_kw={"class": "form-control", "placeholder": "优惠信息!"}
                           )

    # 店铺名称唯一性
    # def validate_shop_name(self, shop_name):
    #     if SellerShop.query.filter_by(shop_name=shop_name.data).first():
    #         raise validators.ValidationError(message="店铺名称已存在!")




