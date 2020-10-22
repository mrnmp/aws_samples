import boto3
#create the resoruce 
sqs = boto3.resource('sqs')
#create the queue
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
