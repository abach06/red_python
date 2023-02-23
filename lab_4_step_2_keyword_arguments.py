"""
keyword arguments

"""
#import boto3

#def translate_text(text, source_language_code, target_language_code): 
 #   client = boto3.client('translate')
 #   response = client.translate_text(
 #       Text=text, 
 #       SourceLanguageCode=source_language_code, 
 #       TargetLanguageCode=target_language_code
 #   )
 #   print(response) 

#def main():
 #   translate_text('I am learning to code in AWS','en','fr')

#if __name__=="__main__":
 #   main()

#A keyword argument is a name-value pair that is passed to the function.

#import boto3

#def translate_text(**kwargs): 
 #   client = boto3.client('translate')
 #   response = client.translate_text(**kwargs)
 #   print(response) 

#def main():
 #   translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

#if __name__=="__main__":
 #   main()
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

#Python used the key\:value pairs defined in the dictionary in place of the keyword arguments