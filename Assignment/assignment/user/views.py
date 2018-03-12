from django.shortcuts import render,redirect,get_list_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from user.models import Friend,Users
from user.forms import UsersForm,FriendFrom
from django.urls import reverse_lazy
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

# def add_user(request):
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             cdin = form.save()
#             return redirect('list')
#     else:
#         form = UsersForm()
#     return render(request,'user/add_user.html',{'form':form})

class CreatePostView(CreateView):

    redirect_field_name = 'user/user_detail.html'

    form_class = UsersForm

    model = Users

class UserListView(ListView):
    template_name = 'user/user_list.html'
    context_object_name = 'user_list'
    model = Users

    def get_queryset(self):
        return Users.objects.all()

class UserDetailView(DetailView):
    model = Users

class UserUpdateView(UpdateView):

    redirect_field_name = 'user/user_detail.html'

    form_class = UsersForm

    model = Users

class UserDeleteView(DeleteView):
    model = Users
    success_url = reverse_lazy('user_list')



def add_friend_to_user(request, pk):
    user = get_object_or_404(Users, pk=user_id)
    if request.method == "POST":
        form = FriendFrom(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.user = user
            friend.save()
            return redirect('user_detail', pk=user.user_id)
    else:
        form = FriendFrom()
    return render(request, 'user/friend_form.html', {'form': form})
