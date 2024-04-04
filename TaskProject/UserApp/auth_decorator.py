from django.shortcuts import redirect

def login_required(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped_view


def loggedin_user(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('my-task')
        return view_function(request, *args, **kwargs)
    return wrapped_view