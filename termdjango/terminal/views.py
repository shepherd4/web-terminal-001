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
				jsonResponse['menu'].append({"value":"<b>menu:</b>\
					<pre>	menu 			- This message</pre>\
					<pre>	about 			- Summary of me</pre>\
					<pre>	projects 		- </pre>\
					<pre>	skills 			- What I can do</pre>\
					<pre>	github 			- </pre>\
					<pre>	contacts 		- Contact me</pre>\
					<pre>	credits 		- Credits for this website</pre>"})

			if data['cmd'] == 'about':
				jsonResponse['about'] = []
				jsonResponse['about'].append({"value":"<b>about</b>\
					<pre>	Name: 			Evgeniy Chebotkin</pre>\
					<pre>	DOB: 			20.02.1989</pre>\
					<pre>	Location: 		Saratov, Russian Federation</pre>"})



			if data['cmd'] == 'projects':
				jsonResponse['projects'] = []
				jsonResponse['projects'].append({"label":"<b>projects:</b>", "value":""})

			if data['cmd'] == 'skills':
				jsonResponse['skills'] = []
				jsonResponse['skills'].append({"value":"<b>skills:</b>\
												<pre>	c, c++, Qt, python, JS, HTML, CSS, Linux</pre>"})				


			if data['cmd'] == 'github':
				jsonResponse['github'] = []
				jsonResponse['github'].append({"value":"<b>github:</b>\
												<pre>	<a href='http://www.github.com/shepherd4'\
												style='color: white'>http://www.github.com/shepherd4</a></pre>"})

			if data['cmd'] == 'contacts':
				jsonResponse['contacts'] = []
				jsonResponse['contacts'].append({"value":"<b>contacts:</b>\
					<pre>	email:			chebotkines@gmail.com</pre>"})

			if data['cmd'] == 'credits':
				jsonResponse['credits'] = []
				jsonResponse['credits'].append({"value":"<b>credits:</b>\
						<pre>	Site build by Chebotkin E.S.</pre>\
						<pre>	Using:</pre>\
						<pre>	 * Jquery Terminal Emulator by Jakub Jankiewicz: <a href='http://terminal.jcubic.pl'>http://terminal.jcubic.pl</a></pre>\
						<pre>	 * Django1.8:</pre>\
						"})				
	
	print(jsonResponse)
	return JsonResponse(jsonResponse)


def event_init_json(request):
	data = {}
	jsonResponse = {}

	if request.is_ajax():
		if request.method == 'GET':
	
			jsonResponse = {
				'cmd_list': ['menu', 'about','projects','skills', 'github', 'contacts', 'credits' ],
			}

	return JsonResponse(jsonResponse)

