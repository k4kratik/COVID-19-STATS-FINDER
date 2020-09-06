import pandas as pd 
from state_wise_data import state_output
import sys

def output(retrieved_data,your_state):
    if your_state == 'initial_flag':
        your_state = int(input("\nEnter Your State ID to check current COVID-19 Condition OR you can enter 0 (zero) to print "
                       "data of all states:\t"))

    if your_state not in range(len(retrieved_data[0])+1):
        print("Please Enter A Valid Integer according to your State.")
    elif your_state == 0:
        # OLD
        # for i in range(1, len(retrieved_data[0])+1):
        #     output(retrieved_data[1], retrieved_data[0], i)
        df = pd.DataFrame(list(retrieved_data[0].values()), columns = ['CONFIRMED', 'ACTIVE', 'RECOVERED', 'DEATHS'],index=list(retrieved_data[0].keys()))
        print(df.to_markdown())
        print("")      
    else:
        state_output(retrieved_data[1], retrieved_data[0], your_state)
        print("")

    continuation_flag = input("Enter other state's code(0 for all states) to get data or enter anything else to quit : ")
    print("")
    if continuation_flag == 'q' or continuation_flag == 'Q' :
        # sys.exit(0)
        return False 
    else:
        try:
            output(retrieved_data, int(continuation_flag))
        except:
            print("Please enter a valid input!")

