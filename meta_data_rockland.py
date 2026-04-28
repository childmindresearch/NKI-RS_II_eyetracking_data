#### to read data off amazon s3 bucket 
import os 
import json 
from pynwb import NWBHDF5IO
import pandas as pd 
print("Import worked")

# set directory on lisa 
directory = '/data3/cdb/MOBI_LAB/NKI_RS2/ET_DATA'
os.chdir(directory)
print("DIRECTORY:", os.getcwd())

# List all subject folders 
subject_folders = os.listdir(directory)
print("Number of Subjects:", len(subject_folders))

passive_sherlock_files = []
passive_present_files = []

# Read in files and get file paths 
for subject in subject_folders:
    new_path = os.path.join(directory, subject, "ses-MOBI1A")

    if os.path.exists(new_path):
        # print(f"file path for {subject} exisits")
        files = os.listdir(new_path)

        for file in files:
            if file.endswith(".nwb") and "passivesherlock" in file:
                passive_sherlock_files.append(os.path.join(new_path, file))
                # print(subject, "adding file")
            
            if file.endswith(".nwb") and "passivepresent" in file:
                passive_present_files.append(os.path.join(new_path, file))
                # print(subject, "adding file")



###################### Separate by data_structure type 

ds1_sherlock_file_paths = []
ds2_sherlock_file_paths = []

ds1_present_file_paths = []
ds2_present_file_paths = []

#### sherlock 
for i in passive_sherlock_files:
      with NWBHDF5IO(i, 'r') as io:
            nwbfile = io.read()
            file_keys = list(nwbfile.acquisition.keys())
            # print(file_keys)

            if any("Eyetrack_Argus" in key for key in file_keys):
                  ds1_sherlock_file_paths.append(i)
            
            if any("Left_eye_gaze" in key for key in file_keys):
                  ds2_sherlock_file_paths.append(i)
print("length of ds1 SHERLOCK:", len(ds1_sherlock_file_paths))
print("length of ds2 SHERLOCK :", len(ds2_sherlock_file_paths))

#### passive 
for i in passive_present_files:
      with NWBHDF5IO(i, 'r') as io:
            nwbfile = io.read()
            file_keys = list(nwbfile.acquisition.keys())
            # print(file_keys)

            if any("Eyetrack_Argus" in key for key in file_keys):
                  ds1_present_file_paths.append(i)
            
            if any("Left_eye_gaze" in key for key in file_keys):
                  ds2_present_file_paths.append(i)
print("length of ds1 PASSIVE:", len(ds1_present_file_paths))
print("length of ds2 PASSIVE:", len(ds2_present_file_paths))




###################### The PRESENT: data_structure_2
all_dfs_left_eye = []
all_dfs_right_eye = []

for file_path in ds2_present_file_paths:
    # print("*****************")
    with NWBHDF5IO(file_path, 'r') as io:
        nwbfile = io.read()
        present_keys = list(nwbfile.acquisition.keys())
        ###############  LEFT EYE ###############
        # keys and containers 
        left_eye_gaze_key = next(key for key in present_keys if "Left_eye_gaze" in key)
        # print(left_eye_gaze_key)
        container_left_eye = nwbfile.acquisition[left_eye_gaze_key]
        container_left_eye_key = next(iter(container_left_eye.spatial_series.keys()))
        # print(container_left_eye_key)
        
        ### Extract data (per NKI instructions)
        obj_left_eye = nwbfile.acquisition[left_eye_gaze_key]
        cst_left_eye = obj_left_eye.spatial_series[container_left_eye_key].data[:]
        times_left_eye = obj_left_eye.spatial_series[container_left_eye_key].timestamps
        # Description for cst data 
        headers_left_eye = obj_left_eye.spatial_series[container_left_eye_key].description.split(',')

        ### Make dataframe 
        df_left_eye = pd.DataFrame(cst_left_eye, columns=headers_left_eye)
        # Add timestamps 
        df_left_eye['times'] = times_left_eye
        # Add subjectID 
        print("checking file_path:", file_path)
        subject_id = file_path.split('/')[10]
        df_left_eye['subjectID'] = subject_id 
        # Add to all_dfs 
        all_dfs_left_eye.append(df_left_eye)

        # ###############  RIGHT EYE ###############
        # # keys and containers 
        # right_eye_gaze_key = next(key for key in present_keys if "Right_eye_gaze" in key)
        # container_right_eye = nwbfile.acquisition[right_eye_gaze_key]
        # container_right_eye_key = next(iter(container_right_eye.spatial_series.keys()))
        # # print(container_right_eye_key)
        
        # ### Extract data (per NKI instructions)
        # obj_right_eye = nwbfile.acquisition[right_eye_gaze_key]
        # cst_right_eye = obj_right_eye.spatial_series[container_right_eye_key].data[:]
        # times_right_eye = obj_right_eye.spatial_series[container_right_eye_key].timestamps
        # # Description for cst data 
        # headers_right_eye = obj_right_eye.spatial_series[container_right_eye_key].description.split(',')

        # ### Make dataframe 
        # df_right_eye = pd.DataFrame(cst_right_eye, columns=headers_right_eye)
        # # Add timestamps 
        # df_right_eye['times'] = times_right_eye
        # # Add subjectID 
        # subject_id = file_path.split('/')[10]
        # df_right_eye['subjectID'] = subject_id 
        # # Add to all_dfs 
        # all_dfs_right_eye.append(df_right_eye)

