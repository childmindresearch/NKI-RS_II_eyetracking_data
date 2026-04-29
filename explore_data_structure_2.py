#### explore_data_structure_2
import pandas as pd 
import os 

# Set directory 
directory = '/home/nburke/Documents/NKI-RS_II_eyetracking_data_outputs'
os.chdir(directory)
print(os.getcwd())

### Custom functions for script 
def descr_stats(df, column_name):
    stats = df[column_name].agg(
        mean='mean',
        min='min',
        max='max',
        std='std'
    )
    print(f"Summary stats for column: {column_name}")
    print(stats)

    return stats

# Read in data 
# present_ds2_left_eye_df = pd.read_csv('present_ds2_left_eye_df.csv')
# present_ds2_right_eye_df = pd.read_csv('present_ds2_right_eye_df.csv')
# sherlock_ds2_left_eye_df = pd.read_csv('sherlock_ds2_left_eye_df.csv')
sherlock_ds2_right_eye_df = pd.read_csv('sherlock_ds2_right_eye_df.csv')

# Check data 
# print(f"present_ds2_left_eye_df {present_ds2_left_eye_df.head()}")
# print(f"present_ds2_right_eye_df {present_ds2_right_eye_df.head()}")
# print(f"sherlock_ds2_left_eye_df {sherlock_ds2_left_eye_df.head()}")
print(f"sherlock_ds2_right_eye_df {sherlock_ds2_right_eye_df.head()}")


########################### SHERLOCK RIGHT EYE ###########################
check_zero = sherlock_ds2_right_eye_df.groupby('subjectID')['rightEyeX'].sum()
print(f"values are 0 then subjecct had no ET data: {check_zero}")

