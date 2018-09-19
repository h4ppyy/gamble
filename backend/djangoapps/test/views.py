#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#UTIL
import json

from django.conf import settings
from backend.djangoapps.common.views import common_sample
from backend.djangoapps.common.views import dictfetchall

from backend.models import GambleUser
from backend.models import GambleResult

def test(request):

    o1 = GambleUser.objects.filter(username='h4ppyy')[0]

    o2 = GambleResult.objects.filter().order_by('-regist_date')[0]

    with connections['default'].cursor() as cur:
        query = '''
            select gb_date, gb_round, gb_leftright, gb_threefour, gb_evenodd, bat_money, success, regist_date
            from gamble_bat
            where user_id = '1'
            order by regist_date desc;
        '''
        cur.execute(query)
        rows = cur.fetchall()

    with connections['default'].cursor() as cur:
        query = '''
            select gb_date, gb_round, gb_leftright, gb_threefour, gb_evenodd
            from gamble_result
            order by regist_date desc;
        '''
        cur.execute(query)
        rows2 = cur.fetchall()

    context = {}
    context['username'] = o1.username
    context['money'] = o1.money
    context['batRound'] = int(o2.gb_round)+1
    context['history'] = rows
    context['result'] = rows2[0]
    return render(request, 'test/test.html', context)

def api_bat(request):

    batRound = request.POST.get('batRound')
    batMoney = int(request.POST.get('batMoney'))
    batEvenOdd = request.POST.get('batEvenOdd')
    batThreeFour = request.POST.get('batThreeFour')
    batLeftRight = request.POST.get('batLeftRight')

    print('batRound -> ', batRound)
    print('batMoney -> ', batMoney)

    o1 = GambleUser.objects.filter(username='h4ppyy')[0]
    o2 = GambleUser.objects.filter(username='h4ppyy').update(money=int(o1.money)-int(batMoney))

    with connections['default'].cursor() as cur:
        query = '''
            insert into gamble_bat(user_id, gb_date, gb_round, gb_leftright, gb_threefour, gb_evenodd, bat_money)
            values(1, '2018-09-19', '{batRound}', '{batEvenOdd}', '{batThreeFour}', '{batLeftRight}', {batMoney});
        '''.format(
            batRound=batRound,
            batMoney=batMoney,
            batEvenOdd=batEvenOdd,
            batThreeFour=batThreeFour,
            batLeftRight=batLeftRight
        )
        cur.execute(query)
        rows = cur.fetchall()

    return JsonResponse({'result':'success'})
