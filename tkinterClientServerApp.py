# Import module
from tkinter import *

from urllib.request import urlopen
from re import *

def select_radio():
    if (i.get() == 'abcnews'):
        request_url = urlopen('https://www.abc.net.au/news/politics/')
        html = request_url.read().decode("utf8")
        between_script_tags = re.findall('<a class="_3T9Id _2msBb vOtE5 _1wNLk _3i4V4 _22UE5" href="/news/2021-07-08/perth-casino-royal-commission-public-submissions/100275954" data-component="Link">(.*?)</a>',html)
        for heading in between_script_tags:
            #print(eachP)
            pass
        heading = heading.replace('&#x27;',' ')

        between_script_tags2 = re.findall('<div class="_2O40L _3XvRm _3BwtN _2eB4R _1yL-m" data-component="CardDescription">(.*?)</div>',html)
        for para in between_script_tags2:
            #print(eachP)
            pass
        para = para.replace('&#x27;',' ')

        between_script_tags3 = re.findall('<time class="W-g-R _14nkQ _3BwtN _2eB4R _3qdyT _18Sdr" data-component="Timestamp" aria-hidden="true" datetime="2021-07-07T21:16:25.000Z">(.*?)</time>',html)
        for time1 in between_script_tags3:
            #print(eachP)
            pass
        #time1 = time1.replace('&#x27;',' ')
        str = "News Source: ABC News \nHost Name: www.abc.net.au \nURL: https://www.abc.net.au/news/politics/"


    elif(i.get() == 'ninenews'):
        request_url = urlopen('https://www.9news.com.au/politics')
        html = request_url.read().decode("utf8")
        between_script_tags = re.findall('<a href="https://www.9news.com.au/national/scott-morrison-royal-commission-defence-veteran-suicide-prime-minister/cb8f54a0-2d43-4224-8ab4-d841e4482132" class="story__headline__link" data-tracking-link-name="na_tag_politics-news_0_na_na"><span class="story__headline__text">(.*?)</span></a>',html)
        for heading in between_script_tags:
            #print(eachP)
            pass
        heading = heading.replace('&#x27;',' ')

        between_script_tags2 = re.findall('<div class="story__abstract">(.*?)</div>',html)
        for para in between_script_tags2:
            #print(eachP)
            pass
        para = para.replace('&quot;',' ')
        para = para.replace('---','')

        between_script_tags3 = re.findall('<time class="story__time">(.*?)</time>',html)
        for time1 in between_script_tags3:
            #print(eachP)
            pass
        str = "Dateline: {} \nNews Source: Nine News \nHost Name: wwww.9news.com.au \nURL: https://www.9news.com.au/politics".format(time1)

    elif(i.get() == 'financialreviewnews'):
        request_url = urlopen('https://www.afr.com/politics')
        html = request_url.read().decode("utf8")
        between_script_tags = re.findall('<a class="_20-Rx" href="/politics/federal/sydney-may-face-longer-lockdown-20210708-p58805">(.*?)</a>',html)
        for heading in between_script_tags:
            #print(eachP)
            pass
        heading = heading.replace('&#x27;',' ')

        between_script_tags2 = re.findall('<p class="_48ktx" data-pb-type="ab">(.*?)</p>',html)
        for para in between_script_tags2:
            #print(eachP)
            pass
        para = para.replace('&#x27;',' ')

        between_script_tags3 = re.findall('<li class="_1PXiX"><time dateTime="Jul 6, 2021 – 6.17pm">(.*?)</time></li>',html)
        for time1 in between_script_tags3:
            #print(eachP)
            pass
            print(time1)
        #time1 = time1.replace('&#x27;',' ')
            str = "Dateline: {}\nNews Source: Financial Review \nHost Name: www.afr.com \nURL: https://www.afr.com/politics".format(time1)

    else:
        request_url = urlopen('https://www.brisbanetimes.com.au/politics')
        html = request_url.read().decode("utf8")
        between_script_tags = re.findall('<a data-testid="article-link" href="/politics/federal/scott-morrison-s-sydney-gets-gold-standard-treatment-20210708-p5883h.html">(.*?)</a>',html)
        for heading in between_script_tags:
            #print(eachP)
            pass
        heading = heading.replace('&#x27;',' ')

        between_script_tags2 = re.findall('<p class="_3XEsE" data-pb-type="ab">(.*?)</p>',html)
        for para in between_script_tags2:
            #print(eachP)
            pass
        para = para.replace('&#x27;',' ')

        between_script_tags3 = re.findall('<time class="W-g-R _14nkQ _3BwtN _2eB4R _3qdyT _18Sdr" data-component="Timestamp" aria-hidden="true" datetime="2021-07-07T21:16:25.000Z">(.*?)</time>',html)
        for time1 in between_script_tags3:
            #print(eachP)
            pass
            print(time1)
        #time1 = time1.replace('&#x27;',' ')
        str = "News Source: Bribane Times News \nHost Name: www.brisbanetimes.com.au \nURL: https://www.brisbanetimes.com.au/politics"


    T0.delete(0,"end")
    T0.insert(0, heading)
    T.delete("1.0","end")
    T.insert("end", para)
    T2.delete("1.0","end")
    T2.insert("end", str)

root = Tk()

# Adjust size
root.geometry("800x380+300+100")
root.minsize(800,380)
root.maxsize(800,380)
root.resizable(0,0)

# Add image file
bg = PhotoImage( file = "news.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 25)

# Add text
label2 = Label( root, text = "Not The Facebook News",font=('Courier','12','bold'),relief=FLAT)

label2.place(x=40,y=0)

label2 = Label( root, text = "Politics News Sources",font=('Courier','12','bold'),relief=FLAT)

label2.place(x=50,y=200)
i = IntVar()
img1 = PhotoImage( file = "abcnews.png")
img2 = PhotoImage( file = "ninenews.png")
img3 = PhotoImage( file = "brisbanetimesnews.png")
img4 = PhotoImage( file = "financialreviewnews.png")
#Basically Links Any Radiobutton With The Variable=i.
i = StringVar()
r1 = Radiobutton(root, image=img1, value="abcnews", variable=i,command=select_radio)
r1.place(x=30,y=240)
r2 = Radiobutton(root, image=img2, value="ninenews", variable=i,command=select_radio)
r2.place(x=190,y=240)
r3 = Radiobutton(root, image=img4, value="financialreviewnews", variable=i,command=select_radio)
r3.place(x=30,y=280)
r4 = Radiobutton(root, image=img3, value="brisbanetimesnews", variable=i,command=select_radio)
r4.place(x=190,y=280)


btnCheckSource = Button(root, bd=2, fg="white", font=('arial',10,'bold'), width=12, height=1, bg="#808080", text="Check Source")
btnCheckSource.place(x=30,y=330)
btnExportSelection = Button(root, bd=2, fg="white", font=('arial',10,'bold'), width=15, height=1, bg="#808080", text="Export Selection")
btnExportSelection.place(x=160,y=330)

label2 = Label( root, text = "Latest News In Politics",font=('Courier','12','bold'),relief=FLAT)

label2.place(x=450,y=10)

T0 = Entry(root, font = ('arial',11), width=54)
T0.place(x=350,y=40)


T = Text(root, height = 12, width = 53)
T.place(x=350,y=70)

T2 = Text(root, height = 5, width = 53)
T2.place(x=350,y=275)





# Execute tkinter
root.mainloop()
