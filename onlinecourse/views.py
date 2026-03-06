from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Question, Choice


# Homepage - list all courses
def index(request):
    course_list = Course.objects.all()
    return render(request, 'onlinecourse/index.html', {
        'course_list': course_list
    })


# Course detail page with lessons and quiz
def course_detail(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    lessons = Lesson.objects.filter(course=course)

    questions = Question.objects.filter(lesson__course=course)

    return render(request, 'onlinecourse/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'questions': questions
    })


# Handle quiz submission
def submit(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':

        selected_choices = []

        for key in request.POST:

            if key == 'csrfmiddlewaretoken':
                continue

            choice_id = int(request.POST[key])
            selected_choices.append(choice_id)

        choices = Choice.objects.filter(id__in=selected_choices)

        correct_choices = choices.filter(is_correct=True)

        if len(choices) > 0:
            score = len(correct_choices) / len(choices) * 100
        else:
            score = 0

        questions = Question.objects.filter(lesson__course=course)

        return render(request, 'onlinecourse/result.html', {
            'score': score,
            'questions': questions
        })

    return render(request, 'onlinecourse/course_detail.html', {
        'course': course
    })
