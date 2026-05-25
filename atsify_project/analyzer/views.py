from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume, Analysis
from .services.pdf_parser import extract_text_from_pdf
from .services.groq_client import analyze_resume_with_llm

@login_required
def analyse_view(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        job_description = request.POST.get('job_description')
        
        if not resume_file or not job_description:
            messages.error(request, "Please provide both a resume PDF and a job description.")
            return redirect('analyse')
            
        if not resume_file.name.lower().endswith('.pdf'):
            messages.error(request, "Only PDF files are supported.")
            return redirect('analyse')

        #Save Resume Model
        resume = Resume.objects.create(
            user=request.user,
            file=resume_file,
            parsed_text=""
        )
        
        #Extract Text
        parsed_text = extract_text_from_pdf(resume.file.path)
        if not parsed_text:
            messages.error(request, "Could not extract text from the PDF. Please try a different file.")
            return redirect('analyse')
            
        resume.parsed_text = parsed_text
        resume.save()
        
        #Call Groq LLaMA 3
        try:
            ai_response = analyze_resume_with_llm(parsed_text, job_description)
            
            #Save Analysis Result
            analysis = Analysis.objects.create(
                user=request.user,
                resume=resume,
                job_description=job_description,
                match_score=ai_response.get("match_score", 0),
                missing_keywords=ai_response.get("missing_keywords", []),
                strengths=ai_response.get("strengths", []),
                suggestions=ai_response.get("suggestions", "No suggestions provided.")
            )
            
            #Redirect to results
            return redirect('results', analysis_id=analysis.id)
            
        except Exception as e:
            messages.error(request, f"Analysis failed: {str(e)}")
            return redirect('analyse')
            
    return render(request, 'analyzer/analyse.html')

@login_required
def results_view(request, analysis_id):
    analysis = get_object_or_404(Analysis, id=analysis_id, user=request.user)
    return render(request, 'analyzer/results.html', {'analysis': analysis})

@login_required
def dashboard_view(request):
    analyses = Analysis.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'analyzer/dashboard.html', {'analyses': analyses})

@login_required
def delete_analysis_view(request, analysis_id):
    if request.method == 'POST':
        analysis = get_object_or_404(Analysis, id=analysis_id, user=request.user)
        analysis.delete()
        messages.success(request, "Analysis deleted successfully.")
    return redirect('dashboard')
