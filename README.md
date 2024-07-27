Wildfire Evacuation Assistance Lambda Functions
This repository contains two AWS Lambda functions designed to assist in wildfire evacuation efforts. The functions categorize responses based on urgency and interact with AWS services like S3 and Bedrock for processing queries.

Function 1: Query Handling and Bedrock Integration
This function uploads a query to an S3 bucket and processes it using AWS Bedrock.

Function 2: Categorizing Responses by Urgency
This function categorizes responses based on urgency, distinguishing between urgent and non-urgent needs during wildfire evacuations.

FUTURE PLANS:
We plan to integrate generative AI to assess the probability of the correctness of news or information. This feature will enhance the reliability of information shared during wildfire evacuations by reducing misinformation and providing users with validated updates.
