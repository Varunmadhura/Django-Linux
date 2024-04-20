
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import paramiko
import subprocess
import os
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('scenario')
    return render(request, 'testapp/login.html')

def scenario(request):
    return render(request,"testapp/page1.html")




def execute_command(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        command = request.POST.get('command', '')

        try:

            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=hostname, username=username, password=password)


            stdin, stdout, stderr = ssh_client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')

            
            ssh_client.close()

            return render(request, 'testapp/page1.html', {'output': output, 'error': error})
        except paramiko.AuthenticationException:
            error = "Authentication failed. Please check your credentials."
            return render(request, 'testapp/page1.html', {'error': error})
        except Exception as e:
            error = f"An error occurred: {str(e)}"
            return render(request, 'testapp/page1.html', {'error': error})

    return render(request, 'testapp/page1.html')
