from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson, Enrollment, Submission, Question, Choice


def index(request):
    courses = Course.objects.all()
    return render(request, 'onlinecourse/index.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/course_detail.html', {'course': course})


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    enrollment = Enrollment.objects.filter(
        user=request.user,
        course=course
    ).first()

    submission = Submission.objects.create(enrollment=enrollment)

    for key in request.POST:
        if key.startswith('choice'):
            choice_id = request.POST[key]
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)

    submission.save()

    return show_exam_result(request, course_id, submission.id)


def show_exam_result(request, course_id, submission_id):

    submission = Submission.objects.get(pk=submission_id)

    questions = Question.objects.filter(
        lesson__course_id=course_id
    )

    score = submission.is_get_score()

    context = {
        'questions': questions,
        'score': score
    }

    return render(
        request,
        'onlinecourse/exam_result_bootstrap.html',
        context
    )
