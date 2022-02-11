# Election Campaign Dynamics

Political campaigns are important moments for political personalities, political parties, and their campaigners as well. During this period, arguments, ideas and topics flow between the candidates, and one can wonder how the discourse of a campaign is constructed. This way, one can understand the main campaign focus points, its key topics, their life-cycle and how they evolve during campaigns. Political speeches, during campaign season are known for being formulaic and repetitive. What could we learn by looking for patterns in the way the speeches change over the course of the campaign? For this project, we are preparing to look at the campaign evolution of the 2022 France Presidential election candidates.

# Running the website on local machine

To run the website on your local machine, you can follow this steps:
```
cd Website/FlaskWebsite
```

Then install all required packages, preferably inside a python environment, such as pipenv or conda, run this command to create or activate a python environment:
```
pipenv shell
```

And run this command to download all required packages
```
pip install -r requirement.txt
```

There would be some problem on installing a number of packages such as hdbscan or bertopic on your machine. It’s because they are dependent to c++ compiler on OSs. Usually linux and mac take advantage of gcc by default but on Windows a c++ compiler is needed to be installed.

Then you can run below command to run the website: `flask run`
