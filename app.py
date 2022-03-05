#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        
        print(text)
        
        out = TextBlob(d).sentiment        
        
        return(render_template("index.html", result=out))
        #return(render_template("index.html", result1=out1, result2=out2, result3=out3))
        
    else:
        return(render_template("index.html", result="Hahaha"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[3]:


from textblob import TextBlob

#open text file in read mode
f = open("sample.txt")
 
#read whole file to a string
d = f.read()

TextBlob(d).sentiment

