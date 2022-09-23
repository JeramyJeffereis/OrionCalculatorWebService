import pandas as pd
class Calculator:

    ## self.calculate(df) - Accepts as it's input DataFrame with converted JSON request data
    ##        containing an operation (A, S, D or M) and up to five rational numbers which can be
    ##        represented as integers, decimals or fractions. The service can only perform one
    ##        operation at a time and the operation is performed on the numbers in the order they 
    ##        are provided (per project specifications).
    def calculate(self, df):
        
        ## Checks to ensure an action has been provided
        if 'action' in df.columns:
            op = df['action'][0]
        else:
            return pd.DataFrame({'Missing JSON attributes': ["It looks like you forgot to include the 'action' attribute. This attribute specifies the operation and it's value can either be A, S, D, or M"]})

        ## Checks to ensure a set of numbers has been provided    
        if 'nums' in df.columns:
            nums = df['nums']
        else:
            return pd.DataFrame({'Missing JSON attributes': ["It looks like you forgot to include the 'nums' attribute. This attribute specifies a list of up to 5 rational numbers which can be integers, decimals or fractions. Integers and decimals can be formatted as either a number or a string however a fraction must be the latter"]})            

        ## Performs the given operation on the given set of numbers    
        sm = 0
        for i in range(0, len(nums)):                
            try:
                
                ## Checks to see if a given number is a fraction and converts it to decimal form
                if type(nums[i])==str and '/' in nums[i]:
                    ind = nums[i].index('/')
                    numer = float(nums[i][:ind])
                    denom = float(nums[i][ind+1:])
                    tmp = numer/denom
                else:
                    tmp = float(nums[i])
                    
                ## Initializes sm on the first run. This is so we can handle a fraction that is provided
                ##     As the first argument
                if i == 0:
                    sm += tmp
                    continue
                
                ## Performs the given operation with the current number in the set
                if op == 'A':
                    sm += tmp
                elif op == 'S':
                    sm -= tmp
                elif op == 'M':
                    sm *= tmp
                elif op == 'D':
                    sm /= tmp
                else:
                    
                    ## Catches when the user has submitted an unnaccepted operation and notifies them
                    if len(op) > 1:
                         err = "This service can only perform one operation at a time"
                    elif len(op) < 1:
                         err = "This service must be given an operation to perform"
                    else:
                        err = "This service only accepts the following input values and operations: 'A' - Add, 'S' - Subtract, 'D' - Divide and 'M' - Multiply."
                    return pd.DataFrame({'Operation Error': ["It looks like you've entered '{}' as the operation. {}".format(op,err)]})

            ## Catches any errors related to the math or type conversion and returns information on the specific
            ##     exception to the user.        
            except Exception as e:
                    return pd.DataFrame({'Error': [e]})
                
        return pd.DataFrame({'Result': [sm]})
        
    
