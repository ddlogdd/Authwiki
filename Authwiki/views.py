from django.shortcuts import render
# Authwiki/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Authwiki
from django.core.exceptions import PermissionDenied



class AuthwikiListView(ListView):
    model = Authwiki
    template_name = 'authwiki_list.html'

class AuthwikiDetailView(LoginRequiredMixin, DetailView): # new
    model = Authwiki
    template_name = 'authwiki_detail.html'
    context_object_name = 'indiv_post'

class AuthwikiUpdateView(LoginRequiredMixin, UpdateView): # new
    model = Authwiki
    fields = ('name', 'description', )
    template_name = 'authwiki_edit.html'
    login_url = 'login'
'''
def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
'''
    
class AuthwikiDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Authwiki
    template_name = 'authwiki_delete.html'
    success_url = reverse_lazy('authwiki_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs): # new
            obj = self.get_object()
            if obj.author != self.request.user:
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)
    

class AuthwikiCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Authwiki
    template_name = 'authwiki_new.html'
    fields = ('name', 'description','cover' )
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

'''
def authwiki(request, pk):
    authwikis = Authwiki.objects.get(id=pk)
    return render (request, 'authwiki_detail.html', {'authwikis':authwikis})
'''

