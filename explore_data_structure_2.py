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
present_ds2_left_eye_df = pd.read_csv('present_ds2_left_eye_df.csv')
present_ds2_right_eye_df = pd.read_csv('present_ds2_right_eye_df.csv')
sherlock_ds2_left_eye_df = pd.read_csv('sherlock_ds2_left_eye_df.csv')
sherlock_ds2_right_eye_df = pd.read_csv('sherlock_ds2_right_eye_df.csv')

# Check data 
# print(f"present_ds2_left_eye_df {present_ds2_left_eye_df.head()}")
# print(f"present_ds2_right_eye_df {present_ds2_right_eye_df.head()}")
# print(f"sherlock_ds2_left_eye_df {sherlock_ds2_left_eye_df.head()}")
print(f"sherlock_ds2_right_eye_df {sherlock_ds2_right_eye_df.head()}")


########################### SHERLOCK RIGHT EYE ###########################
check_zero_x = sherlock_ds2_right_eye_df.groupby('subjectID')['rightEyeX'].sum()
subjects_with_zero = check_zero_x[check_zero_x == 0]
print(f"Number of Subject with 0 for sherlock_right_eye_x: {len(subjects_with_zero)}")

check_zero_y = sherlock_ds2_right_eye_df.groupby('subjectID')['rightEyeY'].sum()
subjects_with_zero = check_zero_y[check_zero_y == 0]
print(f"Number of Subject with 0 for sherlock_right_eye_y: {len(subjects_with_zero)}")

########################### SHERLOCK LEFT EYE ###########################
check_zero_x = sherlock_ds2_left_eye_df.groupby('subjectID')['leftEyeX'].sum()
subjects_with_zero = check_zero_x[check_zero_x == 0]
print(f"Number of Subjects with 0 for sherlock_left_eye_x: {len(subjects_with_zero)}")

check_zero_y = sherlock_ds2_left_eye_df.groupby('subjectID')['leftEyeY'].sum()
subjects_with_zero = check_zero_y[check_zero_y == 0]
print(f"Number of Subject with 0 for sherlock_left_eye_y: {len(subjects_with_zero)}")


########################### PRESENT RIGHT EYE ###########################
check_zero_x = present_ds2_right_eye_df.groupby('subjectID')['rightEyeX'].sum()
subjects_with_zero = check_zero_x[check_zero_x == 0]
print(f"Number of Subject with 0 for present_right_eye_x: {len(subjects_with_zero)}")

check_zero_y = present_ds2_right_eye_df.groupby('subjectID')['rightEyeY'].sum()
subjects_with_zero = check_zero_y[check_zero_y == 0]
print(f"Number of Subject with 0 for present_right_eye_y: {len(subjects_with_zero)}")

########################### PRESENT LEFT EYE ###########################
check_zero_x = present_ds2_left_eye_df.groupby('subjectID')['leftEyeX'].sum()
subjects_with_zero = check_zero_x[check_zero_x == 0]
print(f"Number of Subjects with 0 for present_left_eye_x: {len(subjects_with_zero)}")

check_zero_y = present_ds2_left_eye_df.groupby('subjectID')['leftEyeY'].sum()
subjects_with_zero = check_zero_y[check_zero_y == 0]
print(f"Number of Subject with 0 for present_left_eye_y: {len(subjects_with_zero)}")

