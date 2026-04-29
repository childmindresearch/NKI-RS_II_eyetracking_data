#### explore_data_structure_2
import pandas as pd 
import os 

# Set directory 
directory = '/home/nburke/Documents/NKI-RS_II_eyetracking_data_outputs'
os.chdir(directory)
print(os.getcwd())

# Read in data 
present_ds2_left_eye_df = pd.read_csv('present_ds2_left_eye_df.csv')
present_ds2_right_eye_df = pd.read_csv('present_ds2_right_eye_df.csv')
sherlock_ds2_left_eye_df = pd.read_csv('sherlock_ds2_left_eye_df.csv')
sherlock_ds2_right_eye_df = pd.read_csv('sherlock_ds2_right_eye_df.csv')

# Check data 
print(f"present_ds2_left_eye_df {present_ds2_left_eye_df.head()}")
print(f"present_ds2_right_eye_df {present_ds2_right_eye_df.head()}")
print(f"sherlock_ds2_left_eye_df {sherlock_ds2_left_eye_df.head()}")
print(f"sherlock_ds2_right_eye_df {sherlock_ds2_right_eye_df.head()}")

