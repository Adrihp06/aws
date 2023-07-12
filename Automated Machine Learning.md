## Automated Machine Learning on AWS

We can use both SageMaker Autopilot and Comprehend to establish baseline model performance with very low effort and cost.
<p align="center">
  <img src="https://cevo.com.au/wp-content/uploads/2019/12/sagemaker-studio-autopilot-5.png" alt="awssagemaker" width="70%" />
</p>

### Amazon SageMaker Autopilot

[Amazon SageMaker](https://aws.amazon.com/sagemaker/) simplifies the model training and tuning process and speeds up the overall model development life cycle. By analyzing the data stored in S3, SageMaker Autopilot explores different algorithms and configurations based on many years of AI and machine learning experience at Amazon. The model candidates are summarized by SageMaker Autopilot through a set of automatically generated Jupyter notebooks and Python scripts.
The generated code includes data transformations, model training and model tuning.
SageMaker Autopilot also analyzes and balances the dataset and splits the dataset into train/validation sets.

The generated models are ranked by an objetive metric such as accuracy, AUC and F1-score.

Amazon SageMaker Autopilot is transparent,  we have have fully access to all the features.


Amazon Sage Maker Autopilot also enables model versioning and lineage tracking across all phases of the ML life cycle. A SageMaker Experiment consists of trials. A trial is a collection of steps that includes data preprocessing, model training, and model tuning.

### Train and Deploy with SageMaker Autopilot UI

The SageMaker Autopilot UI is integrated into SageMaker Studio, an IDE that provides a single, web-based visual interface where we can perform our ML development. The objective is to train a deploy a model to predict the star_rating for a given review_body with the Amazon Customer Reviews Dataset.

#### Step 1:
Download, preprocess and load the dataset into S3 buckets.

#### Step 2:
In the AWS Console navigate to Amazon SageMaker and click in SageMaker Studio, follow the instructins to set up SageMaker Studio and click in Open Studio.

#### Step 3:
Now in the SageMaker Studio UI (AutoML), we create and configure an experiment.
We are going to use a subset of the Amazon Customer Reviews Dataset to train the model. We also need to configure some parameters: 

**Experiment and data details:**
- Experiment name
- Input data location
- Output data location
  
**Target and features:**
- Target column: star_rating
- Sample_weight: None
- Features: All
  
**Training methods:**
- Training method and algorithms: Auto
  
**Deplotment settings:**
- Auto_deploy: No
- Run complete experiment

#### Step 4:
The experiment is running and the models are being training. Once SageMaker Autopilot completes the candidate generation phase, we will see the links to the generated notebooks: Candidate Generation and Data Exploration.

#### Step 5:
Now is time to deploy the model, select the model and type the AWS instance type and the endpoint name, to do the inference run the script inference.py
