# quiz/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Question, Option, QuizAttempt  # 👈 QuizAttempt import गर्न नबिर्सनुहोस्

def quiz_by_category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    # Session सुरुवात गर्ने
    if 'current_question_index' not in request.session or request.session['category_slug'] != category_slug:
        request.session['current_question_index'] = 0
        request.session['correct_answers_count'] = 0
        request.session['category_slug'] = category_slug
        request.session['question_ids'] = list(category.questions.values_list('id', flat=True))
        request.session['answered'] = False  # initially not answered
        request.session.save()

    question_ids = request.session.get('question_ids', [])
    total_questions = len(question_ids)
    current_index = request.session['current_question_index']

    # ✅ सबै प्रश्न सकिएपछि result देखाउने र score save गर्ने
    if current_index >= total_questions:
        correct = request.session.get('correct_answers_count', 0)
        half = total_questions // 2

        # ✅ Attempt save गर्ने (user logged in भएमा)
        if request.user.is_authenticated:
            QuizAttempt.objects.create(
                user=request.user,
                category=category,
                score=correct,
                total_questions=total_questions
            )

        context = {
            'category': category,
            'correct_count': correct,
            'total_questions': total_questions,
            'half_total_questions': half,
        }

        # ✅ Session हटाउने
        for key in ['current_question_index', 'correct_answers_count', 'category_slug', 'question_ids', 'answered']:
            request.session.pop(key, None)

        return render(request, 'quiz/quiz_result.html', context)

    # अहिलेको प्रश्न
    question_id = question_ids[current_index]
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        if 'submit_answer' in request.POST:
            selected_option_id = request.POST.get('answer')
            if selected_option_id:
                selected_option = get_object_or_404(Option, id=selected_option_id, question=question)
                explanation = selected_option.explanation
                correct_option = question.options.filter(is_correct=True).first()

                if selected_option.is_correct:
                    messages.success(request, f"✅ सहि उत्तर! {explanation}")
                    request.session['correct_answers_count'] += 1
                else:
                    messages.error(request, f"❌ गलत उत्तर! सहि उत्तर: {correct_option.text}. {explanation}")

                request.session['answered'] = True
                request.session.save()

        elif 'next_question' in request.POST:
            request.session['current_question_index'] += 1
            request.session['answered'] = False
            request.session.save()
            return redirect('quiz:quiz_by_category', category_slug=category_slug)

    context = {
        'category': category,
        'question': question,
        'current_question_index': current_index + 1,
        'total_questions': total_questions,
        'answered': request.session.get('answered', False),
    }
    return render(request, 'quiz/quiz_by_category.html', context)


def quiz_list_view(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories,
    }
    return render(request, 'quiz/quiz_list.html', context)
