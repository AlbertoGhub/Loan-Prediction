# BAR PLOT FUNCTION

def bar_plot(colomn, bar_orientation = "v", number_format = "f"):
    
    """THIS FUNCTION WILL GRAPH THE BAR PLOT EITHER IN PERCENTAGE OR REAL VALUE:
    
    We have 1 mandatory parameter, and 2 set up by default. On the other hand, these are the we have 3 parameters:
            
        a) Column to graph (MANDATORY)
        b) Bar orientation (1. Horizontal (h) or 2. Vertical (v), set by default)
        c) Number display (1. Percentage (p) or 2. Float (f, set by default))
    
    CONDITIONS:
        1. Vertical graph with f
        2. Vertical graph with p
        3. Horizontal graph with f
        4. Horizontal graph with p
    """
    
    bar = None # Container (graph)
    X = [] # Final X labels
    y = colomn.value_counts().unique() # y values    
    
    # THIS SECTION WOULD PARSE ALL THE LABELS INTO A STRING:        
    original_X = list(colomn.value_counts(normalize = True).index) # Say, labels
     
    # TURNING THE LABELS INTO A STRING    
    for item in original_X:
        X.append(str(item))
        # End of for    
    
    title = colomn.value_counts().name # Getting the title
    
    # 1. Horizontal chart with floats
    if((bar_orientation == "h") and (number_format == "f")):
        number_format = "%g" # Format per default
        bar = plt.barh(X, y, color=colors, ec = "black")
        
    # 2. Horizontal chart with percentages
    elif(bar_orientation == "h" and number_format == "p"):        
        y = colomn.value_counts(normalize = True).unique()*100 # y, the 100 is to show it in percentages.
        number_format = '%.3f%%' # Format of 3 decimal and in percentage
        plt.xlim(0, 100) # X limit to 100%
        bar = plt.barh(X, y, color=colors, ec = "black")
        
    # 3. Vertical chart with percentages
    elif(bar_orientation == "v" and number_format == "p"):
        number_format = '%.3f%%' # Format of 3 decimal and in percentage
        y = colomn.value_counts(normalize = True).unique()*100 # y, the 100 is to show it in percentages.
        plt.ylim(0, 100) # y limit to 100%
        bar = plt.bar(X, y, color=colors, ec = "black")
        
    # 4. Vertical chart with floats (default graph)    
    else:
        number_format = "%g" # Format per default
        bar = plt.bar(X, y, color=colors,ec = "black")
    
    plt.bar_label(bar, label_type="edge", padding = 1, fmt=number_format)
    plt.title(title)
    plt.tight_layout()

    
# GROUP BAR

