# News-Analysis-of-Stock-Market----Web-Scraping

This repository contains the files and folders of project, I did during my 1-month internship at Jomofi Digital Lab

Stock market analysis is very important because it helps stock analysts to find out activity of an instrument/sector/market in future. By using stock analysis, investors and traders arrive at equity buying and selling decisions. Studying and evaluating past and current data helps investors and traders to gain an edge in the markets to make informed decisions.

Investors rely on stock analysis in helping them find a profitable stock. Stock market analysis helps the investors to identify whether the worth of security is valued in the market.

Analysis of stock market news is very important because Positive news will normally cause individuals to buy stocks. Good earnings reports, an announcement of a new product, a corporate acquisition, and positive economic indicators all translate into buying pressure and an increase in stock prices.

Social media platform like Twitter provide tweets which may be helpful for stock market analyst.

Suppose if he wants to get those particular headlines which contain the names or shortforms of the companies which are listed in NSE (National Stock Exchange).

So by getting the latest headlines, he can analyse and come to a conclusion that which company is in trending currently in news.

I have created web application will show the latest news headlines (containing the names or short form of the companies listed in NSE) in the form of a DataFrame.

## Methodology

 Steps:
 
•	Download Python latest version on desktop/ laptop

•	Clone the repo

•	Open the files in any Python Ide (preferably Pycharm) in separate windows.

Paste the following commands sequentially in terminal of Pycharm in all the four windows

•	virtualenv venv

•	.\venv\Scripts\activate

•	pip freeze > requirement.txt

•	pip install -r requirement.txt

*Make the required changes in code according to the need*

Paste the following command in terminal to open streamlit app in all four windows
•	streamlit run app.py

You will get a URL something like this :

Local URL: http://localhost:8501

Open the URL in any browser to see the Bar chart containing count of tweets.

After checking the bar chart , deploy the Streamlit app to Heroku

Here are the steps to deploy the app to Heroku

•	Login to Heroku through any browser

•	Create a new app on Heroku website

Webpage will be something like this after you have Log In

Create a new app.

![image](https://github.com/premswaroopmusti/Twitter-API-Scrapper----prev-5-mins-tweet-count/assets/106238419/8b530f5f-1410-49f2-82a4-18898fbb77a6)

![image](https://github.com/premswaroopmusti/Twitter-API-Scrapper----prev-5-mins-tweet-count/assets/106238419/0b4ca709-5d1c-4588-b6ba-3ad1eac345ed)

•	After creating you will get a webpage like this showing commands to follow for deploying the app

•	Paste the above commands in the PyCharm terminal sequentially

•	After the deployment is done you will get a Heroku App URL in the terminal

•	Copy the URL

•	That’s it deployment is done

•	You can use the URL whenever you want to get the bar chart showing tweet count.


### Main Libraries for web scraping (BeautifulSoup, Requests)

For news analysis of stock market, we will write a python program to fetch the news headlines containing those keywords. We will require the following libraries for web scraping the websites.

#### BeautifulSoup

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favourite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

#### Requests

The requests module allows you to send HTTP requests using Python.  The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).


### Frontend (Streamlit)

Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc..

### Backend

#### Heroku

Heroku is a cloud platform as a service (PaaS) supporting several programming languages. 
Heroku is a cloud application platform that makes it easy to both develop and deploy web applications in a variety of languages.
Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go. For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages

#### Python

Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing component

## Results and Discussion

Web Application shows latest news headlines which contain the names or shortforms of the companies which are listed in NSE (National Stock Exchange) in the form of a DataFrame.

3.1 Services used

### Heroku

![image](https://github.com/premswaroopmusti/Twitter-API-Scrapper----prev-5-mins-tweet-count/assets/106238419/ac7758df-cc8f-43d4-a877-150e3844ebdb)

Fig1: Heroku Dashboard

Heroku is a cloud platform that lets companies build, deliver, and monitor simple applications quickly and without endless infrastructure headaches. Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
I have used Heroku to build, run and operate applications. In Fig1, you can see the Heroku Dashboard which is showing web applications that i have built and deployed.

### Streamlit

![image](https://github.com/premswaroopmusti/Twitter-API-Scrapper----prev-5-mins-tweet-count/assets/106238419/1d60a85a-a45b-470b-bdef-1286e0015636)

Fig2: Home page of Streamlit’s Webpage

Streamlit is a open-source python based framework to rapidly build and share beautiful machine learning and data science web apps. We can instantly develop web apps and deploy them easily using Streamlit. I have used it for the same purpose. Fig2 shows the home page of Streamlit website.

### Python

![image](https://github.com/premswaroopmusti/Twitter-API-Scrapper----prev-5-mins-tweet-count/assets/106238419/6f97ebc0-842c-4302-b655-2e6726c31386)

Fig3: Python Webpage

Python can be used for data analysis ,data pre-processing ,data visualization and for working on DataFrames. Its high-level built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing component. I have used it for the same purpose. I’ve used the latest version of Python as seen in Fig.3

## Product Final Screenshots:

![image](https://github.com/premswaroopmusti/News-Analysis-of-Stock-Market----Web-Scraping/assets/106238419/3d6eb951-914d-4e60-9465-2ca69b4fe750)

Fig5: Web Application shows the DataFrame

Fig5 shows the Web Application displaying the DataFrame which contains the latest news headlines along with company name or hashtags present in the respective news headline.


## Conclusion
   
This paper proposes a flexible, efficient and free to use Web Applications. Web application shows the latest news headlines containing the names or shortforms of the companies which are listed in NSE (National Stock Exchange) in the form of a DataFrame. A user just needs to hit the URL of the Web Application in any web browser (like Google Chrome or Internet Explorer etc) and after hitting the URL, app will take some time and then shows DataFrame.

## References
   
-	https://www.toptal.com/python/twitter-data-mining-using-python
-	https://www.moneycontrol.com/news/
-	https://www.investing.com/news/
-	https://www.nseindia.com/products-services/equity-derivatives-nifty50 


