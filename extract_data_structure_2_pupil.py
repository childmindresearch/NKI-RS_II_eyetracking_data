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
all_dfs_pupil_diameter = []

for file_path in ds2_present_file_paths:
    # print("*****************")
    with NWBHDF5IO(file_path, 'r') as io:
        nwbfile = io.read()
        present_keys = list(nwbfile.acquisition.keys())
        ###############  PUPIL DIAMETER  ###############
        # keys and containers 
        pupil_diameter_key = next(key for key in present_keys if 'Pupil_Diameters_EL' in key)
        print("pupil diamter key:", pupil_diameter_key)
        # Data Array 
        cst_pupil = nwbfile.acquisition[pupil_diameter_key].data[:]
        # Timestamps for each datapoint
        times_pupil = nwbfile.acquisition[pupil_diameter_key].timestamps[:]
        # Description for cst data holds all headers 
        headers_pupil = nwbfile.acquisition[pupil_diameter_key].description.split(',')
        print("HEADERS:", headers_pupil)
       
        ### Make dataframe 
        df_pupil_diameter = pd.DataFrame(cst_pupil, columns=headers_pupil)
        # Add timestamps 
        df_pupil_diameter['times'] = times_pupil
        # Add subjectID 
        # print("checking file_path:", file_path)
        subject_id = file_path.split('/')[6]
        print("subjectID:", subject_id)
        df_pupil_diameter['subjectID'] = subject_id 
        # Add to all_dfs 
        all_dfs_pupil_diameter.append(df_pupil_diameter)


present_ds2_pupil_diamter = pd.concat(all_dfs_pupil_diameter)
print(present_ds2_pupil_diamter.head())
present_ds2_pupil_diamter.to_csv("/home/nburke/Documents/NKI-RS_II_eyetracking_data_outputs/present_ds2_pupil.csv")
# print("Number of subjects in PRESENT DS2:", len(present_ds2_pupil_diamter['subjectID'].unique()))
# print(f"PRESENT: mean_x = {present_ds2_pupil_diamter['leftEyeX'].mean()}, min_x = {present_ds2_pupil_diamter['leftEyeX'].min()}, max_x = {present_ds2_pupil_diamter['leftEyeX'].max()}")

###################### SHERLOCK: data_structure_2
all_dfs_pupil_diameter = []

for file_path in ds2_sherlock_file_paths:
    # print("*****************")
    with NWBHDF5IO(file_path, 'r') as io:
        nwbfile = io.read()
        sherlock_keys = list(nwbfile.acquisition.keys())
        ###############  PUPIL DIAMETER  ###############
        # keys and containers 
        pupil_diameter_key = next(key for key in sherlock_keys if 'Pupil_Diameters_EL' in key)
        print("pupil diamter key:", pupil_diameter_key)
        # Data Array 
        cst_pupil = nwbfile.acquisition[pupil_diameter_key].data[:]
        # Timestamps for each datapoint
        times_pupil = nwbfile.acquisition[pupil_diameter_key].timestamps[:]
        # Description for cst data holds all headers 
        headers_pupil = nwbfile.acquisition[pupil_diameter_key].description.split(',')
        print("HEADERS:", headers_pupil)
       
        ### Make dataframe 
        df_pupil_diameter = pd.DataFrame(cst_pupil, columns=headers_pupil)
        # Add timestamps 
        df_pupil_diameter['times'] = times_pupil
        # Add subjectID 
        # print("checking file_path:", file_path)
        subject_id = file_path.split('/')[6]
        print("subjectID:", subject_id)
        df_pupil_diameter['subjectID'] = subject_id 
        # Add to all_dfs 
        all_dfs_pupil_diameter.append(df_pupil_diameter)


present_ds2_pupil_diamter = pd.concat(all_dfs_pupil_diameter)
print(present_ds2_pupil_diamter.head())
present_ds2_pupil_diamter.to_csv("/home/nburke/Documents/NKI-RS_II_eyetracking_data_outputs/sherlock_ds2_pupil.csv")
# print("Number of subjects in PRESENT DS2:", len(present_ds2_pupil_diamter['subjectID'].unique()))
# print(f"PRESENT: mean_x = {present_ds2_pupil_diamter['leftEyeX'].mean()}, min_x = {present_ds2_pupil_diamter['leftEyeX'].min()}, max_x = {present_ds2_pupil_diamter['leftEyeX'].max()}")
