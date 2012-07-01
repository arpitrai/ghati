from django.shortcuts import render_to_response
from django.template import RequestContext
from ghatiparty.models import Songs

def index(request, mood):
    mood_match = {'im-too-cool-for-this': 'G1', 'ghatipan-in-control': 'G2', 'ghatipan-heaven': 'G3'}
    if mood == 'mix-it-all':
        playlist = Songs.objects.order_by('?')
    else: 
        playlist = Songs.objects.filter(mood=mood_match[mood]).order_by('?')
    return render_to_response('player.html', { 'playlist': playlist }, context_instance=RequestContext(request))
