"""
Minimal Bedrock Inference Example

This example demonstrates basic invocation of Amazon Bedrock models.
It is designed for learning purposes, not production use.

Concepts demonstrated:
- Bedrock client initialization
- Model invocation
- Response parsing

Production considerations (not included here):
- Error handling (try/except blocks)
- Input validation
- Cost monitoring
- Security (IAM roles, VPC endpoints)
- Retry logic with exponential backoff
"""

import boto3
import json


def invoke_bedrock_model(prompt: str, model_id: str = 'anthropic.claude-v2') -> str:
    """
    Invoke a Bedrock model with a simple prompt.
    
    Args:
        prompt: The input prompt for the model
        model_id: The Bedrock model ID to use
        
    Returns:
        The model's completion text
        
    Note: This is a minimal example. In production, add:
    - Comprehensive error handling
    - Input validation and sanitization
    - Cost tracking and limits
    - Security controls (IAM, VPC)
    - Retry logic for transient failures
    """
    # Initialize Bedrock runtime client
    # Note: Ensure your AWS credentials are configured
    # Region must support Bedrock (e.g., us-east-1, us-west-2)
    bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
    
    # Prepare request body
    # Format depends on model family (Claude, Llama, etc.)
    body = json.dumps({
        'prompt': prompt,
        'max_tokens_to_sample': 100,
        'temperature': 0.7,
        'top_p': 0.9
    })
    
    # Invoke the model
    # In production, wrap this in try/except for error handling
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType='application/json',
        accept='application/json',
        body=body
    )
    
    # Parse response
    response_body = json.loads(response['body'].read())
    
    # Extract completion text
    # Response format varies by model family
    completion = response_body.get('completion', '')
    
    return completion


if __name__ == '__main__':
    # Example usage
    prompt = 'Explain what Amazon Bedrock is in one sentence.'
    
    print(f"Prompt: {prompt}\n")
    print("Invoking Bedrock model...\n")
    
    try:
        result = invoke_bedrock_model(prompt)
        print(f"Response: {result}")
    except Exception as e:
        print(f"Error: {e}")
        print("\nCommon issues:")
        print("- Bedrock not enabled in your region")
        print("- Missing IAM permissions")
        print("- Invalid model ID")
        print("- Network connectivity issues")

