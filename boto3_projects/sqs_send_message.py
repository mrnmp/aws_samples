import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
##queue = sqs.get_queue_by_name(QueueName='test')

# Create two  new messages, 2 message with attribute

response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))
