from django.shortcuts import render, redirect
from .models import Campaign, Lead
from .forms import CampaignForm, LeadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'marketing_app/campaign_list.html', {'campaigns': campaigns})

def campaign_create(request):
    form = CampaignForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('campaign_list')
    return render(request, 'marketing_app/form.html', {'form': form})

def lead_list(request, campaign_id):
    leads = Lead.objects.filter(campaign_id=campaign_id)
    return render(request, 'marketing_app/lead_list.html', {'leads': leads})

def lead_create(request, campaign_id):
    form = LeadForm(request.POST or None, initial={'campaign': campaign_id})
    if form.is_valid():
        form.save()
        return redirect('lead_list', campaign_id=campaign_id)
    return render(request, 'marketing_app/form.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=uname, password=passwd)
        if user:
            login(request, user)
            return redirect('campaign_list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'marketing_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
