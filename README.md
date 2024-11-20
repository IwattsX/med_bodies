# How to run the training/predictions
1) Create a conda environment
```
conda env create -f environment.yml
```
2) Change directory into Scripts
```
cd Scripts/
```
3) Training/Prediction

This will train from the csv inside of the dataset csv files
```
python trainModel.py --input dataset/voltageDataset.csv --output dataset/datasetTrainSigData.csv --model_path data/model1.pth
```

This will do an evaluation by loading the model and placing it in evaluation mode
```
python3 predictModel.py
```

# Medical Bodies
Taking in circular meshes (medical bodies), getting voltage data from the electrodes, and simulating the medical body back using AI/ML techniques with the voltages. 

- **NOTE** : Use ```help func``` to display documentation

# Plot the circle mesh (course)
figure;pdemesh(p, e, t)

# Plot the circle mesh (fine)
figure;pdemesh(p1, e1, t1)

change
