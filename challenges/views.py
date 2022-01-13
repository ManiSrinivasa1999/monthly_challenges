from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat only fruit for entire month',
    'february': 'Walk for atleast 20 min every day',
    'march': 'Code atleast one hour everyday',
    'april': 'Meditate 15 min every day',
    'may': 'Start learning new technology',
    'june': 'Walk for atleast 20 min every day',
    'july': 'Eat only fruit for entire month',
    'august': 'Walk for atleast 20 min every day',
    'september': 'Code atleast one hour everyday',
    'october': 'Meditate 15 min every day',
    'november': 'Start learning new technology',
    'december': 'Walk for atleast 20 min every day',
}


# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalize_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalize_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month": month,
        })
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported.</h1>')
