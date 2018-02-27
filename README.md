# Robinson spider

A small scrapy spider written to collect information for Expeditie Robinson 2018


## Installation on Windows 10
 
 1. Download the zip file(click the green Clone or Download top-right)
 2. Unzip the file
 3. Install Python 3: https://www.python.org/downloads/
    - Make sure that you select to install `pip` during the installation
 4. Download and install buildtools: https://aka.ms/BuildTools 
    - click on Build Tools for Visual Studio 2017 for download
 5. When installing Select Visual Studio Build Tools and Click Install

*For devs: I know that docker or virt-env is better, this is for non-techies....*

 6. Browse to the folder where you unzipped the downloaded file(first step)
That folder should contain a file called README.md and scrapy.cfg

 7. Open a command window here: `shift+rightclick` and click: `Open Powershell window here`

 8. Execute the following command: `pip install pypiwin32 scrapy`

 9. When that finishes installing run this command to actually scrape the data:`scrapy crawl robinson`


## Using it

The final step of the installation process creates a file called `export.tsv` that contains all the scraped data. A column with the name,url and columns for each game that is going on containing the current votes for that.

If you closed the command window or want to run it again on another day:

 1. Backup the previous export.tsv, it will be overwritten!(needs a fix)
 2. Browse to the folder where you unzipped the files(Installation step 6)
 3. Run the command again: `scrapy crawl robinson`
 
To use the data, it is easiest to open the `export.tsv` file with a text editor like notepad(++) and copy the whole contents. 
Paste the data in Excel or another spreadsheet program and do with it what you want

Tip: When using Excel, create a table so you can sort