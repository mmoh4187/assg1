from selenium import webdriver
import threading
import sign_up 

def before_all(ctx):
    ctx.server = sign_up
    ctx.address = sign_up.address
    ctx.thread = threading.Thread(target=ctx.server.serve_forever)
    ctx.thread.start()  # start flask app server
    ctx.browser = webdriver.Firefox()

def after_all(ctx):
    ctx.browser.get(ctx.address + "/shutdown") # shut down flask app server
    ctx.thread.join()
    ctx.browser.quit()
