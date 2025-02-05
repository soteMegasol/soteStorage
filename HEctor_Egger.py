
import json
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
            
json_path = r"\\SRVDABU02\Benutzerordner$\sofia.teixeira\Desktop\Projects\Solar_Studies\Hector_Egger.json" 
file = open(json_path)  
data = json.load(file)  

# area color dictionary/definition for an easier global color changing
area_colors = {
    'Area 1': 'lightcoral',
    'Area 2': 'khaki',
    'Area 3': 'plum',
    'Area 4': 'cornflowerblue',
    'Area 5': 'limegreen'
}

Months = {
    "jan":31,
    "feb":28,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug":31,
    "sep":30,
    "oct":31,
    "nov":30,
    "dec":31
}

# value labels function
def addlabels(x,y, padding=10):
    for i in range(len(x)):
        plt.text(i, y[i]+padding,f'{y[i]:.1f}', ha='center')


def Monthly_Energy_per_Area():

    # Area 1 

    sum_hours_jan = sum(data["24-00220-01-01"]["jan"])
    y_jan = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-01"]["feb"])
    y_feb = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-01"]["mar"])
    y_mar = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-01"]["apr"])
    y_apr = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-01"]["may"])
    y_may = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-01"]["jun"])
    y_jun = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-01"]["jul"])
    y_jul = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-01"]["aug"])
    y_aug = sum_hours_aug/1000
    
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    y_sep = sum_hours_sep/1000
    
    sum_hours_oct = sum(data["24-00220-01-01"]["oct"])
    y_oct = sum_hours_oct/1000
    
    sum_hours_nov = sum(data["24-00220-01-01"]["nov"])
    y_nov = sum_hours_nov/1000
    
    sum_hours_dec = sum(data["24-00220-01-01"]["dec"])
    y_dec = sum_hours_dec/1000
    

    ## Graph data - Area 1
    
    # def Graph_Monthly_Estimated_Energy_Output_per_Area():   Fazer o gräfico cm funcao? Assim pode usar-se apenas a funcäo 
                                                             # monthly, p fazer tb o gräfico da funcao compound. Seria sö chamar um gräfico diferente

    x=["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y=[y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec]   
    
    plt.figure(1)
    plt.bar(x, y, color =area_colors ['Area 1'] , width=0.4)   # P/ fazer gräficos de barras
    plt.xlabel("Month",labelpad=10 )
    plt.ylabel("Estimated Energy output",labelpad=10 )
    plt.title("Monthly Estimated Energy Output per Area - Area 1 [MWh]", pad=20)
    plt.yticks([4,8,12,16,20,24,28,32,36,40,44])
    plt.ylim(0, 44) 
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Monthly_E_per_Area_1.png', format='png')
    addlabels(x,y, padding=0.5)
    plt.show()


# Area 2 

    sum_hours_jan = sum(data["24-00220-01-02"]["jan"])
    y_jan = sum_hours_jan/1000
 
    sum_hours_feb = sum(data["24-00220-01-02"]["feb"])
    y_feb = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-02"]["mar"])
    y_mar = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-02"]["apr"])
    y_apr = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-02"]["may"])
    y_may = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-02"]["jun"])
    y_jun = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-02"]["jul"])
    y_jul = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-02"]["aug"])
    y_aug = sum_hours_aug/1000
    
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    y_sep = sum_hours_sep/1000
    
    sum_hours_oct = sum(data["24-00220-01-02"]["oct"])
    y_oct = sum_hours_oct/1000
    
    sum_hours_nov = sum(data["24-00220-01-02"]["nov"])
    y_nov = sum_hours_nov/1000
    
    sum_hours_dec = sum(data["24-00220-01-02"]["dec"])
    y_dec = sum_hours_dec/1000
    


    ## Graph data - Area 2

    x=["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y=[y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec]   
    plt.figure(2)  # figure should always be called before ticks
    plt.bar(x, y, color =area_colors ['Area 2'], width=0.4) 
    plt.xlabel("Month", labelpad=10)
    plt.ylabel("Estimated Energy output", labelpad=10)
    plt.title("Monthly Estimated Energy Output per Area - Area 2 [MWh]", pad=20) 
    plt.yticks([4,8,12,16,20,24,28])
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Monthly_E_per_Area_2.png', format='png')
    addlabels(x,y, padding=0.5)
    plt.show()


    
# Area 3 

    sum_hours_jan = sum(data["24-00220-01-03"]["jan"])
    y_jan = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-03"]["feb"])
    y_feb = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-03"]["mar"])
    y_mar = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-03"]["apr"])
    y_apr = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-03"]["may"])
    y_may = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-03"]["jun"])
    y_jun = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-03"]["jul"])
    y_jul = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-03"]["aug"])
    y_aug = sum_hours_aug/1000

    sum_hours_sep = sum(data["24-00220-01-03"]["sep"])
    y_sep = sum_hours_sep/1000

    sum_hours_oct = sum(data["24-00220-01-03"]["oct"])
    y_oct = sum_hours_oct/1000

    sum_hours_nov = sum(data["24-00220-01-03"]["nov"])
    y_nov = sum_hours_nov/1000

    sum_hours_dec = sum(data["24-00220-01-03"]["dec"])
    y_dec = sum_hours_dec/1000



    ## Graph data - Area 3

    x=["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y=[y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec]   
  
    plt.figure(3)
    plt.bar(x, y, color =area_colors ['Area 3'], width=0.4) 
    plt.xlabel("Month",labelpad=10,)
    plt.ylabel("Estimated Energy output",labelpad=10)
    plt.title("Monthly Estimated Energy Output per Area - Area 3 [MWh]", pad=20)  
    plt.yticks([4,8,12,16,20,24,28])
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Monthly_E_per_Area_3.png', format='png')
    addlabels(x,y, padding=0.5)
    plt.show()


# Area 4 

    sum_hours_jan = sum(data["24-00220-01-04"]["jan"])
    y_jan = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-04"]["feb"])
    y_feb = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-04"]["mar"])
    y_mar = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-04"]["apr"])
    y_apr = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-04"]["may"])
    y_may = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-04"]["jun"])
    y_jun = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-04"]["jul"])
    y_jul = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-04"]["aug"])
    y_aug = sum_hours_aug/1000

    sum_hours_sep = sum(data["24-00220-01-04"]["sep"])
    y_sep = sum_hours_sep/1000

    sum_hours_oct = sum(data["24-00220-01-04"]["oct"])
    y_oct = sum_hours_oct/1000

    sum_hours_nov = sum(data["24-00220-01-04"]["nov"])
    y_nov = sum_hours_nov/1000

    sum_hours_dec = sum(data["24-00220-01-04"]["dec"])
    y_dec = sum_hours_dec/1000



    ## Graph data - Area 4

    x=["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y=[y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec]   
   
    plt.figure(4)
    plt.bar(x, y, color =area_colors ['Area 4'], width=0.4) 
    plt.xlabel("Month",labelpad=10)
    plt.ylabel("Estimated Energy output",labelpad=10)
    plt.title("Monthly Estimated Energy Output per Area - Area 4 [MWh]", pad=20) 
    plt.yticks([2,4,6,8,10,12,14,16,18])
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Monthly_E_per_Area_4.png', format='png')
    addlabels(x,y, padding=0.5)
    plt.show()


    
# Area 5 

#   sum_hours_jan = sum(data["24-00220-01-05"]["jan"])
    y_jan = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-05"]["feb"])
    y_feb = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-05"]["mar"])
    y_mar = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-05"]["apr"])
    y_apr = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-05"]["may"])
    y_may = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-05"]["jun"])
    y_jun = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-05"]["jul"])
    y_jul = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-05"]["aug"])
    y_aug = sum_hours_aug/1000
    
    sum_hours_sep = sum(data["24-00220-01-05"]["sep"])
    y_sep = sum_hours_sep/1000
    
    sum_hours_oct = sum(data["24-00220-01-05"]["oct"])
    y_oct = sum_hours_oct/1000
    
    sum_hours_nov = sum(data["24-00220-01-05"]["nov"])
    y_nov = sum_hours_nov/1000
    
    sum_hours_dec = sum(data["24-00220-01-05"]["dec"])
    y_dec = sum_hours_dec/1000
    


    ## Graph data - Area 5

    x=["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y=[y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec]   
  
    plt.figure(5)
    plt.bar(x, y, color =area_colors ['Area 5'], width=0.4) 
    plt.xlabel("Month",labelpad=10 )
    plt.ylabel("Estimated Energy output",labelpad=10 )
    plt.title("Monthly Estimated Energy Output per Area - Area 5 [MWh]", pad=20)  
    plt.yticks([8,12,16,20,24,28,32,36,40])
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Monthly_E_per_Area_5.png', format='png')
    addlabels(x,y, padding=0.5)
    plt.show()

Monthly_Energy_per_Area()


def Annual_Energy_per_Area_Graph():


 # Area 1

    sum_hours_jan = sum(data["24-00220-01-01"]["jan"])
    sum_hours_feb = sum(data["24-00220-01-01"]["feb"])
    sum_hours_mar = sum(data["24-00220-01-01"]["mar"])
    sum_hours_apr = sum(data["24-00220-01-01"]["apr"])
    sum_hours_may = sum(data["24-00220-01-01"]["may"])
    sum_hours_jun = sum(data["24-00220-01-01"]["jun"])
    sum_hours_jul = sum(data["24-00220-01-01"]["jul"])
    sum_hours_aug = sum(data["24-00220-01-01"]["aug"])
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    sum_hours_oct = sum(data["24-00220-01-01"]["oct"])
    sum_hours_nov = sum(data["24-00220-01-01"]["nov"])
    sum_hours_dec = sum(data["24-00220-01-01"]["dec"])
    
    total_sum_hours_1 = sum ([sum_hours_jan,sum_hours_feb,sum_hours_mar,sum_hours_apr,
                           sum_hours_may,sum_hours_jun,sum_hours_jul,sum_hours_aug,
                           sum_hours_sep,sum_hours_oct, sum_hours_nov,sum_hours_dec])
    y_area_1 = total_sum_hours_1/1000  # changes unit to MWh
    print (y_area_1)


 # Area 2

    sum_hours_jan = sum(data["24-00220-01-02"]["jan"])
    sum_hours_feb = sum(data["24-00220-01-02"]["feb"])
    sum_hours_mar = sum(data["24-00220-01-02"]["mar"])
    sum_hours_apr = sum(data["24-00220-01-02"]["apr"])
    sum_hours_may = sum(data["24-00220-01-02"]["may"])
    sum_hours_jun = sum(data["24-00220-01-02"]["jun"])
    sum_hours_jul = sum(data["24-00220-01-02"]["jul"])
    sum_hours_aug = sum(data["24-00220-01-02"]["aug"])
    sum_hours_sep = sum(data["24-00220-01-02"]["sep"])
    sum_hours_oct = sum(data["24-00220-01-02"]["oct"])
    sum_hours_nov = sum(data["24-00220-01-02"]["nov"])
    sum_hours_dec = sum(data["24-00220-01-02"]["dec"])
    
    total_sum_hours_2 = sum ([sum_hours_jan,sum_hours_feb,sum_hours_mar,sum_hours_apr,
                           sum_hours_may,sum_hours_jun,sum_hours_jul,sum_hours_aug,
                           sum_hours_sep,sum_hours_oct, sum_hours_nov,sum_hours_dec])
    y_area_2 = total_sum_hours_2/1000
    print (y_area_2)


 # Area 3

    sum_hours_jan = sum(data["24-00220-01-03"]["jan"])
    sum_hours_feb = sum(data["24-00220-01-03"]["feb"])
    sum_hours_mar = sum(data["24-00220-01-03"]["mar"])
    sum_hours_apr = sum(data["24-00220-01-03"]["apr"])
    sum_hours_may = sum(data["24-00220-01-03"]["may"])
    sum_hours_jun = sum(data["24-00220-01-03"]["jun"])
    sum_hours_jul = sum(data["24-00220-01-03"]["jul"])
    sum_hours_aug = sum(data["24-00220-01-03"]["aug"])
    sum_hours_sep = sum(data["24-00220-01-03"]["sep"])
    sum_hours_oct = sum(data["24-00220-01-03"]["oct"])
    sum_hours_nov = sum(data["24-00220-01-03"]["nov"])
    sum_hours_dec = sum(data["24-00220-01-03"]["dec"])
    
    total_sum_hours_3 = sum ([sum_hours_jan,sum_hours_feb,sum_hours_mar,sum_hours_apr,
                           sum_hours_may,sum_hours_jun,sum_hours_jul,sum_hours_aug,
                           sum_hours_sep,sum_hours_oct, sum_hours_nov,sum_hours_dec])
    y_area_3 = total_sum_hours_3/1000
    print (y_area_3)

    
 # Area 4

    sum_hours_jan = sum(data["24-00220-01-04"]["jan"])
    sum_hours_feb = sum(data["24-00220-01-04"]["feb"])
    sum_hours_mar = sum(data["24-00220-01-04"]["mar"])
    sum_hours_apr = sum(data["24-00220-01-04"]["apr"])
    sum_hours_may = sum(data["24-00220-01-04"]["may"])
    sum_hours_jun = sum(data["24-00220-01-04"]["jun"])
    sum_hours_jul = sum(data["24-00220-01-04"]["jul"])
    sum_hours_aug = sum(data["24-00220-01-04"]["aug"])
    sum_hours_sep = sum(data["24-00220-01-04"]["sep"])
    sum_hours_oct = sum(data["24-00220-01-04"]["oct"])
    sum_hours_nov = sum(data["24-00220-01-04"]["nov"])
    sum_hours_dec = sum(data["24-00220-01-04"]["dec"])
    
    total_sum_hours_4 = sum ([sum_hours_jan,sum_hours_feb,sum_hours_mar,sum_hours_apr,
                           sum_hours_may,sum_hours_jun,sum_hours_jul,sum_hours_aug,
                           sum_hours_sep,sum_hours_oct, sum_hours_nov,sum_hours_dec])
    y_area_4 = total_sum_hours_4/1000
    print (y_area_4)


 # Area 5

    sum_hours_jan = sum(data["24-00220-01-05"]["jan"])
    sum_hours_feb = sum(data["24-00220-01-05"]["feb"])
    sum_hours_mar = sum(data["24-00220-01-05"]["mar"])
    sum_hours_apr = sum(data["24-00220-01-05"]["apr"])
    sum_hours_may = sum(data["24-00220-01-05"]["may"])
    sum_hours_jun = sum(data["24-00220-01-05"]["jun"])
    sum_hours_jul = sum(data["24-00220-01-05"]["jul"])
    sum_hours_aug = sum(data["24-00220-01-05"]["aug"])
    sum_hours_sep = sum(data["24-00220-01-05"]["sep"])
    sum_hours_oct = sum(data["24-00220-01-05"]["oct"])
    sum_hours_nov = sum(data["24-00220-01-05"]["nov"])
    sum_hours_dec = sum(data["24-00220-01-05"]["dec"])
    
    total_sum_hours_5 = sum ([sum_hours_jan,sum_hours_feb,sum_hours_mar,sum_hours_apr,
                           sum_hours_may,sum_hours_jun,sum_hours_jul,sum_hours_aug,
                           sum_hours_sep,sum_hours_oct, sum_hours_nov,sum_hours_dec])
    y_area_5 = total_sum_hours_5/1000
    print (y_area_5)
    


   # Global Graph


    x=["Area 1\nNW", "Area 2\nW", "Area 3\nSW","Area 4\nSSE","Area 5\nSW"]
    y=[y_area_1, y_area_2, y_area_3, y_area_4, y_area_5]   
    ytotal=sum(y)
    colors = [area_colors ['Area 1'],area_colors ['Area 2'], area_colors ['Area 3'],area_colors ['Area 4'], area_colors ['Area 5']]  
    plt.bar(x, y, color=colors, width=0.4)
    plt.ylabel("Estimated Energy output",labelpad=10)
    plt.title(f"Annual Estimated Energy Output per Area [MWh]\n ( Total Estimated Energy = {ytotal} MWh ) ", pad=20) # pad allows space between graph title and upper line of chart box
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Anual_E_per_Area.png', format='png')
    plt.yticks([0,50,100,150,200,250,300,350])

    # for i in range(len(x)):
        # plt.text(i,y[i] + 5,y[i] , ha='center')
    # props = dict(boxstyle='round', facecolor='mintcream', alpha=0.5)
    # plt.text(0.25, 0.80, textstr, transform=plt.gca().transAxes, fontsize=10,
            # verticalalignment='top', bbox=props)
  
    # Adjusting the bottom margin
    plt.subplots_adjust(top=0.80)  # Adjust the top margin to create more space for the title
    
    plt.show()

    
    print(sum(y))
    # addlabels(x, y)

Annual_Energy_per_Area_Graph()


def Avg_Monthly_Itemized_Energy_Output():

 # Area 1 

    sum_hours_jan = sum(data["24-00220-01-01"]["jan"])
    y_jan_1 = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-01"]["feb"])
    y_feb_1 = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-01"]["mar"])
    y_mar_1 = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-01"]["apr"])
    y_apr_1 = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-01"]["may"])
    y_may_1 = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-01"]["jun"])
    y_jun_1 = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-01"]["jul"])
    y_jul_1 = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-01"]["aug"])
    y_aug_1 = sum_hours_aug/1000
    
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    y_sep_1 = sum_hours_sep/1000
    
    sum_hours_oct = sum(data["24-00220-01-01"]["oct"])
    y_oct_1 = sum_hours_oct/1000
    
    sum_hours_nov = sum(data["24-00220-01-01"]["nov"])
    y_nov_1 = sum_hours_nov/1000
    
    sum_hours_dec = sum(data["24-00220-01-01"]["dec"])
    y_dec_1 = sum_hours_dec/1000
    

# Area 2 

    sum_hours_jan = sum(data["24-00220-01-02"]["jan"])
    y_jan_2 = sum_hours_jan/1000
 
    sum_hours_feb = sum(data["24-00220-01-02"]["feb"])
    y_feb_2 = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-02"]["mar"])
    y_mar_2 = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-02"]["apr"])
    y_apr_2 = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-02"]["may"])
    y_may_2 = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-02"]["jun"])
    y_jun_2 = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-02"]["jul"])
    y_jul_2 = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-02"]["aug"])
    y_aug_2 = sum_hours_aug/1000
    
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    y_sep_2 = sum_hours_sep/1000
    
    sum_hours_oct = sum(data["24-00220-01-02"]["oct"])
    y_oct_2 = sum_hours_oct/1000
    
    sum_hours_nov = sum(data["24-00220-01-02"]["nov"])
    y_nov_2 = sum_hours_nov/1000
    
    sum_hours_dec = sum(data["24-00220-01-02"]["dec"])
    y_dec_2 = sum_hours_dec/1000
    


    
# Area 3 

    sum_hours_jan = sum(data["24-00220-01-03"]["jan"])
    y_jan_3 = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-03"]["feb"])
    y_feb_3 = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-03"]["mar"])
    y_mar_3 = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-03"]["apr"])
    y_apr_3 = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-03"]["may"])
    y_may_3= sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-03"]["jun"])
    y_jun_3 = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-03"]["jul"])
    y_jul_3 = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-03"]["aug"])
    y_aug_3 = sum_hours_aug/1000

    sum_hours_sep = sum(data["24-00220-01-03"]["sep"])
    y_sep_3 = sum_hours_sep/1000

    sum_hours_oct = sum(data["24-00220-01-03"]["oct"])
    y_oct_3 = sum_hours_oct/1000

    sum_hours_nov = sum(data["24-00220-01-03"]["nov"])
    y_nov_3 = sum_hours_nov/1000

    sum_hours_dec = sum(data["24-00220-01-03"]["dec"])
    y_dec_3 = sum_hours_dec/1000



# Area 4 

    sum_hours_jan = sum(data["24-00220-01-04"]["jan"])
    y_jan_4 = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-04"]["feb"])
    y_feb_4 = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-04"]["mar"])
    y_mar_4 = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-04"]["apr"])
    y_apr_4 = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-04"]["may"])
    y_may_4 = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-04"]["jun"])
    y_jun_4 = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-04"]["jul"])
    y_jul_4 = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-04"]["aug"])
    y_aug_4= sum_hours_aug/1000

    sum_hours_sep = sum(data["24-00220-01-04"]["sep"])
    y_sep_4 = sum_hours_sep/1000

    sum_hours_oct = sum(data["24-00220-01-04"]["oct"])
    y_oct_4 = sum_hours_oct/1000

    sum_hours_nov = sum(data["24-00220-01-04"]["nov"])
    y_nov_4 = sum_hours_nov/1000

    sum_hours_dec = sum(data["24-00220-01-04"]["dec"])
    y_dec_4 = sum_hours_dec/1000


    
# Area 5 

    sum_hours_jan = sum(data["24-00220-01-05"]["jan"])
    y_jan_5 = sum_hours_jan/1000

    sum_hours_feb = sum(data["24-00220-01-05"]["feb"])
    y_feb_5 = sum_hours_feb/1000

    sum_hours_mar = sum(data["24-00220-01-05"]["mar"])
    y_mar_5 = sum_hours_mar/1000

    sum_hours_apr = sum(data["24-00220-01-05"]["apr"])
    y_apr_5 = sum_hours_apr/1000

    sum_hours_may = sum(data["24-00220-01-05"]["may"])
    y_may_5 = sum_hours_may/1000

    sum_hours_jun = sum(data["24-00220-01-05"]["jun"])
    y_jun_5 = sum_hours_jun/1000

    sum_hours_jul = sum(data["24-00220-01-05"]["jul"])
    y_jul_5 = sum_hours_jul/1000

    sum_hours_aug = sum(data["24-00220-01-05"]["aug"])
    y_aug_5 = sum_hours_aug/1000
    
    sum_hours_sep = sum(data["24-00220-01-05"]["sep"])
    y_sep_5 = sum_hours_sep/1000
    
    sum_hours_oct = sum(data["24-00220-01-05"]["oct"])
    y_oct_5 = sum_hours_oct/1000
    
    sum_hours_nov = sum(data["24-00220-01-05"]["nov"])
    y_nov_5 = sum_hours_nov/1000
    
    sum_hours_dec = sum(data["24-00220-01-05"]["dec"])
    y_dec_5 = sum_hours_dec/1000
    


    ## Global Graph data

    x=["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y1=[y_jan_1, y_feb_1, y_mar_1, y_apr_1, y_may_1, y_jun_1, y_jul_1, y_aug_1, y_sep_1, y_oct_1, y_nov_1, y_dec_1]   
    y2=[y_jan_2, y_feb_2, y_mar_2, y_apr_2, y_may_2, y_jun_2, y_jul_2, y_aug_2, y_sep_2, y_oct_2, y_nov_2, y_dec_2] 
    y3=[y_jan_3, y_feb_3, y_mar_3, y_apr_3, y_may_3, y_jun_3, y_jul_3, y_aug_3, y_sep_3, y_oct_3, y_nov_3, y_dec_3] 
    y4=[y_jan_4, y_feb_4, y_mar_4, y_apr_4, y_may_4, y_jun_4, y_jul_4, y_aug_4, y_sep_4, y_oct_4, y_nov_4, y_dec_4] 
    y5=[y_jan_5, y_feb_5, y_mar_5, y_apr_5, y_may_5, y_jun_5, y_jul_5, y_aug_5, y_sep_5, y_oct_5, y_nov_5, y_dec_5] 
    
    # Convert lists to numpy arrays for easier manipulation
    y1 = np.array(y1)
    y2 = np.array(y2)
    y3 = np.array(y3)
    y4 = np.array(y4)
    y5 = np.array(y5)

    # y=[y1,y2,y3,y4,y5]
    ytotal = y1.sum() + y2.sum() + y3.sum() + y4.sum() + y5.sum()
    # Create the stacked area plot
    plt.figure(1,figsize=(6, 5))
    plt.stackplot(x, y1, y2, y3, y4, y5, labels=['Area 1', 'Area 2', 'Area 3', 'Area 4', 'Area 5'], colors=['lightcoral','khaki', 'plum','cornflowerblue','limegreen'])
    plt.xlabel("Month", labelpad=10)
    plt.ylabel("Energy Output (MWh)", labelpad=10)
    plt.legend(loc='upper right')
    plt.title(f"Average Monthly Itemized Energy Output - [MWh]\n Total = {ytotal:.2f}", pad=15) # 
    # labels 
    # mid_index = x.index("Jun")
    # cumulative_y = np.zeros(len(x))
    # for i, y_layer in enumerate([y1, y2, y3, y4, y5]):
        # cumulative_y += y_layer
        # plt.text(x[mid_index], cumulative_y[mid_index] - y_layer[mid_index] / 2, f'{sum(y[i]):.1f}', ha='center', va='center')
    # props = dict(boxstyle='round', facecolor='mintcream', alpha=0.5)
    # plt.text(0.05, 0.80, textstr, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=props)    
    plt.show()
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Avg_Monthly_Itemized_Energy_Output.png', format='png')

Avg_Monthly_Itemized_Energy_Output()

 
def Hourly_Compound_Energy_Output():    


    # December 

    y_area_1_ = [0] * 24
    y_area_2_ = [0] * 24
    y_area_3_ = [0] * 24
    y_area_4_ = [0] * 24
    y_area_5_ = [0] * 24


    for i in range (4,21):   

        y_area_1_[i]= data["24-00220-01-01"]["dec"][i]
        y_area_2_[i]= data["24-00220-01-02"]["dec"][i]
        y_area_3_[i]= data["24-00220-01-03"]["dec"][i]
        y_area_4_[i]= data["24-00220-01-04"]["dec"][i]
        y_area_5_[i]= data["24-00220-01-05"]["dec"][i]
    

    ## Graph data December

    x = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    y1 = np.array(y_area_1_[4:21])
    y2 = np.array(y_area_2_[4:21])
    y3 = np.array(y_area_3_[4:21])
    y4 = np.array(y_area_4_[4:21])
    y5 = np.array(y_area_5_[4:21])
    

    # plot bars in stack manner

    plt.bar(x, y1, color = area_colors ['Area 1'])
    plt.bar(x, y2, bottom = y1, color=area_colors['Area 2'])
    plt.bar(x, y3, bottom = y1 + y2, color=area_colors['Area 3'] )
    plt.bar(x, y4, bottom = y1 + y2 + y3, color=area_colors['Area 4'])
    plt.bar(x, y5, bottom = y1 + y2 + y3 + y4, color=area_colors['Area 5'])
    plt.legend(["Area 1 - NW", "Area 2 - W", "Area 3 - SW", "Area 4 - SSE", "Area 5 - SW"], loc='upper left')
    plt.xlabel("Hour",labelpad=10)
    plt.ylabel("Hourly Energy Output",labelpad=10)
    plt.title("Hourly Compound Energy Output - December [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Hourly Compound Energy Output - December.png', format='png')
    textstr = 'Daylight hours=8h'
    props = dict(boxstyle='round', facecolor='mintcream', alpha=0.5)
    plt.text(0.05, 0.40, textstr, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=props)
    plt.show()




    # March 

    y_area_1_ = [0] * 24
    y_area_2_ = [0] * 24
    y_area_3_ = [0] * 24
    y_area_4_ = [0] * 24
    y_area_5_ = [0] * 24


    for i in range (4,21):   

        y_area_1_[i]= data["24-00220-01-01"]["mar"][i]
        y_area_2_[i]= data["24-00220-01-02"]["mar"][i]
        y_area_3_[i]= data["24-00220-01-03"]["mar"][i]
        y_area_4_[i]= data["24-00220-01-04"]["mar"][i]
        y_area_5_[i]= data["24-00220-01-05"]["mar"][i]
    

    ## Graph data March

    x = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    y1 = np.array(y_area_1_[4:21])
    y2 = np.array(y_area_2_[4:21])
    y3 = np.array(y_area_3_[4:21])
    y4 = np.array(y_area_4_[4:21])
    y5 = np.array(y_area_5_[4:21])
    

    plt.bar(x, y1, color =area_colors ['Area 1'])
    plt.bar(x, y2, bottom = y1, color=area_colors ['Area 2'])
    plt.bar(x, y3, bottom = y1 + y2, color=area_colors ['Area 3'])
    plt.bar(x, y4, bottom = y1 + y2 + y3, color=area_colors ['Area 4'])
    plt.bar(x, y5, bottom = y1 + y2 + y3 + y4, color=area_colors ['Area 5'])
    plt.legend(["Area 1 - NW", "Area 2 - W", "Area 3 - SW", "Area 4 - SSE", "Area 5 - SW"])
    plt.xlabel("Hour", labelpad=10)
    plt.ylabel("Hourly Energy Output", labelpad=10)
    plt.title("Hourly Compound Energy Output - March [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Hourly Compound Energy Output - March.png', format='png')
    textstr = 'Daylight hours=11h'
    props = dict(boxstyle='round', facecolor='mintcream', alpha=0.5)
    plt.text(0.05, 0.40, textstr, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=props)
    plt.show()


    # June

    y_area_1_ = [0] * 24
    y_area_2_ = [0] * 24
    y_area_3_ = [0] * 24
    y_area_4_ = [0] * 24
    y_area_5_ = [0] * 24


    for i in range (4,21):   

        y_area_1_[i]= data["24-00220-01-01"]["jun"][i]
        y_area_2_[i]= data["24-00220-01-02"]["jun"][i]
        y_area_3_[i]= data["24-00220-01-03"]["jun"][i]
        y_area_4_[i]= data["24-00220-01-04"]["jun"][i]
        y_area_5_[i]= data["24-00220-01-05"]["jun"][i]
    

    ## Graph data June

    x = ["4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    y1 = np.array(y_area_1_[4:21])
    y2 = np.array(y_area_2_[4:21])
    y3 = np.array(y_area_3_[4:21])
    y4 = np.array(y_area_4_[4:21])
    y5 = np.array(y_area_5_[4:21])
    y=[y1,y2,y3,y4,y5]

    plt.bar(x, y1, color = area_colors ['Area 1'])
    plt.bar(x, y2, bottom = y1, color=area_colors ['Area 2'])
    plt.bar(x, y3, bottom = y1 + y2, color=area_colors ['Area 3'])
    plt.bar(x, y4, bottom = y1 + y2 + y3, color=area_colors ['Area 4'])
    plt.bar(x, y5, bottom = y1 + y2 + y3 + y4, color=area_colors ['Area 5'])
    plt.legend(["Area 1 - NW", "Area 2 - W", "Area 3 - SW", "Area 4 - SSE", "Area 5 - SW"])
    plt.xlabel("Hour",labelpad=10)
    plt.ylabel("Hourly Energy Output",labelpad=10)
    plt.title("Hourly Compound Energy Output - June [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Hourly Compound Energy Output - June.png', format='png')
    
    # Adding value labels
    # for i in range(len(x)):
        # cumulative_height = 0
        # for j in range(len(y)):
            #cumulative_height += y[j][i]
            # plt.text(i, cumulative_height - y[j][i]/2, f'{y[j][i]:.1f}', ha='center')
    

    textstr = 'Daylight hours=14h'
    props = dict(boxstyle='round', facecolor='mintcream', alpha=0.5)
    plt.text(0.05, 0.40, textstr, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=props)
    plt.show()

Hourly_Compound_Energy_Output()


def Avg_Daily_Energy_Output():

    # Area 1 

    sum_hours_jan = sum(data["24-00220-01-01"]["jan"])
    y_jan = sum_hours_jan/31

    sum_hours_feb = sum(data["24-00220-01-01"]["feb"])
    y_feb = sum_hours_feb/29

    sum_hours_mar = sum(data["24-00220-01-01"]["mar"])
    y_mar = sum_hours_mar/31

    sum_hours_apr = sum(data["24-00220-01-01"]["apr"])
    y_apr = sum_hours_apr/30

    sum_hours_may = sum(data["24-00220-01-01"]["may"])
    y_may = sum_hours_may/31

    sum_hours_jun = sum(data["24-00220-01-01"]["jun"])
    y_jun = sum_hours_jun/30

    sum_hours_jul = sum(data["24-00220-01-01"]["jul"])
    y_jul = sum_hours_jul/31

    sum_hours_aug = sum(data["24-00220-01-01"]["aug"])
    y_aug = sum_hours_aug/31
    
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    y_sep = sum_hours_sep/30
    
    sum_hours_oct = sum(data["24-00220-01-01"]["oct"])
    y_oct = sum_hours_oct/31
    
    sum_hours_nov = sum(data["24-00220-01-01"]["nov"])
    y_nov = sum_hours_nov/30
    
    sum_hours_dec = sum(data["24-00220-01-01"]["dec"])
    y_dec = sum_hours_dec/31
    

    ## Graph data - Area 1

    x=np.array(["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    y=np.array([y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec])   
     
    # Create a numerical representation of the months for interpolation
    x_numeric = np.arange(len(x))

    X_Y_Spline = make_interp_spline(x_numeric, y)
 
    # Returns evenly spaced numbers over a specified interval.
    X_ = np.linspace(x_numeric.min(), x_numeric.max(), 500)
    Y_ = X_Y_Spline(X_)

    # plt.yticks([4,8,12,16,20,24,28,32,36,40])
    plt.figure(1)
    # plt.bar(x, y, color='red', width=0.4)   # P/ fazer gräficos de barras
    plt.plot (X_, Y_, color =area_colors ['Area 1']) 
    plt.xticks(x_numeric, x)  # Use the original month names as x-axis labels
    plt.xlabel("Month",labelpad=10)
    plt.ylabel("Estimated Energy output",labelpad=10)
    plt.title("Average Daily Estimated Energy Output - Area 1 [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Avg_Daily_Energy_Area_1.png', format='png')
    # addlabels(x,y, padding=10)
    plt.show()


# Area 2 

    sum_hours_jan = sum(data["24-00220-01-02"]["jan"])
    y_jan = sum_hours_jan/31
 
    sum_hours_feb = sum(data["24-00220-01-02"]["feb"])
    y_feb = sum_hours_feb/29

    sum_hours_mar = sum(data["24-00220-01-02"]["mar"])
    y_mar = sum_hours_mar/31

    sum_hours_apr = sum(data["24-00220-01-02"]["apr"])
    y_apr = sum_hours_apr/30

    sum_hours_may = sum(data["24-00220-01-02"]["may"])
    y_may = sum_hours_may/31

    sum_hours_jun = sum(data["24-00220-01-02"]["jun"])
    y_jun = sum_hours_jun/30

    sum_hours_jul = sum(data["24-00220-01-02"]["jul"])
    y_jul = sum_hours_jul/31

    sum_hours_aug = sum(data["24-00220-01-02"]["aug"])
    y_aug = sum_hours_aug/31
    
    sum_hours_sep = sum(data["24-00220-01-01"]["sep"])
    y_sep = sum_hours_sep/30
    
    sum_hours_oct = sum(data["24-00220-01-02"]["oct"])
    y_oct = sum_hours_oct/31
    
    sum_hours_nov = sum(data["24-00220-01-02"]["nov"])
    y_nov = sum_hours_nov/30
    
    sum_hours_dec = sum(data["24-00220-01-02"]["dec"])
    y_dec = sum_hours_dec/31
    


    ## Graph data - Area 2


    x=np.array(["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    y=np.array([y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec])   
     
    # Create a numerical representation of the months for interpolation
    x_numeric = np.arange(len(x))

    X_Y_Spline = make_interp_spline(x_numeric, y)
 
    # Returns evenly spaced numbers over a specified interval.
    X_ = np.linspace(x_numeric.min(), x_numeric.max(), 500)
    Y_ = X_Y_Spline(X_)

    
    plt.figure(1)
    plt.plot (X_, Y_, color =area_colors ['Area 2']) 
    plt.xticks(x_numeric, x)  # Use the original month names as x-axis labels
    plt.ylabel("Estimated Energy output",labelpad=10,)
    plt.title("Average Daily Estimated Energy Output per Area - Area 2 [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Avg_Daily_Energy_Area_2', format='png')
    # addlabels(x,y,padding=10)
    plt.show()


    
# Area 3 

    sum_hours_jan = sum(data["24-00220-01-03"]["jan"])
    y_jan = sum_hours_jan/31

    sum_hours_feb = sum(data["24-00220-01-03"]["feb"])
    y_feb = sum_hours_feb/29

    sum_hours_mar = sum(data["24-00220-01-03"]["mar"])
    y_mar = sum_hours_mar/31

    sum_hours_apr = sum(data["24-00220-01-03"]["apr"])
    y_apr = sum_hours_apr/30

    sum_hours_may = sum(data["24-00220-01-03"]["may"])
    y_may = sum_hours_may/31

    sum_hours_jun = sum(data["24-00220-01-03"]["jun"])
    y_jun = sum_hours_jun/30

    sum_hours_jul = sum(data["24-00220-01-03"]["jul"])
    y_jul = sum_hours_jul/31

    sum_hours_aug = sum(data["24-00220-01-03"]["aug"])
    y_aug = sum_hours_aug/31

    sum_hours_sep = sum(data["24-00220-01-03"]["sep"])
    y_sep = sum_hours_sep/30

    sum_hours_oct = sum(data["24-00220-01-03"]["oct"])
    y_oct = sum_hours_oct/31

    sum_hours_nov = sum(data["24-00220-01-03"]["nov"])
    y_nov = sum_hours_nov/30

    sum_hours_dec = sum(data["24-00220-01-03"]["dec"])
    y_dec = sum_hours_dec/31



    ## Graph data - Area 3


    x=np.array(["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    y=np.array([y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec])   
     
    # Create a numerical representation of the months for interpolation
    x_numeric = np.arange(len(x))

    X_Y_Spline = make_interp_spline(x_numeric, y)
 
    # Returns evenly spaced numbers over a specified interval.
    X_ = np.linspace(x_numeric.min(), x_numeric.max(), 500)
    Y_ = X_Y_Spline(X_)

    plt.figure(1)
    plt.plot (X_, Y_,color=area_colors ['Area 3'] ) 
    plt.xticks(x_numeric, x)  # Use the original month names as x-axis labels
    plt.xlabel("Month", labelpad=10,)
    plt.ylabel("Estimated Energy output",labelpad=10 )
    plt.title("Average Daily Estimated Energy Output per Area - Area 3 [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Avg_Daily_Energy_Area_3.png', format='png')
    # addlabels(x,y)
    plt.show()


# Area 4 

    sum_hours_jan = sum(data["24-00220-01-04"]["jan"])
    y_jan = sum_hours_jan/31

    sum_hours_feb = sum(data["24-00220-01-04"]["feb"])
    y_feb = sum_hours_feb/29

    sum_hours_mar = sum(data["24-00220-01-04"]["mar"])
    y_mar = sum_hours_mar/31

    sum_hours_apr = sum(data["24-00220-01-04"]["apr"])
    y_apr = sum_hours_apr/30

    sum_hours_may = sum(data["24-00220-01-04"]["may"])
    y_may = sum_hours_may/31

    sum_hours_jun = sum(data["24-00220-01-04"]["jun"])
    y_jun = sum_hours_jun/30

    sum_hours_jul = sum(data["24-00220-01-04"]["jul"])
    y_jul = sum_hours_jul/31

    sum_hours_aug = sum(data["24-00220-01-04"]["aug"])
    y_aug = sum_hours_aug/31

    sum_hours_sep = sum(data["24-00220-01-04"]["sep"])
    y_sep = sum_hours_sep/30

    sum_hours_oct = sum(data["24-00220-01-04"]["oct"])
    y_oct = sum_hours_oct/31

    sum_hours_nov = sum(data["24-00220-01-04"]["nov"])
    y_nov = sum_hours_nov/30

    sum_hours_dec = sum(data["24-00220-01-04"]["dec"])
    y_dec = sum_hours_dec/31



    ## Graph data - Area 4


    x=np.array(["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    y=np.array([y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec])   
     
    # Create a numerical representation of the months for interpolation
    x_numeric = np.arange(len(x))

    X_Y_Spline = make_interp_spline(x_numeric, y)
 
    # Returns evenly spaced numbers over a specified interval.
    X_ = np.linspace(x_numeric.min(), x_numeric.max(), 500)
    Y_ = X_Y_Spline(X_)
    plt.figure(1)
    plt.plot (X_, Y_, color =area_colors ['Area 4']) 
    plt.xticks(x_numeric, x)  # Use the original month names as x-axis labels
    plt.xlabel("Month",labelpad=10)
    plt.ylabel("Estimated Energy output",labelpad=10)
    plt.title("Average Daily Estimated Energy Output per Area - Area 4 [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Avg_Daily_Energy_Area_4.png', format='png')
    # addlabels(x,y)
    plt.show()


    
# Area 5 

#   sum_hours_jan = sum(data["24-00220-01-05"]["jan"])
    y_jan = sum_hours_jan/31

    sum_hours_feb = sum(data["24-00220-01-05"]["feb"])
    y_feb = sum_hours_feb/29

    sum_hours_mar = sum(data["24-00220-01-05"]["mar"])
    y_mar = sum_hours_mar/30

    sum_hours_apr = sum(data["24-00220-01-05"]["apr"])
    y_apr = sum_hours_apr/31

    sum_hours_may = sum(data["24-00220-01-05"]["may"])
    y_may = sum_hours_may/30

    sum_hours_jun = sum(data["24-00220-01-05"]["jun"])
    y_jun = sum_hours_jun/30

    sum_hours_jul = sum(data["24-00220-01-05"]["jul"])
    y_jul = sum_hours_jul/31

    sum_hours_aug = sum(data["24-00220-01-05"]["aug"])
    y_aug = sum_hours_aug/31
    
    sum_hours_sep = sum(data["24-00220-01-05"]["sep"])
    y_sep = sum_hours_sep/30
    
    sum_hours_oct = sum(data["24-00220-01-05"]["oct"])
    y_oct = sum_hours_oct/31
    
    sum_hours_nov = sum(data["24-00220-01-05"]["nov"])
    y_nov = sum_hours_nov/30
    
    sum_hours_dec = sum(data["24-00220-01-05"]["dec"])
    y_dec = sum_hours_dec/31
    


    ## Graph data - Area 5

   
    x=np.array(["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    y=np.array([y_jan, y_feb, y_mar, y_apr, y_may, y_jun, y_jul, y_aug, y_sep, y_oct, y_nov, y_dec])   
     
    # Create a numerical representation of the months for interpolation
    x_numeric = np.arange(len(x))   

    # Creates a smoother curved line
    X_Y_Spline = make_interp_spline(x_numeric, y)
 
    # Returns evenly spaced numbers over a specified interval.
    X_ = np.linspace(x_numeric.min(), x_numeric.max(), 500)
    Y_ = X_Y_Spline(X_)

 
    plt.figure(1)
    plt.plot (X_, Y_, color =area_colors ['Area 5']) # If we want go back to the origiinal graphs must match the wit x and y.
    plt.xticks(x_numeric, x)  # Use the original month names as x-axis labels
    plt.xlabel("Month",labelpad=10)
    plt.ylabel("Estimated Energy output",labelpad=10)
    plt.title("Average Daily Estimated Energy Output per Area - Area 5 [kWh]", pad=20)
    plt.savefig('//SRVDABU02/Benutzerordner$/sofia.teixeira/Desktop/Projects/PythonProjects/Solar_Studies/Hector_Egger/Graphs/Avg_Daily_Energy_Area_5.png', format='png')
    # addlabels(x,y)
    plt.show()


Avg_Daily_Energy_Output()
