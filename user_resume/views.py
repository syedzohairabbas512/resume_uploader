from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import ResumeForm
from .models import Resume


class Homeview(View):

    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'index.html', {'candidates': candidates, "form": form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("yes")
            return redirect('/')
        else:
            print("no")
            print(form.errors)  # Print form errors to understand the issue
            return render(request, 'index.html', {"form": form})


class CandidateView(View):
    def get(self, request, pk):
        try:
            candidate = Resume.objects.get(pk=pk)
            print(candidate.name)
            return render(request, 'candidates.html', {'candidate': candidate})
        except Resume.DoesNotExist:
            return HttpResponse("Candidate not found", status=404)
