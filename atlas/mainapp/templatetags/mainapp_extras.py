from django import template
from mainapp.models import Obj1Ai,Obj2Ai

register = template.Library()


@register.filter(name='to_string')
def to_string(date):
    f_str = ''
    f_str += date
    f_str = str(f_str)
    print(type(date))
    print(date)
    return f'{f_str}'

@register.simple_tag()
def get_errors_1(id):
    return Obj1Ai.objects.filter(idai=id,err__gt=0,sts=1).count()

@register.simple_tag()
def get_errors_2(id):
    return Obj2Ai.objects.filter(idai=id,err__gt=0,sts=1).count()
