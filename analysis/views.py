from django.shortcuts import redirect, render
from django.db.models import Sum

from authentication.models import Profile
from analysis.models import EmotionsStat, RegularityStat, Incentive
from journal.models import Zen
from analysis.forms import QuestionnaireForm


def stats_page_view(request):
    emotion_data = dict()
    emotion_data_last = dict()
    emotion_data_weekly = dict()
    emotion_data_monthly = dict()
    total_entries = EmotionsStat.objects.filter(user=request.user).count()
    regularity_model = RegularityStat.objects.filter(user=request.user)
    regularity_model_x, regularity_model_y = list(), list()
    zen_model = Zen.objects.get(user=request.user)
    for x in regularity_model.iterator():
        regularity_model_x.append(x.date.day)
    for y in regularity_model.iterator():
        regularity_model_y.append(float(y.time_spent))
    regularity_model_len = regularity_model.count()
    if total_entries > 0:
        emotion_queryset = EmotionsStat.objects.filter(user=request.user)
        emotion_data['Happy'] = float(emotion_queryset.aggregate(Sum('happy'))['happy__sum'])
        emotion_data['Angry'] = float(emotion_queryset.aggregate(Sum('angry'))['angry__sum'])
        emotion_data['Sad'] = float(emotion_queryset.aggregate(Sum('sad'))['sad__sum'])
        emotion_data['Surprise'] = float(emotion_queryset.aggregate(Sum('surprise'))['surprise__sum'])
        emotion_data['Fear'] = float(emotion_queryset.aggregate(Sum('fear'))['fear__sum'])
        emotion_queryset_last = EmotionsStat.objects.filter(user=request.user).first()
        emotion_data_last['Happy'] = float(emotion_queryset_last.happy)
        emotion_data_last['Angry'] = float(emotion_queryset_last.angry)
        emotion_data_last['Sad'] = float(emotion_queryset_last.sad)
        emotion_data_last['Surprise'] = float(emotion_queryset_last.surprise)
        emotion_data_last['Fear'] = float(emotion_queryset_last.fear)
        print(emotion_data_last)
    if total_entries >= 3:
        emotion_queryset_weekly = EmotionsStat.objects.filter(user=request.user)[:7]
        emotion_data_weekly['Happy'] = float(emotion_queryset_weekly.aggregate(Sum('happy'))['happy__sum'])
        emotion_data_weekly['Angry'] = float(emotion_queryset_weekly.aggregate(Sum('angry'))['angry__sum'])
        emotion_data_weekly['Sad'] = float(emotion_queryset_weekly.aggregate(Sum('sad'))['sad__sum'])
        emotion_data_weekly['Surprise'] = float(emotion_queryset_weekly.aggregate(Sum('surprise'))['surprise__sum'])
        emotion_data_weekly['Fear'] = float(emotion_queryset_weekly.aggregate(Sum('fear'))['fear__sum'])
    if total_entries >= 7:
        emotion_queryset_monthly = EmotionsStat.objects.filter(user=request.user)[:30]
        emotion_data_monthly['Happy'] = float(emotion_queryset_monthly.aggregate(Sum('happy'))['happy__sum'])
        emotion_data_monthly['Angry'] = float(emotion_queryset_monthly.aggregate(Sum('angry'))['angry__sum'])
        emotion_data_monthly['Sad'] = float(emotion_queryset_monthly.aggregate(Sum('sad'))['sad__sum'])
        emotion_data_monthly['Surprise'] = float(emotion_queryset_monthly.aggregate(Sum('surprise'))['surprise__sum'])
        emotion_data_monthly['Fear'] = float(emotion_queryset_monthly.aggregate(Sum('fear'))['fear__sum'])
    context = {'zen_model': zen_model, 'emotion_data': emotion_data, 'emotion_data_weekly': emotion_data_weekly, 'emotion_data_monthly': emotion_data_monthly, 'emotion_data_last': emotion_data_last, 'regularity_model_len': regularity_model_len, 'regularity_model': regularity_model, 'regularity_model_x': regularity_model_x, 'regularity_model_y': regularity_model_y}
    return render(request, 'analysis/stats.html', context=context)