present_ds2_left_eye_df = pd.concat(all_dfs_left_eye)
print(present_ds2_left_eye_df.head())
print("Number of subjects in PRESENT DS2:", len(present_ds2_left_eye_df['subjectID'].unique()))
print(f"PRESENT: mean_x = {present_ds2_left_eye_df['leftEyeX'].mean()}, min_x = {present_ds2_left_eye_df['leftEyeX'].min()}, max_x = {present_ds2_left_eye_df['leftEyeX'].max()}")
# present_ds2_right_eye_df = pd.concat(all_dfs_right_eye)
# print(present_ds2_right_eye_df.head())
# print(present_ds2_right_eye_df['subjectID'].unique())
# print("Number of subjects:", len(present_ds2_right_eye_df['subjectID'].unique()))


###################### The SHERLOCK: data_structure_2
all_dfs_left_eye = []
all_dfs_right_eye = []

for file_path in ds2_sherlock_file_paths:
    # print("*****************")
    with NWBHDF5IO(file_path, 'r') as io:
        nwbfile = io.read()
        present_keys = list(nwbfile.acquisition.keys())
        ###############  LEFT EYE ###############
        # keys and containers 
        left_eye_gaze_key = next(key for key in present_keys if "Left_eye_gaze" in key)
        # print(left_eye_gaze_key)
        container_left_eye = nwbfile.acquisition[left_eye_gaze_key]
        container_left_eye_key = next(iter(container_left_eye.spatial_series.keys()))
        # print(container_left_eye_key)
        
        ### Extract data (per NKI instructions)
        obj_left_eye = nwbfile.acquisition[left_eye_gaze_key]
        cst_left_eye = obj_left_eye.spatial_series[container_left_eye_key].data[:]
        times_left_eye = obj_left_eye.spatial_series[container_left_eye_key].timestamps
        # Description for cst data 
        headers_left_eye = obj_left_eye.spatial_series[container_left_eye_key].description.split(',')

        ### Make dataframe 
        df_left_eye = pd.DataFrame(cst_left_eye, columns=headers_left_eye)
        # Add timestamps 
        df_left_eye['times'] = times_left_eye
        # Add subjectID 
        subject_id = file_path.split('/')[10]
        df_left_eye['subjectID'] = subject_id 
        # Add to all_dfs 
        all_dfs_left_eye.append(df_left_eye)

        # ###############  RIGHT EYE ###############
        # # keys and containers 
        # right_eye_gaze_key = next(key for key in present_keys if "Right_eye_gaze" in key)
        # container_right_eye = nwbfile.acquisition[right_eye_gaze_key]
        # container_right_eye_key = next(iter(container_right_eye.spatial_series.keys()))
        # # print(container_right_eye_key)
        
        # ### Extract data (per NKI instructions)
        # obj_right_eye = nwbfile.acquisition[right_eye_gaze_key]
        # cst_right_eye = obj_right_eye.spatial_series[container_right_eye_key].data[:]
        # times_right_eye = obj_right_eye.spatial_series[container_right_eye_key].timestamps
        # # Description for cst data 
        # headers_right_eye = obj_right_eye.spatial_series[container_right_eye_key].description.split(',')

        # ### Make dataframe 
        # df_right_eye = pd.DataFrame(cst_right_eye, columns=headers_right_eye)
        # # Add timestamps 
        # df_right_eye['times'] = times_right_eye
        # # Add subjectID 
        # subject_id = file_path.split('/')[10]
        # df_right_eye['subjectID'] = subject_id 
        # # Add to all_dfs 
        # all_dfs_right_eye.append(df_right_eye)

sherlock_ds2_left_eye_df = pd.concat(all_dfs_left_eye)
print(sherlock_ds2_left_eye_df.head())
print("Number of subjects in SHERLOCK DS2:", len(sherlock_ds2_left_eye_df['subjectID'].unique()))
print(f"SHERLOCK: mean_x = {sherlock_ds2_left_eye_df['leftEyeX'].mean()}, min_x = {sherlock_ds2_left_eye_df['leftEyeX'].min()}, max_x = {sherlock_ds2_left_eye_df['leftEyeX'].max()}")
# sherlock_ds2_right_eye_df = pd.concat(all_dfs_right_eye)
# print(sherlock_ds2_right_eye_df.head())
# print(sherlock_ds2_right_eye_df['subjectID'].unique())
# print("Number of Subjects:", len(sherlock_ds2_right_eye_df['subjectID'].unique()))