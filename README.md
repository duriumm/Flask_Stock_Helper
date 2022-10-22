# Flask Stock Helper

## Description
This appllication takes a CSV file of stocks and their market value during the day, then outputs the top three winners of the CSV file as JSON
The CSV file is updateable during runtime


### How to run
Run main.py and go to localhost(http://127.0.0.1:5000/) + /stocklist 
to trigger the get function which will return the winners from the CSV list


## Dependencies
- Flask
- Pandas

## Ideas on how to improve for furute developers
For the future development i would recommend:
- Specify a schema for how the CSV needs to look
- PUT function to add additional data to the CSV file 
- User Interface where we can specify CSV file path and show the top winners 

<br>
