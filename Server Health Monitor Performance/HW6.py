from wsgiref.simple_server import make_server
import psutil,datetime

def health_monitor(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    message = "<h1>Welcome to the Server Health monitor</h1>"
    message +="<table style=\"width:100%\">"
    message += "<tr>"
    message +="<td style=\"background-color:blue\"><strong>BOOT TIME:</strong></td>"
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    message +="<td style=\"background-color:blue\">"+str(boot_time)+"</td>"
    message +="</tr>"

    cpu_util = psutil.cpu_percent(interval=1, percpu=True)
    message += "<tr style=\"background-color:green\"><th rowspan=\"4\"><strong>CPU UTILIZATION</strong></th>"
    i=1
    
    for cpu in cpu_util:
        if cpu < 20:
             message += "<td style=\"background-color:seagreen\">"
        else:
            message += "<td style=\"background-color:pink\">"
            
        message += "CPU {} : {}%".format(i, cpu)
        
        i+=1
        message += "</td></tr>"
    
    mem = psutil.virtual_memory()
    message += "<tr>"
    message +="<td style=\"background-color:blue\"><strong>AVAILABLE MEMORY:</strong></td>"
    message +="<td style=\"background-color:blue\">"+str(mem.available)+"</td>"
    message +="</tr>"
    message += "<tr>"
    message +="<<td style=\"background-color:blue\"><strong>USED MEMORY:</strong></td>"
    message +="<td style=\"background-color:blue\">"+str(mem.used)+"</td>"
    message +="</tr>"
    message +="<td style=\"background-color:blue\"><strong>USED PERCENTAGE:</strong></td>"
    message +="<td style=\"background-color:blue\">"+str(mem.percent)+"</td>"
    message +="</tr>"

    return[bytes(message,'utf-8')]

httpd = make_server('', 8000,health_monitor)
print("Serving on port 8000...")


httpd.serve_forever()
