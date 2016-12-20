from django.http import JsonResponse
from django.shortcuts import render
#from django.core.context_processors import csrf

# Create your views here.

def index(request):
	return render(request, 'main.html')


def event_cmd_json(request):

	jsonResponse = {}

	if request.is_ajax():
		if request.method == 'GET':
			data = request.GET.dict()

			if data['cmd'] == 'menu':
				jsonResponse['menu'] = []
				jsonResponse['menu'].append("<b class='out-label'>menu:</b>")
				jsonResponse['menu'].append("<pre class='out-text'>	menu 			- This message</pre>")
				jsonResponse['menu'].append("<pre class='out-text'>	about 			- Summary of me</pre>")
				jsonResponse['menu'].append("<pre class='out-text'>	projects 		- </pre>")
				jsonResponse['menu'].append("<pre class='out-text'>	skills 			- What I can do</pre>")
				jsonResponse['menu'].append("<pre class='out-text'>	github 			- </pre>")
				jsonResponse['menu'].append("<pre class='out-text'>	contacts 		- Contact me</pre>")
				jsonResponse['menu'].append("<pre class='out-text'>	credits 		- Credits for this website</pre>")

			if data['cmd'] == 'about':
				jsonResponse['about'] = []
				jsonResponse['about'].append("<b class='out-label'>about</b>")
				jsonResponse['about'].append("<pre class='out-text'>	Name: 			Evgeniy Chebotkin</pre>")
				jsonResponse['about'].append("<pre class='out-text'>	DOB: 			20.02.1989</pre>")
				jsonResponse['about'].append("<pre class='out-text'>	Location: 		Saratov, Russian Federation</pre>")

			if data['cmd'] == 'projects':
				jsonResponse['projects'] = []
				jsonResponse['projects'].append("<b class='out-label'>projects:</b>")

			if data['cmd'] == 'skills':
				jsonResponse['skills'] = []
				jsonResponse['skills'].append("<b class='out-label'>skills:</b>")
				jsonResponse['skills'].append("<pre class='out-text'>	c, c++, Qt, python, JS, HTML, CSS, Linux</pre>")


			if data['cmd'] == 'github':
				jsonResponse['github'] = []
				jsonResponse['github'].append("<b class='out-label'>github:</b>")
				jsonResponse['github'].append("<pre class='out-text'>	<a href='http://www.github.com/shepherd4'\
												style='color: white'>http://www.github.com/shepherd4</a></pre>")
			if data['cmd'] == 'contacts':
				jsonResponse['contacts'] = []
				jsonResponse['contacts'].append("<b class='out-label'>contacts:</b>")
				jsonResponse['contacts'].append("<pre class='out-text'>	email:			chebotkines@gmail.com</pre>")

			if data['cmd'] == 'credits':
				jsonResponse['credits'] = []
				jsonResponse['credits'].append("<b class='out-label'>credits:</b>")
				jsonResponse['credits'].append("<pre class='out-text'>	Site build by Chebotkin E.S.</pre>")
				jsonResponse['credits'].append("<pre class='out-text'>	Using:</pre>")
				jsonResponse['credits'].append("<pre class='out-text'>	 * Jquery Terminal Emulator by Jakub Jankiewicz: <a href='http://terminal.jcubic.pl' style='color: white'>http://terminal.jcubic.pl</a></pre>")
				jsonResponse['credits'].append("<pre class='out-text'>	 * Django1.8:</pre>")

	return JsonResponse(jsonResponse)


def event_init_json(request):
	jsonResponse = {}

	if request.is_ajax():
		if request.method == 'GET':

			jsonResponse = {
				'cmd_list': ['menu', 'about','projects','skills', 'github', 'contacts', 'credits' ],
			}

	return JsonResponse(jsonResponse)

