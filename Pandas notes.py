#Create a new repository called pandas-challenge- complete
#clone repository to local computer- complete
#Push code at least once an hour and double check to ensure code uploaded to github

#SHORTCUT command slash next to shift button to comment
#Shortcut command z uncomment
#add Jupyter notebook to this folder. This will be the main script to run for analysis.
#not complete yet
#You must submit a link to your Github/Git Lab repo that contains your Jupyter Notebook.
#You must include a written description of at least two observable trends based on the data.
#Push the above changes to github

#Start with: 
#"How do I import the data?" 
## Modules
# import os
# import csv

# how to open a file 1:13:30 into Day 1 Pandas
#Set path for file
#csvpath = os.path.join("Resources", "netflix_ratings.csv")
### Netflix Remix class activites 02 Day 1
# You will see this pattern in your homework where you have a starter file and have outputs that the grader is somewht expecting
    #The grader is expecting an output as such. So you have an idea of what to put in there

#this is for loop is going through each row in the CSV and its trying to match each row
#to the value that is assigned to the video variable. The user input is the video variable.
#It's going to check whether or not the first element of that row, one element, it is comma seperated (comma delimited)
#the first element, does it match tht e input from user, if it is then print out some stuff, it is not then keep going 
# and if it isn't found then print out the statement ("sorry about this ")
    
    #for row in csvreader:
        #if row[0]== video:
            #print(row[0] + "is rated" + row[1] + "with a rating of" + row[6])
            #set variable to confirm we have found the video
            #found = True
            #if found is false:
                #print("Sorry about this, we don't seem to have what you are looking for!")

###without the with block Class discussion 1:15 to 1:24
#csvreader = csv.reader(csvfile, delimiter=",")
    #module.method
    #take the reader method from the csv module
    #.reader instructions are stored in the csv module
    #it will take an input of characters and do something and create a csv reader object
    #csv reader object is a list of a list
    #now iterate throught the list of the list
    #it is only checking the first item of each line
    #iterate through every single row, one row at a time. 
    #this is called a 2D array
    #the first list below will be assigned to a 
    #one element of the outside element is 
    
    #for row in csv reader (list of a list), one element of the outside list is an iunside list with 3 elements
        #for row in csv reader one at a time it is going to be assigned in to a variable name row
        ### if the element in index 0 bc we access ind elements of a list with integer indices
            ##we are saying Row if the element at index 0 equals equals to vidoe (variable above) then print out the element at the zero index 
            #and the elemetn at the first index and the element at the 6 index
            #and then change the variable found the bollian value true
        #the flase line never executes if the video is not found
        #if it is false (it was never changed to true) print out the false expression
        #false will not execute if true but the boolean expression will still be checked it just won't print in this case if it is true
#wrap everything around the with statement because with the with statement at the end of the with block the "Resources"
#the variables will not be released

###module called Pandas This is used to visualize, analyze, and alter large datasets
    #This is a multi demissional list. A table with 2 rows is 2 dimensiional
    #example row1 =[0,1,2,3,4,5,6,7] there are 8 elements to this list set to a variable named row1
    #example continued row2= [2,3,4,5,6,7,8,9] There are 8 elements to this list
    #Instead of working with 2 deminssional list we will work with columns and rows
    #in Pandas we will work with a table of columns and rows. We are accustomed to row1 in excel and column a for example
    #but in pandas rows will be identified by its index (has to be unique- normally in excel we accept rows to be 1,2,3, etc)
    #We get to define what the columns are and the row can be changed to whatever we want but they are assigned a sequential integer number
    #Pandas allows us to work with 2 dimensional list in a more intitituve method

#while pandas alone is stuck using list, tuples, and dictionaries, Pandas lets Python programmers work with "Series" and "DataFrames"
#Each column in a DataFram is a Series
#Series is one column table (yet there are two columns, the first one is the index, in excel it is your row number, it doesn't have to be 1,2, 3, 4 
#but each one has to be unique) whereas a datafram is a table with multiple columns 

#A single column table (table with 1 column) is a series. A table with multiple columns is a datafram
#each row whether it is a DF or series must have an index that is unique to that table

# "How do I convert the data into a DataFrame?" 
    # Convert a single dictionary containing lists into a dataframe
    #this is one big dictionary
    #it has 2 keys Dynasty and Pharaoh
    #the values associated with each key is a list. 
    #how many items are in the list? 2
    #so passing a larger dict to the pd.datafram constructor we are going to assign the resulting data frame 
    #to a variable name pharoh_df
    #remember the array must be the same length, so adding "test" to the end of the first list (key dynasty) 
    # You will get an error because the array is not the same length. 

    #pharaoh_df = pd.DataFrame(
        #{"Dynasty": ["Early Dynastic Period", "Old Kingdom"],
        #"Pharaoh": ["Thinis", "Memphis"]
        #}
        #)
    #pharaoh_df

    #EXAMPLE 2
    # Create a DataFrame of frames using a dictionary of lists
    #Provide the name for column and then all the values associated with that column
    #Provide the price for a column and then all the values associated with that column
    #Provide the sales for a column and then all the values associated with that column
    #we have to ensure the deminsion (the length) of the list has to be the same
    #if we don't have a data point for the particular row then we have to manually type in 'N/A'
    #otherwise it wouldn't run bc the shape isn't the same
        #frame_df = pd.DataFrame({
            #"Frame": ["Ornate", "Classical", "Modern", "Wood", "Cardboard"],
            #"Price": [15.00, 12.50, 10.00, 5.00, 1.00],
            #"Sales": [100, 200, 150, 300, 'N/A']
        #})
        #frame_df
