
# Importing the libraries
import pandas as pd

# Declaring Global variables
project_name = None


# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')

# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    
    global scrappedReviews
    global project_name
    
    project_name = "Sentiment Analysis with Insights"
    print("My project name = ", project_name)
    print('my scrapped data = ', scrappedReviews.sample(5) )
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
        
# Calling the main function 
if __name__ == '__main__':
    main()
    
    
    