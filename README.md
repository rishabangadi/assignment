## Install required libraries

```
pip3 install requests argparse
```

There are two files: **assignment.py** and **assignment-1.py**

- **assignment-1.py** : This has the function that takes only two arguments: address and page size.
- **assignment.py** : In addition to address and page size, the function takes check-in date, check-out date, number of adults, currency as arguments

## Run the below command

```
python3 assignment-1.py "73 W Monroe St, Chicago, IL 60603, USA" 20 
```
or

```
python3 assignment.py "73 W Monroe St, Chicago, IL 60603, USA" 50 "2024-03-01" "2024-03-05" --adults 2 --currency "USD"
```

#### Mandatory Arguments

- First argument : Address
- Second argument : Page size
- Third argument : Checkin date
- Fourth argument : checkout date

#### Optional Arguments

- adults
- currency
