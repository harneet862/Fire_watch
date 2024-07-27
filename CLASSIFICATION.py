import json

def lambda_handler(event, context):
    responses = event['responses']
    
    # Define the questions and criteria for urgency
    urgent_criteria = {
        "location": ["safe", "immediate evacuation"],
        "fire_approach": ["yes"],
        "flames_smoke": ["yes"],
        "medical_conditions": ["yes"],
        "breathing_difficulties": ["yes"],
        "medications": ["no"],
        "transportation": ["no"],
        "safe_place": ["no"],
        "contact_emergency": ["no"],
        "communication": ["no"],
        "special_needs": ["yes"],
        "pets": ["yes"],
        "stress_level": [4, 5],
        "evacuating_help": ["no"],
        "suspicious_offers": ["yes"],
        "emergency_kit": ["no"]
    }
    
    urgent_responses = []
    non_urgent_responses = []
    
    for response in responses:
        urgency_level = "non-urgent"
        for question, answer in response.items():
            if question in urgent_criteria and answer in urgent_criteria[question]:
                urgency_level = "urgent"
                break
        
        if urgency_level == "urgent":
            urgent_responses.append(response)
        else:
            non_urgent_responses.append(response)
    
    return {
        'statusCode': 200,
        'urgent_responses': urgent_responses,
        'non_urgent_responses': non_urgent_responses
    }
