def code_execution(request):
    if request.method == 'POST':
        get_first_name = request.POST.get('first_name', '')
        eval("exec(\"setname('%s')\")" % get_first_name)