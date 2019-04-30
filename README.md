# Inter-provincial Bus Accidents in Ecuador
Tracking fatal bus accidents in Ecuador http://peteamer.pythonanywhere.com/
## Methods
This program scrapes news stories about fatal inter-provincial bus
accidents in Ecuador from the website of El Comercio, one of Ecuador's 
major newspapers. Stories are then searched, using regular expressions,
for mentions of the accident's death count, time of the accident,
route where the accident occurred, and date of accident. All of that
information is then put into a spreadsheet. Cleaning for duplicates
and some translation of non digit times is then done using Pandas,
 though the program produces both a 'raw' and 'processed' dataset
 for those who wish to view data that has been less abstracted.
 
 ## Setup/Run
 Built in Python 3.6, that version or higher recommended.
Run the following commands in the main directory, "Bus_Retry"
 ```
 $ pip install -r requirements.txt
$ python run_retrieval.py --arg1 True
$ python run_cleaning.py
```
 Note that run_retrieval.py takes an argument, '--arg1'. This is
 used to indicate whether you want to get a fresh scrape of stories
 (True) or if you want to work with the .pickle file that was
 generated with your last run (False). First use should be done with
 True as the arg.
