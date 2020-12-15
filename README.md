## mailrobot
This is a program to predict data analysis via machine learning. It is possible to use different python libraries.

## FIRST

* Configure system environment on Windows OS
* Download Pyhton from visualstudio code extensions

## SECOND

How to create my training set? How to determine requests and responses for my parameters?

* Get csv file of opening tickets as a training set.
* Learn the definations from training set.
* Define the cluster fields.

* Is the new ticket?
* Get the fields from text 
* Determine the cluster from tranining set.
* Check not null the fields.
* Response not exist fields.
* Get all the information.
* Open the ticket.


## THIRD

```
-- pytextai folder right click open in terminal

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -m venv env
. env/Scripts/activate.bat

python app.py

```

/usr/local/lib/python3.8/dist-packages/tqdm/std.py:699: FutureWarning: The Panel class is removed from pandas. Accessing it from the top-level namespace will also be removed in the next version
  from pandas import Panel
<ipython-input-1-3a929f084650>:205: DeprecationWarning: Call to deprecated `LabeledSentence` (Class will be removed in 4.0.0, use TaggedDocument instead).
  output.append(LabeledSentence(s, ["tweet_" + str(i)]))