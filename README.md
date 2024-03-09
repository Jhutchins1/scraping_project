# UNIDO Statistics Scraping Project 

## My original proposal: ##

I chose this UNIDO, the United Nations Industrial Development Organization, website to scrape because it had plenty of publicly available data to choose from. In my proposal I decided that I was going to scrape three data points from different countires in their database. The three points of data I originally planned to scrape for each country were their population, their MVA (Manufacturing Value Added) per capita, and their ranking on the CIP (Competitive Industrial Performance) Index. Along with successfully scraping these data points, my program also provides the country's page URL, and the name of the country for each group of data. 

## Beginning the Process 

First I had to get all of the country URLs I needed (20 to be exact) out of the drop down menu on the website, and place these URLs in a list. The homepage for this website is stat.unido.org which actually begins on the page for the United States of America. In my get_urls() function I stored my URLs and returned them for their data to be scraped. 

Once I got these, I created a rudimentary file where I began testing different scraping strategies. I faced challenges in this area because for each country, all of their statistics are coded in the same type of container with the same classes. I found that by indentifying the data by its index I could extract the specific data points that I needed from these <div> containers. 


## Functions
Once I figured out how to scrape one page, the rest of the project came together. I turned this code to scrape one page, into a function called **scrape_data()** with the arguments url and driver since I am using selenium to go through my list and scrape all twenty countries. This function neatly returns the data for the country page it scrapes for the URL it is given. It also allows the function to sleep 5 seconds to ensure the page loads and that it has time to scrape the data. 

After writing the function for scraping the data for a single URL, and writing the function that returns all twenty of my URLs, I wrote one last function called **run_scraping()** with the argument "urls", which = my URL function, **get_urls()** as declared at the bottom of my script. 

This function, **run_scraping()** applies my scraping code to each of the twenty URLs in the list. While I originally had this function print everything I scraped to the terminal, I instead created a blank list of my twenty scrapes and wrote my data to a CSV file titled scraped_data.csv. 

So overall, I have a function that scrapes the data from each URL, I have a function that stores my URLs in a list and returns them one by one to be scraped, and I have a function that scrapes each URL and places the data in a list, and writes the data to a CSV file. My **run_scraping** function is the most crucial function as it incorporates both of my other functions. The run_scraping function is called at the bottom of my script after it is defined above. 


## Challenges 
My biggest challenge for this project was in trying to let Selenium interact with the drop down menu itself. Ideally my code would let the driver click on the drop down menu, select the country, scrape the data, and then repeat the process for twenty countries. However, by manually providing my code with the URL of twenty countries, it lets the programmer choose which countries they want to scrape rather than twenty of them at random. I faced a lot of difficulty trying to write code that would allow my driver to interact directly with the dropdown menu. There are multiple drop down menus on the page, and it seemed near impossible to extract the specific elements I need that code the dropdown menu for the Selenium driver to interact with. 

I also encountered some formatting problems, where my code just scraped the data and provided them in on their lines, but the reader would have no idea what the data meant or which country it was associated with so I made sure the information was presented clearly and neatly. 
