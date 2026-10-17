import threading

job = {"done": False, "result": None, "msg": ""}

def say(text):
    job["msg"] = text       # text update to the UI

def runJob(func):
    try:
        job["result"] = func(say)
    except Exception as e:
        job["result"] = None
        job["msg"] = "Error: " + str(e)
    job["done"] = True

def startThread(func):
    job["done"] = False
    job["result"] = None
    job["msg"] = ""
    t = threading.Thread(target=runJob, args=(func,))
    t.daemon = True
    t.start()