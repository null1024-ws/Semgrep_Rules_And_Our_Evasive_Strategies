def code_execution(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        def setname():
            return first_name
        #BAD -- Allow user to define code to be run.
        exec("setname('%s')" % setname())