def groupped_bar(data, name = "COLUMN NAME", percentage = "f"):
    
    """GRAPHING THE GROUPED BARS
    
    1. Getting the names we are going to put in.
    2. Getting the values for the bars. (Columns)
    3. Getting the x_ticks"""

    # FORMAT NUMBER
    number_format = "%g"

    # LABELS
    x_label = list(data.columns) # Ledgers (columns)
    x_ticks_values = list(data.index.values) # For the x values on the graphs
    
        
    # WIDTH
    w = 0.4

    # DATA: Format - N - Y
    # CREATING DICT SO WE CAN HAVE THE REQUIRED NUMBER OF VARIABLES  
    
    ledger = {} # Ledger
    data_bar = {} # Data to plot
    bar = {} # Creating the barchart
    
    for suffix in range(len(x_label)): # Extracting data       
        index = x_label[suffix] # Picking the column (Ledgers)
        
        # Data for the chart
        data_bar["data_bar_" + str(suffix + 1)] = list(data[index]) # Taking the data to plot
        ledger["ledger_" + str(suffix + 1)] = index
        # End of 4

    # PERCENTAGES IF NEEDED.
    if(percentage == "p"): 
        plt.ylim(0, 110)
        number_format = '%.2f%%' # Format of 3 decimal and in percentage
        results_bar_1 = [] # To get the results
        results_bar_2 = []
        last_value = [] # To get the previous value
        current_value = [] # to get the current value
        count = 0
        
        for key in data_bar.values():
        # CAPTURING THE KEY VALUES, SO I CAN GET THE LIST OF VALUES FROM THE DICT
        # WE NEED TO CAPTURE THE VALUES INDIVIDUALLY

            # print(key)
            if(count == 0):
                results = key
                count +=1
            else:
                # ADDING THE FINAL VALUES TO A DICT FOR LATER ON
                last_value = results
                results = []
                for operation in range(0, len(key)):

                    # CALCULATING THE PERCENTAGE FOR N AND Y
                    
                    # N
                    results_bar_1.append((last_value[operation])/(last_value[operation] + key[operation])*100) # Percentage for N

                    # Y
                    results_bar_2.append((key[operation])/(last_value[operation] + key[operation])*100) # Percentage for Y

            # End of 4

        # REPLACING THE VALUES ON THE ORIGINAL DICT
        data_bar["data_bar_1"] = results_bar_1
        data_bar["data_bar_2"] = results_bar_2

        # End of if
        
    # LOCATIONS
    location_x = np.arange(len(x_ticks_values)) # location of x ticks of the first bar
    location_y = [i + w for i in location_x] # location of x ticks of the second bar
    
    # DRAWING THE BARS: Saving it into a variable to put the values on top   

    for suffix in range(len(data_bar)):
        if(suffix == 0):
            bar["bar_" + str(suffix + 1)] = plt.bar(location_x, data_bar["data_bar_" + str(suffix + 1)], w, 
                                                    label = ledger["ledger_" + str(suffix + 1)], 
                                                    ec = "black", color = "#FFA07A")
        else:
            bar["bar_" + str(suffix + 1)] = plt.bar(location_y, data_bar["data_bar_" + str(suffix + 1)], w, 
                                                    label = ledger["ledger_" + str(suffix + 1)], 
                                                    ec = "black", color = "#90EE90")
        
        # bar_1 = plt.bar(location_x, "data_bar_" + str(suffix + 1), w, label = "ledger_" + str(suffix + 1), ec = "black")
        # bar_2 = plt.bar(location_x, "data_bar_" + str(suffix + 1), w, label = "ledger_" + str(suffix + 1), ec = "black")
    
    # TITLE
    plt.title(name + " vs LOAN STATUS")

    # NAME OF THE LABELS    
    plt.ylabel("APPROVAL RATE")

    # NAME OF THE VALUES ON X
    plt.xticks(location_x + w/2, list(data.index)) # (location + width/2, label)
    plt.legend()

    # PUTTING THE NUMBERS ON TOP

    for suffix in range(len(bar)):
        plt.bar_label(bar["bar_" + str(suffix + 1)], label_type="edge", padding = 0.5, fmt=number_format)  
        
    plt.tight_layout()

# SHOWING NaNs

def na_calculator(data):
    '''SHOWING THE STATS OF MISSING DATA AND DATA TYPE'''

    percentage_missing = (data.isna().mean()*100).sort_values(ascending = False)                      # Storing the Percentages of NaNs
    sum_missing = data.isna().sum().sort_values(ascending = False)                                    # Storing the Sum of NaNs
    names = sum_missing.index.to_list()                                                               # Storing names (to show in the columns)
    data_type = data[names].dtypes                                                                    # Storing the type of data based on the order from the previous obtained data (slicing)
    sum_values = sum_missing.to_list()                                                                # Getting count of missing values
    perc_values = np.around(percentage_missing.to_list(), 3)                                          # Getting percentage of missing values
    types = data_type.to_list()                                                                       # Getting the types of the data
    # TURN ALL THE DATA INTO A DATAFRAME
    df_missing = pd.DataFrame({"NAMES" : names,
                                    "VALUE COUNT" : sum_values,
                                    "PERCENTAGE (%)" : perc_values,
                                    "DATA TYPE": types})
    return df_missing