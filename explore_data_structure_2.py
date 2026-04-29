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

##############################################################################################
########################### # SUBJECTS PER DF ##############################################
#############################################################################################
n_subj_present_right_eye = len(present_ds2_right_eye_df['subjectID'])
n_subj_present_left_eye = len(present_ds2_left_eye_df['subjectID'])
n_subj_sherlock_right_eye = len(present_ds2_right_eye_df['subjectID'])
n_subj_sherlock_left_eye = len(present_ds2_left_eye_df['subjectID'])
print(f"Number of subjects present_right_eye: {n_subj_present_right_eye}")
print(f"Number of subjects present_left_eye: {n_subj_present_left_eye}")
print(f"Number of subjects sherlock_right_eye: {n_subj_sherlock_right_eye}")
print(f"Number of subjects sherlock_left_eye: {n_subj_sherlock_left_eye}")

##############################################################################################
########################### # SUBJECTS WITH MISSING DATA IN COLUMN ###########################
#############################################################################################

# ########################### sherlock right eye 
# check_zero_x = sherlock_ds2_right_eye_df.groupby('subjectID')['rightEyeX'].sum()
# subjects_with_zero = check_zero_x[check_zero_x == 0]
# print(f"Number of Subject with 0 for sherlock_right_eye_x: {len(subjects_with_zero)}")

# check_zero_y = sherlock_ds2_right_eye_df.groupby('subjectID')['rightEyeY'].sum()
# subjects_with_zero = check_zero_y[check_zero_y == 0]
# print(f"Number of Subject with 0 for sherlock_right_eye_y: {len(subjects_with_zero)}")

# ########################### sherlock left eye 
# check_zero_x = sherlock_ds2_left_eye_df.groupby('subjectID')['leftEyeX'].sum()
# subjects_with_zero = check_zero_x[check_zero_x == 0]
# print(f"Number of Subjects with 0 for sherlock_left_eye_x: {len(subjects_with_zero)}")

# check_zero_y = sherlock_ds2_left_eye_df.groupby('subjectID')['leftEyeY'].sum()
# subjects_with_zero = check_zero_y[check_zero_y == 0]
# print(f"Number of Subject with 0 for sherlock_left_eye_y: {len(subjects_with_zero)}")

# ########################### present right eye
# check_zero_x = present_ds2_right_eye_df.groupby('subjectID')['rightEyeX'].sum()
# subjects_with_zero = check_zero_x[check_zero_x == 0]
# print(f"Number of Subject with 0 for present_right_eye_x: {len(subjects_with_zero)}")

# check_zero_y = present_ds2_right_eye_df.groupby('subjectID')['rightEyeY'].sum()
# subjects_with_zero = check_zero_y[check_zero_y == 0]
# print(f"Number of Subject with 0 for present_right_eye_y: {len(subjects_with_zero)}")

# ########################### present left eye

# check_zero_x = present_ds2_left_eye_df.groupby('subjectID')['leftEyeX'].sum()
# subjects_with_zero = check_zero_x[check_zero_x == 0]
# print(f"Number of Subjects with 0 for present_left_eye_x: {len(subjects_with_zero)}")

# check_zero_y = present_ds2_left_eye_df.groupby('subjectID')['leftEyeY'].sum()
# subjects_with_zero = check_zero_y[check_zero_y == 0]
# print(f"Number of Subject with 0 for present_left_eye_y: {len(subjects_with_zero)}")

### OUTPUT 
    # Number of Subject with 0 for sherlock_right_eye_x: 2
    # Number of Subject with 0 for sherlock_right_eye_y: 2
    # Number of Subjects with 0 for sherlock_left_eye_x: 113
    # Number of Subject with 0 for sherlock_left_eye_y: 113
    # Number of Subject with 0 for present_right_eye_x: 2
    # Number of Subject with 0 for present_right_eye_y: 2
    # Number of Subjects with 0 for present_left_eye_x: 113
    # Number of Subject with 0 for present_left_eye_y: 113

num_zero_sherlock_right_eye_x = 2 
num_zero_sherlock_right_eye_y = 2
num_zero_sherlock_left_eye_x = 113
num_zero_sherlock_left_eye_y = 113
num_zero_present_right_eye_x = 2 
num_zero_present_right_eye_y = 2
num_zero_present_left_eye_x = 113
num_zero_present_left_eye_y = 113

### PRECENT MISSING
pct_missing_sherlock_right_eye_x = num_zero_sherlock_right_eye_x/n_subj_sherlock_right_eye
pct_missing_sherlock_right_eye_y = num_zero_sherlock_right_eye_y/n_subj_sherlock_right_eye

pct_missing_sherlock_left_eye_x = num_zero_sherlock_left_eye_x/n_subj_sherlock_left_eye
pct_missing_sherlock_left_eye_y = num_zero_sherlock_left_eye_y/n_subj_sherlock_left_eye

pct_missing_present_right_eye_x = num_zero_present_right_eye_x/n_subj_present_right_eye
pct_missing_present_right_eye_y = num_zero_present_right_eye_y/n_subj_present_right_eye

pct_missing_present_left_eye_x = num_zero_present_left_eye_x/n_subj_present_left_eye
pct_missing_present_left_eye_y = num_zero_present_left_eye_y/n_subj_present_left_eye

print(f"pct_missing SHERLOCK RIGHT EYE X : {pct_missing_sherlock_right_eye_x}")
print(f"pct_missing SHERLOCK RIGHT EYE Y : {pct_missing_sherlock_right_eye_y}")
print(f"pct_missing SHERLOCK LEFT EYE X : {pct_missing_sherlock_left_eye_x}")
print(f"pct_missing SHERLOCK LEFT EYE Y : {pct_missing_sherlock_left_eye_y}")
print("*"*50)
print(f"pct_missing PRESENT RIGHT EYE X : {pct_missing_present_right_eye_x}")
print(f"pct_missing PRESENT RIGHT EYE Y : {pct_missing_present_right_eye_y}")
print(f"pct_missing PRESENT LEFT EYE X : {pct_missing_present_left_eye_x}")
print(f"pct_missing PRESENT LEFT EYE Y : {pct_missing_present_left_eye_y}")