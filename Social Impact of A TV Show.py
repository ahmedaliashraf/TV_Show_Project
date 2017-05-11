#Original Python 3.6 code by Ahmed Ashraf, Spring 2017
#Investigate the social imapct of a TV show by
#Calculating the total number of newborn named after
#characters from the show each year
 

import matplotlib.pyplot as plt
import re
import pandas as pd
import stats

def readTxtFileWithPattern(fileName,pattern):
    f = open(fileName)
    names = f.read().split()
    count = 0;
    for i in range(len(names)):
        splitName = names[i].split(",")
        if(re.search(pattern,splitName[0])):
            count += int(splitName[2])
    return count
        
def calculateTotalWithPattern(years,pattern):
    count = []
    for i in range (len(years)):
        fileName = "nationalNameDataByYear\yob" + str(years[i])+ ".txt"
        count.append(readTxtFileWithPattern(fileName,pattern))
    return count

def calculateTotalAndPlotForShow(showName,characters,years):
    #list to hold corrlation for each character
    corrList= []
    
    #avaialble colors for character label in plot
    colors = ['b','g','r','m','y','c','k']      
    
    #Obtain viwership data of TV Show(showName) by reading csv file
    viewerData = pd.read_csv("viewershipData/" + str(showName) + ".csv")
    viewership = [float(x) for x in viewerData['viewers']]
    #print(viewership)
    
    #For each character calculate total for each year and plot
    fig,(bx,ax) = plt.subplots(2,sharex=True)  #Setup figure and subplots
    for i in range(len(characters)):
        countPerYear = calculateTotalWithPattern(years,characters[i])                      #Variable to store count for each year
        ax.plot(years, countPerYear, color=colors[i], label=characters[i])         #Plot name count with different color
        corrList.append(stats.correlation(viewership,countPerYear))
    bx.plot(years, viewership, color='k', label="viewership")    
    
    #plt.title("Popularity of " + showName + 
    #          " and Kids Named similarly to characters it From 1990 to 2015")       #Title for plot
    bx.set_title("Popularity of " + showName)
    ax.set_title("Number of Kids Named after Characters")
    
    ax.set_xlabel('Year')                #Label for x-axis
    ax.set_ylabel('Count')               #Label for y-axis
    bx.set_ylabel('Count (in millions)')
    
    ax.legend(loc = 0,fontsize = 'x-small')#Make a legend in upper left corner
    bx.legend(loc = 0,fontsize = 'x-small')#Make a legend in upper left corner
    plt.show()
    
    #print correlation between and children named after chracters
    print("Correlation between "+showName+" viewership and ")
    for j in range(len(characters)):
        print("children named "+characters[j]+" : "+"{0:.3f}".format(corrList[j]))


def calculateTotalAndPlotSeparateForEachShowAndCharacter(showName,characters,years):
    #path
    path = "visuals/IndependentPlot/"
    
    #list to hold corrlation for each character
    corrList= []
    
    #avaialble colors for character label in plot
    colors = ['b','g','r','m','y','#FFD5F0','c']      
    
    #Obtain viwership data of TV Show(showName) by reading csv file
    viewerData = pd.read_csv("viewershipData/" + str(showName) + ".csv")
    viewership = [float(x) for x in viewerData['viewers']]   
    
    #For each character calculate total for each year and plot
    for i in range(len(characters)):
        countPerYear = calculateTotalWithPattern(years,characters[i])                      #Variable to store count for each year
        corrList.append(stats.correlation(viewership,countPerYear))
        plt.plot(years, countPerYear, color=colors[i], label=characters[i])         #Plot name count with different color
        plt.title("Number of Newborn Named " + characters[i])
        plt.xlabel("year")
        plt.ylabel("count")
        #plt.legend(loc = 0,fontsize = 'x-small')#Make a legend in upper left corner
        plt.show()
        completeName = path+showName+"/"+characters[i]+".png"
        #plt.savefig(completeName)
        
    plt.title("Viewership of "+ showName)
    plt.plot(years, viewership, color='k', label="viewership") 
    plt.xlabel("year")
    plt.ylabel("count (in millions)")
    plt.show()
    
    completeName = showName+"/"+showName+"viewership.png"
    #plt.savefig(completeName)
    
    
    #print correlation between and children named after chracters
    print("Correlation between "+showName+" viewership and ")
    for j in range(len(characters)):
        print("children named "+characters[j]+" : "+"{0:.3f}".format(corrList[j]))
      
def main():
    
    #An array containg the years for which we have data
    #could have just used year = 1990 and increment in loop for fileName,
    #but need year array for scatter plot x any way.
    years = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,
             2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
    
    #ask user preference of plot type
    pref = input("Would you prefer Single (S) or Independent (I) plots: ").upper()
    if pref != "S" and pref !="I":
        pref = input("Would you prefer Single (S) or Independent (I) plot: ").upper()
    
    print("\n")
    
    #First TV Show-The Big Bang Theory
    print("First TV Show-The Big Bang Theory")
        #pattern defining various character names
    characters = ["Penny","Sheldon","Leonard","Raj","Leonard","Howard"] #"Leonard"
    
    if pref == "S":
        calculateTotalAndPlotForShow("The Big Bang Theory",characters,years)
    else:
        calculateTotalAndPlotSeparateForEachShowAndCharacter("The Big Bang Theory",characters,years)
    print("===============================================\n\n")
    
    #Second TV Show- How I Met Your Mother
    print("Second TV Show- How I Met Your Mother")
        #pattern defining various character names
    characters = ["Barney","Robin","Ted","Lily","Marshall"] #"Lily"
    
    if pref == "S":
        calculateTotalAndPlotForShow("HIMYM",characters,years)
    else:
        calculateTotalAndPlotSeparateForEachShowAndCharacter("HIMYM",characters,years)
    print("===============================================\n\n")
    
    #Third TV Show- Game of Thrones
    print("Third TV Show- Game of Thrones")
        #pattern defining various character names
    characters = ["Daenerys","Khaleesi","Jon","Snow","Arya","Sansa","Tyrion"] #"Jon","Arya",
    
    if pref == "S":
        calculateTotalAndPlotForShow("GoT",characters,years) 
    else:
        calculateTotalAndPlotSeparateForEachShowAndCharacter("GoT",characters,years)  
    print("===============================================\n\n")
    
main()