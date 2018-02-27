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


