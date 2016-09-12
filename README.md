# ONSdatabaker scripts - MQ5

Please note. We use github for versioning purposes only. If anyone wants the actual data involved it will always be easily accessible via the ONS website (www.ons.gov.uk) and API service.

The MQ5 source data consists of three spreadhseets. Each has one tab of data and one of CDID code lookups.


## Usage

1.) "Download as zip" from the above options and extract

2.) Drop the MQ5 spreadsheets into the folder.

3.) Double click on the "Click To Run" batch file. It will prompt you for the number of quarters to be extracted (See below). Enter the value then press enter and the rest is automatic.


## Number of Quarters

You need to add the number of quarters to be extrated from the spreadsheets. These quarers MUST START in column C of the 1st tab(s). We cant do this automatically as MQ5 source spreadsheets sometimes supply empty columns for previous years.

### IMPORTANT - if you are supplied with empty columns you MUST delete them. For the script to run the columns of data must start in column C and must have data in them.