def quiz_page_view(request):
    profile_model = Profile.objects.get(user=request.user)
    incentive_model = Incentive.objects.get(user=request.user)
    question_form = QuestionnaireForm()
    if request.method == 'POST':
        question_form = QuestionnaireForm(request.POST)
        if question_form.is_valid():
            q1 = question_form.cleaned_data['q1']
            q2 = question_form.cleaned_data['q2']
            q3 = question_form.cleaned_data['q3']
            q4 = question_form.cleaned_data['q4']
            q5 = question_form.cleaned_data['q5']
            q6 = question_form.cleaned_data['q6']
            q7 = question_form.cleaned_data['q7']
            q8 = question_form.cleaned_data['q8']
            q9 = question_form.cleaned_data['q9']
            q10 = question_form.cleaned_data['q10']
            q11 = question_form.cleaned_data['q11']
            q12 = question_form.cleaned_data['q12']
            q13 = question_form.cleaned_data['q13']
            q14 = question_form.cleaned_data['q14']
            q15 = question_form.cleaned_data['q15']
            q16 = question_form.cleaned_data['q16']
            q17 = question_form.cleaned_data['q17']
            q18 = question_form.cleaned_data['q18']
            q19 = question_form.cleaned_data['q19']
            q20 = question_form.cleaned_data['q20']
            IN, E, S, N, T, F, J, P = 0, 0, 0, 0, 0, 0, 0, 0
            for e in [q1, q5, q9, q13, q17]:
                if e == '1':
                    E += 1
                else:
                    IN += 1
            for e in [q2, q6, q10, q14, q18]:
                if e == '1':
                    S += 1
                else:
                    IN += 1
            for e in [q3, q7, q11, q15, q19]:
                if e == '1':
                    T += 1
                else:
                    F += 1
            for e in [q4, q8, q12, q16, q20]:
                if e == '1':
                    J += 1
                else:
                    P += 1
            personality = str('I' if IN > E else 'E') + str('S' if S > N else 'N') + str('T' if T > F else 'F') + str('J' if J > P else 'P')
            print(personality)
            incentive_model.registrar = True
            profile_model.personality = personality
            profile_model.save()
            incentive_model.save()
            return redirect('profile_edit')
    return render(request, 'analysis/quiz.html', {'profile_model': profile_model, 'incentive_model': incentive_model, 'form': question_form})


def incentives_page_view(request):
    return render(request, 'analysis/incentives.html')


def suggestions_page_view(request):
    profile_model = Profile.objects.get(user=request.user).personality
    emotion = EmotionsStat.objects.filter(user=request.user).first().emotion
    generalized_suggestions = []
    failure = False
    if (not profile_model) or profile_model == '':
        failure = True
    if emotion == 'Happy':
        if 'I' in profile_model:
            generalized_suggestions.append('The immediate thing that you might want to avoid is following the urge to \
                be in extroverted environments just because others are doing so as well. You know what makes you comfortable.\
                Better stick to that.')
            generalized_suggestions.append('A lot of grief comes from unresolved issues that you might be putting underneath \
                some cover to avoid feeling them. Either encounter those issues head on, resolve them or try to let go.')
            generalized_suggestions.append('If you\'re hungry, enjoy a solitary meal and watch your favourite show or try \
                watching certain movies.')
            generalized_suggestions.append('Spend time with someone who is very close to you. Avoid people around whom you do \
                not want to be.')
            generalized_suggestions.append('When something bad happens, almost everything seems to fall apart. You start \
                disliking yourself for more reasons than you actually were upset about in the first place. At such moments, shut \
                your mind off and do not think.')
        elif 'E' in profile_model:
            generalized_suggestions.append('Unless you are extremely upset or angry, you may not want to stay alone at such \
                times. Get together with certain close friends or a group to talk it out until it makes you feel good.')
            generalized_suggestions.append('You might want to be around people who approve or value your sense of independence \
                and respect it.')
            generalized_suggestions.append('Catch up with old friends.')
            generalized_suggestions.append('Go to a place that holds good memories with the same people with whom we had been there \
                before.')

    elif emotion == 'Sad':
        pass
    return render(request, 'analysis/suggestions.html', {'profile_model': profile_model, 'failure': failure})