#the assignment to a variable name. It should be obvious. 
#If we don't assign the resulting object the instance of a data frame class to a varialbe name
###YOU WILL NOT BE ABLE TO ASSIGN THE VARIABLE FOR CALCULATIONS LATER. REMEMBER TO ASSIGN YOUR OBJECTS

#"How do I build the first table?"
    #we can create a Pandas Series from a raw list
    #recall a dict is a set of keys and values
    # Convert a list of dictionaries into a dataframe
    #crate a data frame here
    #remember dict 
    #how many dicts is states_dict? It is a list of how many dictionarys? 2
    #how many keys in each dict? 2 keys in 2 dictionarys
    #the index 0 is the first dict below
    #the index of 1 is the second dict below

    #states_dicts = [{"STATE": "New Jersey", "ABBREVIATION": "NJ"}, #this list has 2 elements. #{key : value , key: value,}
        #{"STATE": "New York", "ABBREVIATION": "NY"}] #(key: value, key: value)

    #states_df = pd.DataFrame(states_dicts)  #pass a list of dictonaries to the pd.dataframe and it will generate a table. 
    #states_df
       ###you are getting a NameError: name 'pd' is not defined
        #import pandas as pd is at the top

#Don't get intimidated by the number of asks. Many of them are repetitive in nature with just a few tweaks.

###Display a statistical overview of the DataFrame
    #We have a pandas.read_csv()   This is a function from the module. The result is a table
    #df.describe()   This is a method we are doing on the object. The result is we are working with the data fram itself
    #this is taking the first 5 rows of the data frame, the variable name is data_file (see In 13 above)
    #the describe method will look at the numerical columns and calculate the uni variate statistics (looking at one variable by itself)
    #so lookin at every number in the id column by itself, here are some statistics for it, see out 12: 
    #Use mostly for the count and the mean but also includes min and max. Can't due statstics on string values
  
    #data_file_df.describe()
        #you can assign this to a varaiable
        #you can then pull up stats_df as a hanging object
        #stats_df=data_file_df.describe
        #this returns an entirely new data frame. That was called data_file.df
        #this data frame has 8 rows and 2 columns, it is assigned to the variable name stats_df


#Create an overview table that summarizes key metrics about each school, including:

#School Name

#School Type

# Total Students
    #2:45 into class
    #Pandas 1 /05-Ins_DataFunctions/Solved/data_functions.ipynb
    ### The SUM method adds every entry in the series
    #inside of the bracket it is expecting string value that matches the column name
    #The toal method 
    
    #data_file_df
    
    #total = data_file_df["Amount"].sum()
    #total
# Total School Budget
    #2:45 into class
    #Pandas 1 /05-Ins_DataFunctions/Solved/data_functions.ipynb
    ### The SUM method adds every entry in the series
    #inside of the bracket it is expecting string value that matches the column name
    #The toal method 
    
    #data_file_df
    
    #total = data_file_df["Amount"].sum()
    #total

# Per Student Budget

# Average Math Score
    #average_math_score = average
    # average =data_file_df["Amount"].mean()
         #Activites 05-Ins_DataFunctions/Solved
        #2:46 into Pandas Day 1
        ## The mean method averages the series
        #There are methods in pandas to simplify the math
        #here we are saying just pull the amount column and calculate the mean
        #use the .mean method (this returns a scaler value- a single value in mathamatical terms is one scaler value)

        #average = data_file_df["Amount"].mean()
        #average
# Average Reading Score

# % Passing Math (The percentage of students that passed math.)
    #2:50 into Pandas 1 
    # Calculations can also be performed on Series and added into DataFrames as new columns
    # add a new column to the original data frame(see above 1000 rows x 5 columns)
    # on the right hand side of the equation is what we want to assign. 
    # So this is saying take the amount column divided by 1000 (what data type is 1000 of dollars?)
    #a scaler value A scalar is a simple single numeric value (as in 1, 2/3, 3.14, etc.), usually integer, fixed point, or float (single or double), 
    #as opposed to an array, structure, object, complex vector (real plus imaginary or magnitude plus angle components), higher dimensional vector or matrix (etc.)
    #What data type is data_file_df ["Amount"]
    #it is a series 
    #the result is a series
    #we are assinging data_file_df a column called "Thousands of Dollars"
    #we are assigning thousands_of_dollars to that column to the data_file_df data frame

    #thousands_of_dollars = data_file_df["Amount"]/1000
    #data_file_df["Thousands of Dollars"] = thousands_of_dollars

    #data_file_df.head()

# % Passing Reading (The percentage of students that passed reading.)


# % Overall Passing (The percentage of students that passed math **and** reading.)
