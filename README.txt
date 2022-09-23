README.txt
 

       TABLE OF CONTENTS
       
(1) python-ws.py - Python module that listens to the endpoint and receives the initial requests, converting the JSON data into DataFrame format and passing it to the processing module. Eventually, it receives the results from the processing module and passes it back to the API client.

(2) myprocessor.py - Receives the data and performs the operation requested on the set of rational numbers provided.

(3) Dockerfile - Dockerfile to define the container that will hold the web service


    ABOUT THE PROJECT
    This is a RESTful web service built to add, subtract, multiply, and divide up to five rational numbers. Per the clarification provided, the service can only perform one operation at a time and the operation works with the numbers in the order they are provided. 


BUILT WITH
   (1) Python - Programming Language
      (1a) CherryPy  -  Python Lib
      (1b) pandas  -  Python Lib
      (1c) json  -  Python Lib
   (2) Docker - Container Service
   (3) ngrok - Reverse Proxy Service


   USAGE DIRECTIONS FOR CLIENT
   When the server is set up, it is automatically set to run on the machines localhost IP address and port 4102. The port number can be changed by altering the settings in the source code/commands (see install.txt for more on this). The reverse proxy service ngrok is then used to tunnel this IP address and port number to a publicly available domain name. Due to the limited capabilities of the free version for most reverse proxy services, the aforementioned domain name will change whenever the ngrok session for the web service is restarted (see Disclaimer section for more on this). As a result, after ensuring that ngrok is running on the correct port, you must also ensure that you have the correct domain name for the current session. Once you have this, all you'll need to do is add '/process' to the end and you'll have your REST API Endpoint which should look something like this:

    'https://2ace-2600-1702-1650-1020-4d06-f831-ee7e-f7fd.ngrok.io/process'. 

    From there, this endpoint will accept a POST request and the POST data. The POST data is given in JSON form and follows the specifications given below. The endpoint does not need any custom headers, although the standard "Content-type: application/json" should be given if it is not already in order to ensure the correct format.


   INPUT FORMAT
   The input should be in JSON format and contain the following three keys:
   
(1) "nums"   - A list of up to 5 rational numbers. These numbers can be any combination of integers, decimals and fractions and can be passed interchangeably. The integers and decimals provided can also be formatted interchangeably as either a number or string, while the fractions must be provided as a string.

(2) "action" - The operation to be performed on the set of numbers. Per the instructions provided, the service can only perform one operation at a time and the operation will work with the numbers in the order provided. The operations that can be performed and their corresponding accepted input values are as follows:
                       Operation: Addition       | Input Value: 'A'
                       Operation: Subtraction    | Input Value: 'S'
                       Operation: Multiplication | Input Value: 'M'
                       Operation: Division       | Input Value: 'D'
		       
(3) "return_format" - Determines how the result will be formatted when returned to the client. There are two accepted formats for the returned result: pretty formatting and literal formatting. Pretty formatting emphasizes readabiility so you can get a clearer picture of what's being returned. Literal formatting emphasizes interoperability by maintaining escape characters so the result can be directly interpreted more reliably by other applications. The two accepted input values are as follows:
                               Input Value: 'pretty'    - Pretty formatting
                               Input Value: 'literal'   - Literal formatting

Altogether, the JSON input with the aforementioned three keys should look something like the following:
         {
               "nums"            :     [n1...] , 
               "action"          :     "M",
               "return_format"   :     "pretty"
         }


    EXAMPLES
     Example 1: Multiplication with interchangeable string and number formatted integers, fractions and decimals.
      Input:
        {
               "nums"            :     ["3", 20, "1/3", 0.5] , 
               "action"          :     "M",
               "return_format"   :     "pretty"
        }
      Output:
        {
               "Result": 10
        }

    Example 2: Math operation failed due to division by zero.
      Input:
        {
               "nums"            :     ["3", 0, "1/3", 0.5] , 
               "action"          :     "M",
               "return_format"   :     "pretty"
        }
      Output:
        {
              "Error": {
                        "args": [
                                 "float division by zero"
                                ]
                        }
        }



DISCLAIMER
   There were a lot of assumptions that were made as to what the project was looking for, although I've also inferred that this was part of the point as the prompt was only one sentence long with no input examples and when asked for further clarification I was really only given "We expect the service to perform one operation at a time. The operation should work with the numbers in the order provided." Given this I was able to surmise that the web service should accept one operation and perform it on the numbers in the order provided. The main thing here that tipped me off was that the second sentence of the clarification said "'the operation' (singular) should work with 'the numbers' (plural) in the order the where provided". 

   The decision to host the web service through a reverse proxy service from my local machine was made due to most of the major cloud providers requiring some kind of payment to store an application on their servers and host it on the internet. Similarly, in order to re-use an ngrok domain name between sessions you must purchase a plan or keep it running in the background on a dedicated server, which I would have to purchase. With the minimal information provided, I assumed you didn't want me to purchase anything out of my own pocket as that would be quite innapropriate to ask of a prospective candidate as part of the interview.
