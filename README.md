# Data Acquisition
This project is mainly based on the [GetOldTweets](https://github.com/Jefferson-Henrique/GetOldTweets-python) project, which is written in Python to get old tweets and bypass some limitations of Twitter Official API. It successfully collected all the data needed by the Social Web course.

## Details
Twitter Official API has the bother limitation of time constraints. Even though the educational account is provided, neither Twitter-Python nor Tweepy seemed unable to get rid of the limitations.  
So this project used a different method to crawl the data directly from Twitter by using the [Twitter advanced search engine](https://twitter.com/search-advanced). There remain some limitations, while after some modifications, this tool can finish the data acquisition process of the Socal Web course.


## Prerequisites
The original version support both python 3+ and Python 2.7+. Since there remain several bugs in the python3 version. This project chooses the python2.7 version instead. And pyquery package is needed.
```
pip install pyquery
```

## Main Functions and Script
- **Exporter.py:** Export tweets to a csv file named **output_got.csv**.  
It was modified from the original version. The program stops for 10 minutes after crawling 10,000 tweets, which is tested to be a stable pace. A counter and much more output were used to trace the condition of the program.

- **gendate.py:** Generate a list of dates to **date.txt**.  
Once the acquisition process is blocked, it can be used to generate the date, which simplified the debug process.
  
- **gencommand.py:** Generate the script **go.sh** for the data acquisition process.  
It uses the date.txt and stores the data for one day according to the date.

- **checker.py:** Check whether we have obtained all of the tweets for every day.  
This function simply reads the data file until the last line. If the program finished correctly, the last line of the data should end at 8 am, since the program runs on the cloud service in Tokyo in Japan.

- **go.sh:** The script generated for running the data acquisition.  
It calls the Exporter.py with components of *-querysearch* *-since* and *-until*. Then it copies the output into the folder with the date as the filename.

- **date.txt:** The list of the date when data needed to be collected.

- **nowcnt.txt:** The counter recorded by **Exporter.py**.

- **Main.py:** Examples of how to use.  
It is used to check whether the connection to Twitter is unblocked.
