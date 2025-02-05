from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings


def report(request, corpus_id):
    corpora_url = 'https://' if settings.USE_SSL else 'http://'
    corpora_url += settings.ALLOWED_HOSTS[0]

    return render(
        request,
        'report.html',
        {
            'corpora_host': corpora_url,
            'corpus_id': corpus_id,
        }
    )
