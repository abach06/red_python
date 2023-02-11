#Create an empty list of aws services
aws_services_list = []
print(aws_services_list)

#populate list
aws_services_list.append('S3')
aws_services_list.append('Lambda')
aws_services_list.append('EC2')
aws_services_list.append('CloudFormation')
aws_services_list.append('ECS')
aws_services_list.append('IAM')
aws_services_list.append('CloudWatch')
aws_services_list.append('VPC')
aws_services_list.append('DynamoDB')
aws_services_list.append('Cognito')
aws_services_list.append('KMS')

#print the list
print(aws_services_list)

#print the length of the list
print("Length of aws_services_list is", len(aws_services_list))

#Remove two specific services from the list by name or by index.
del aws_services_list[0]
del aws_services_list[7]

#print updated list
print(aws_services_list)

#print the length of the updated list
print("Length of aws_services_list is", len(aws_services_list))
