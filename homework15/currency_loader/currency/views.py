from django.shortcuts import render
import datetime
import requests

from .forms import MyForm
# from django.template import RequestContext
# from django.views.generic import View
# from django.contrib import messages


# Create your views here.
def index(request):
    today = datetime.date.today()
    today_format = today.strftime("%Y-%m-%d")
    delta = datetime.timedelta(days=14)

    if request.method == 'POST':
        form = MyForm(request.POST)
        # if form.is_valid():
        input_date = form.data['date']
        set_date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
        count_date = set_date - delta
        result_date = count_date.strftime("%Y-%m-%d")

        r_jsn = requests.get(
            'http://moex.com/iss/engines/currency/markets/selt/securities/'
            'USD000UTSTOM/candles.json?from={0}&till={1}&interval=60&start=0'.format(result_date, set_date)
        )
        jsn = r_jsn.json()
        data = jsn.get('candles').get('data')

        return render(request, 'currency/index.html', {'result_date': result_date, 'now': input_date, 'data': data, })
    else:
        return render(request, 'currency/index.html', {'now': today_format})






