from django.shortcuts import render

# Create your views here.
def Welcome_Page(request):
	return render(request, 'MyApp/Welcome_Page.html')

def Thanks_Page(request):
	return render(request, 'MyApp/Thanks_Page.html')

def MyTempView(request):
	return render(request, 'MyApp/MyTempView.html')
