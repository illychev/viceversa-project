from django.shortcuts import render

def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['vice-versa']
	reversed_text = user_text[::-1]
	number_of_spaces = user_text.count(' ')
	number_of_words = number_of_spaces+1
	return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'numberofwords': number_of_words})