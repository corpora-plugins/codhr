from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.conf import settings
from corpus import get_corpus

@xframe_options_exempt
def report(request, corpus_id):
    corpora_url = 'https://' if settings.USE_SSL else 'http://'
    corpora_url += settings.ALLOWED_HOSTS[0]
    is_embedded = 'embedded' in request.GET
    award_results = []
    project_results = []
    stakeholder_results = []
    period_results = []
    event_results = []
    attendance_results = []

    corpus = get_corpus(corpus_id)
    if corpus:
        award_query = {
            'content_type': 'Award',
            'general_query': '*',
            'fields_sort': [{'award_period.timespan': {'order': 'ASC'}}],
            'page': 1,
            'page_size': 5000,
        }
        award_results = corpus.search_content(**award_query)

        project_query = {
            'content_type': 'Project',
            'general_query': '*',
            'page': 1,
            'page_size': 5000,
        }
        project_results = corpus.search_content(**project_query)

        stakeholder_query = {
            'content_type': 'Stakeholder',
            'general_query': '*',
            'page': 1,
            'page_size': 5000,
        }
        stakeholder_results = corpus.search_content(**stakeholder_query)

        period_query = {
            'content_type': 'Period',
            'general_query': '*',
            'fields_sort': [{'timespan': {'order': 'ASC'}}],
            'page': 1,
            'page_size': 5000,
        }
        period_results = corpus.search_content(**period_query)

        event_query = {
            'content_type': 'Event',
            'general_query': '*',
            'fields_sort': [{'period.timespan': {'order': 'ASC'}}],
            'page': 1,
            'page_size': 5000,
        }
        event_results = corpus.search_content(**event_query)

        attendance_query = {
            'content_type': 'Attendance',
            'general_query': '*',
            'page': 1,
            'page_size': 5000,
        }
        attendance_results = corpus.search_content(**attendance_query)

    return render(
        request,
        'report.html',
        {
            'corpora_host': corpora_url,
            'corpus_id': corpus_id,
            'is_embedded': is_embedded,
            'award_data': award_results,
            'project_data': project_results,
            'stakeholder_data': stakeholder_results,
            'period_data': period_results,
            'event_data': event_results,
            'attendance_data': attendance_results,
        }
    )
