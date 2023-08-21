import os
#os.system('ls -l')

# # Download Experiment Infos
# os.system('aws s3 cp s3://natural-scenes-dataset/nsddata/experiments/nsd/nsd_expdesign.mat E:/NSD/nsddata/experiments')
# os.system('aws s3 cp s3://natural-scenes-dataset/nsddata/experiments/nsd/nsd_stim_info_merged.pkl E:/NSD/nsddata/experiments')
#
# # Download Stimuli
# os.system('aws s3 cp s3://natural-scenes-dataset/nsddata_stimuli/stimuli/nsd/nsd_stimuli.hdf5 E:/NSD/nsddata_stimuli/stimuli')

# Download Betas
# for sub in [1,2,5,7]:
#     for sess in range(1,38):
#         os.system('aws s3 cp s3://natural-scenes-dataset/nsddata_betas/ppdata/subj{:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/betas_session{:02d}.nii.gz E:/NSD/nsddata_betas/ppdata/subj{:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/betas_session{:02d}.nii.gz'.format(sub,sess,sub, sess))

# Download ROIs
for sub in [1,2,5,7]:
    os.system('aws s3 cp s3://natural-scenes-dataset/nsddata/ppdata/subj{:02d}/func1pt8mm/roi/ E:/NSD/nsddata/ppdata/subj{:02d}/func1pt8mm/roi/ --recursive'.format(sub,sub))
