import random 

def evaluate_accuracy(text):
    # Simulate factual accuracy score between 0.6 and 1.0
    return round(random.uniform(0.6, 1.0), 2)

def evaluate_relevance(prompt, response):
    # Simulate relevance score based on prompt/response similarity
    return round(random.uniform(0.6, 1.0), 2)

def evaluate_coherence(text):
    # Simulate coherence using text fluency rules
    return round(random.uniform(0.7, 1.0), 2)