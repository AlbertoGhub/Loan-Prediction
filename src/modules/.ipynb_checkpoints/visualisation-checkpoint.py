import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# # COLOR GENERATOR (WHEN I NEED TO TEST THE PALETTE OF COLORS):

# hex_colors = [
#     '#d9f2e6', '#c2e6d2', '#aadbbf', '#93cfab', '#7cc497',
#     '#65b983', '#4eae70', '#37a35c', '#1f9848', '#198c41',
#     '#14803a', '#0f7434'
# ]

# fig, ax = plt.subplots(figsize=(10, 2))
# for i, hex_code in enumerate(hex_colors):
#     ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=hex_code))
#     ax.text(i + 0.5, -0.2, hex_code, ha='center', va='top', fontsize=9, rotation=45)

# ax.set_xlim(0, len(hex_colors))
# ax.set_ylim(-0.5, 1)
# ax.axis('off')
# plt.title("Custom Light Green Palette (Hex Codes)", fontsize=12)
# plt.tight_layout()


# COLOR
sns.set_style('darkgrid')             # darkgrid, white grid, dark, white and ticks 
plt.rc('axes', titlesize=18)          # fontsize of the axes title 
plt.rc('axes', labelsize=14)          # fontsize of the x and y labels
plt.rc('xtick', labelsize=13)         # fontsize of the tick labels 
plt.rc('ytick', labelsize=13)         # fontsize of the tick labels 
plt.rc('legend', fontsize=13)         # legend fontsize 
plt.rc('font', size=13)               # controls default text sizes
colors = sns.color_palette('pastel') 

# BAR PLOT FUNCTION
def bar_plot(colomn, bar_orientation = "v", number_format = "f"):
    
    """THIS FUNCTION WILL GRAPH THE BAR PLOT EITHER IN PERCENTAGE OR REAL VALUE:
    
    We have 1 mandatory parameter, and 2 set up by default. On the other hand, these are the 3 parameters:
            
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
    
    # 1. Horizontal chart with floats
    if((bar_orientation == "h") and (number_format == "f")):
        number_format = "%g" # Format per default
        bar = plt.barh(X, y, color=colors, ec = "black")
        
    # 2. Horizontal chart with percentages
    elif(bar_orientation == "h" and number_format == "p"):        
        y = colomn.value_counts(normalize = True).unique()*100 # y, the 100 is to show it in percentages.
        number_format = '%.2f%%' # Format of 3 decimal and in percentage
        plt.xlim(0, 100) # X limit to 100%
        bar = plt.barh(X, y, color=colors, ec = "black")
        
    # 3. Vertical chart with percentages
    elif(bar_orientation == "v" and number_format == "p"):
        number_format = '%.2f%%' # Format of 3 decimal and in percentage
        y = colomn.value_counts(normalize = True).unique()*100 # y, the 100 is to show it in percentages.
        plt.ylim(0, 100) # y limit to 100%
        bar = plt.bar(X, y, color=colors, ec = "black")
        
    # 4. Vertical chart with floats (default graph)    
    else:
        number_format = "%g" # Format per default
        bar = plt.bar(X, y, color=colors,ec = "black")
    
    plt.bar_label(bar, label_type="edge", padding = 1, fmt=number_format)


    
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
                                                    ec = "black", color = colors[0])
        else:
            bar["bar_" + str(suffix + 1)] = plt.bar(location_y, data_bar["data_bar_" + str(suffix + 1)], w, 
                                                    label = ledger["ledger_" + str(suffix + 1)], 
                                                    ec = "black", color = colors[1])
        
        # bar_1 = plt.bar(location_x, "data_bar_" + str(suffix + 1), w, label = "ledger_" + str(suffix + 1), ec = "black")
        # bar_2 = plt.bar(location_x, "data_bar_" + str(suffix + 1), w, label = "ledger_" + str(suffix + 1), ec = "black")
    
    # TITLE
    plt.title(name + " vs Loan Status")

    # NAME OF THE LABELS    
    plt.ylabel("Approval Rate")

    # NAME OF THE VALUES ON X
    plt.xticks(location_x + w/2, list(data.index)) # (location + width/2, label)
    plt.legend()

    # PUTTING THE NUMBERS ON TOP

    for suffix in range(len(bar)):
        plt.bar_label(bar["bar_" + str(suffix + 1)], label_type="edge", padding = 0.5, fmt=number_format)  
        
    plt.tight_layout()


# ANALYSING INCOME
def avg_income(label, analysed_col):
    """INCOME ANALYSIS"""
    
    # Calculate values
    mean_income = analysed_col.mean()
    min_income = analysed_col.min()
    max_income = analysed_col.max()
    
    # Plot ApplicantIncome
    plt.figure(figsize=(10, 6))
    plt.plot(analysed_col, color=colors[0], label=label + " Income")
    
    # Add horizontal lines for mean, min, and max
    plt.axhline(mean_income, color=colors[1], linestyle='--', linewidth=2, label=f'Mean: {np.around(mean_income, 2)}')
    plt.axhline(min_income, color=colors[2], linestyle=':', linewidth=2, label=f'Min: {min_income}')
    plt.axhline(max_income, color=colors[3], linestyle='-.', linewidth=2, label=f'Max: {max_income}')
    
    # Labels, title, and legend
    plt.title(label + ' Income with Mean, Min and Max', fontsize=16)
    plt.xlabel(label + ' Index', fontsize=13)
    plt.ylabel('Income', fontsize=13)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)

# CORRELATION MATRIX
def correlation_matrix(corr_matrix):
    
    # Set up the figure size
    plt.figure(figsize=(10, 7))

    # Create the heatmap
    ax = sns.heatmap(
        corr_matrix, 
        annot=True,                # Add correlation values to each cell
        fmt=".2f",                 # Format the correlation values
        cmap="BuPu",               # Color palette
        vmax=0.8,                  # Set maximum value for color scale
        square=True,               # Make the heatmap square
        linewidths=0.5,            # Add a little line spacing between cells
        cbar_kws={"shrink": 0.8},  # Shrink the color bar
    )

    # Rotate the x-axis labels for better visibility
    plt.xticks(rotation=45, ha="right")
    
    # Rotate the y-axis labels for better visibility (optional)
    plt.yticks(rotation=0)
    
    # Title for the plot
    plt.title("Correlation Matrix", fontsize=16)
    
    # Show the plot
    plt.tight_layout()