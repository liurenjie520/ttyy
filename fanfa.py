import json

import config
from json import load as load_json
def jk():
    result = []
    file_object_yj = open(file=config.Default.yj, mode='rb')
    # file_object_pzbj = open(file=config.Default.other, mode='rb')
    yj_original = load_json(file_object_yj)
    # pzbj_original = load_json(file_object_pzbj)
    fjtx=yj_original['papers']
    fjtxstr = ", ".join(repr(e) for e in fjtx)
    print(fjtxstr)
    # jjson=json.load(yj_original)
    kk = yj_original['days']
    # jjson['days']
    # jjson=json.load(kk)
    # print(type(kk))

    dd = ", ".join(repr(e) for e in kk)
    # ff=dd.replace("'", '\"')
    # opo=ff.replace("True","\"休息日\"")
    # xx=opo.replace("False","\"补班\"")
    # ddjson=json.load(xx)
    # ddjson=", ".join(xx)
    # print(type(ddjson))
    opo = dd.replace("{", '(')
    opo2 = opo.replace("}", ')')
    yd = opo2.replace("'date':", "")
    # print(yd)
    ff = yd.replace(", 'isOffDay': True", ",\'假期(休)\',url")
    ety = ff.replace(", 'isOffDay': False", ",\'补班\',url")


    ffas = ety.replace("name': '", "")
    sdf = ffas.replace("-", "")
    urla=sdf.replace("url", fjtxstr)
    dfga = "[" + urla + "]"
    dicee=eval(dfga)
    # print(dicee)

    #
    # # print(type(dd))
    # # print(dfga)
    #
    return dicee


#
# s=''
# result = []
# for i in kk:
#     data=i
#     for j in data:
#         tmp1=data['date']+data['name']+str(data['isOffDay'])
#
#         # tmp0=data['name']
#         # tmp3=data['isOffDay']
#         # tmp3=str(tmp3)
#         # tmp2 = (tmp1, tmp0,tmp3)
#         # tmp2=str(tmp2)
#         # s=s+tmp2
#         # result.append(tmp2)
#         print(tmp1)
#


if __name__ == '__main__':
    a=jk()
    print(a)



