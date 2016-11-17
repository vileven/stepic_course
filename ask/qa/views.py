from django.shortcuts import render

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotModified
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from qa.models import Answer
from qa.models import Question


# Create your views here.
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page, paginator


def index(request):
    # questions = Question.objects.all()
    # questions = questions.order_by('-id')
    questions = Question.objects.new()
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('home') + '?page='
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular_questions(request):
    # questions = Question.objects.all()
    # questions = questions.order_by('-rating')
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('popular_questions') + '?page='
    return render(request, 'popular_questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question(request, pk):
    qst = get_object_or_404(Question, id=pk)
    answers = qst.answer_set.all()
    return render(request, 'question.html', {
        'question': qst,
        'answers': answers,
    })


