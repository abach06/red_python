"""
Arguments

"""
#import boto3

#def translate_text():
   # client = boto3.client('translate')
   # response = client.translate_text(
   #     Text='I am learning to code in AWS', 
#        SourceLanguageCode='en', 
 #       TargetLanguageCode='fr' 
 #   )
 #   print(response) 

#def main():
 #   translate_text()

#if __name__=="__main__":
 #   main()

import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('This is fun','en','ja') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()
