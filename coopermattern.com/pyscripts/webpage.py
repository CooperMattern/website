#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tablecreate import createtable as ct

with open('html/index.html','w') as f:
    s = '''<!DOCTYPE html>
                <head>
                    <style>
                        table, th, td {
                            border: 1px solid black;
                            border-collapse: collapse;
                        }
                        table {
                            width:100%;
                        }
                    </style>
                </head>
                <body>
                    <form action="refresh.php" method="get">
                        <input type="submit" value="Run me now!">
                    </form>
                    '''+ct()+'''
                </body>
            </html>'''
    f.write(s)


# In[ ]:




