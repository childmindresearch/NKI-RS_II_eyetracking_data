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

################################# The PRESENT DS1

all_dfs = []

for file_path in ds1_present_file_paths:
    with NWBHDF5IO(file_path, 'r') as io:
        nwbfile = io.read()
        present_keys = list(nwbfile.acquisition.keys())
        eyetrack_argus_key = next(key for key in present_keys if "Eyetrack_Argus" in key)
        # print(eyetrack_argus_key)

        container = nwbfile.acquisition[eyetrack_argus_key]
        container_key = next(iter(container.spatial_series.keys()))
        # print(container_key)

        ### Extract data (per NKI instructions)
        obj = nwbfile.acquisition[eyetrack_argus_key]
        cst = obj.spatial_series[container_key].data[:]
        times = obj.spatial_series[container_key].timestamps[:]
        # Description for cst data 
        headers = obj.spatial_series[container_key].description.split(',')

        ### Make dataframe 
        df = pd.DataFrame(cst)
        # Add timestamps 
        df['times'] = times
        # Add subjectID
        subject_id = file_path.split('/')[6]
        print("subjectID:", subject_id)
        df['subjectID'] = subject_id
        all_dfs.append(df)

present_ds1_df = pd.concat(all_dfs)
present_ds1_df.columns = ['x_corr_pixels', 'y_corr_pixels', 'times', 'subjectID']
print(present_ds1_df.head())
present_ds1_df.to_csv('/home/nburke/Documents/NKI-RS_II_eyetracking_data_outputs/present_ds1_df.csv')


################################# SHERLOCK DS1

all_dfs = []

for file_path in ds1_sherlock_file_paths:
    with NWBHDF5IO(file_path, 'r') as io:
        nwbfile = io.read()
        sherlock_keys = list(nwbfile.acquisition.keys())
        eyetrack_argus_key = next(key for key in sherlock_keys if "Eyetrack_Argus" in key)
        # print(eyetrack_argus_key)

        container = nwbfile.acquisition[eyetrack_argus_key]
        container_key = next(iter(container.spatial_series.keys()))
        # print(container_key)

        ### Extract data (per NKI instructions)
        obj = nwbfile.acquisition[eyetrack_argus_key]
        cst = obj.spatial_series[container_key].data[:]
        times = obj.spatial_series[container_key].timestamps[:]
        # Description for cst data 
        headers = obj.spatial_series[container_key].description.split(',')

        ### Make dataframe 
        df = pd.DataFrame(cst)
        # Add timestamps 
        df['times'] = times
        # Add subjectID
        subject_id = file_path.split('/')[6]
        print("subjectID:", subject_id)
        df['subjectID'] = subject_id
        all_dfs.append(df)

sherlock_ds1_df = pd.concat(all_dfs)
sherlock_ds1_df.columns = ['x_corr_pixels', 'y_corr_pixels', 'times', 'subjectID']
print(sherlock_ds1_df.head())
sherlock_ds1_df.to_csv('/home/nburke/Documents/NKI-RS_II_eyetracking_data_outputs/sherlock_ds1_df.csv')
