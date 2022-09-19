from django import template

register = template.Library()


@register.filter
def translate_num(value):
    value = str(value)
    en_to_fa = value.maketrans('0987654321', '۰۹۸۷۶۵۴۳۲۱')
    return value.translate(en_to_fa)
