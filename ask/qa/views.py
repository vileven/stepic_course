from django.shortcuts import render

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotModified
from django.views.decorators.http import require_GET, require_POST
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from qa.models import Answer
from qa.models import Question
from qa.forms import AskForm, AnswerForm, SignUpForm, LoginForm


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
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'question.html', {
        'question': qst,
        'answers': answers,
        'form': form,
    })


def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            ask = form.save()
            url = reverse('question', args=[ask.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask_question.html', {
        'form': form
    })


def question_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = reverse('question', args=[answer.question.id])
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
