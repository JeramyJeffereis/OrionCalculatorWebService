import cherrypy
import pandas as pd
import calculator
import json
c = calculator.Calculator()

class CalculatorWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()

   ## self.process() - Receives JSON data from request and converts to DataFrame. Passes calculator module
   ##   said DataFrame and formats the results before returning it to the client. User specifies in request whether
   ##   result should formatted as 'literal' with escape chars or 'pretty' without them. Defaults to pretty if none given. 
   def process(self):
      
      ## Receives JSON request and save it into variable
      data = cherrypy.request.json

      ## Attempts to convert JSON to DataFrame and notifies client if that fails
      try:
          df = pd.DataFrame(data)
      except Exception as e:
          return self.error(pd.DataFrame({'Error': [e]}))

      ## Checks to ensure a return_format has been provided  
      if 'return_format' in df.columns:
          ret_form = df['return_format'][0]
      else:
          return self.error(pd.DataFrame({'Missing JSON attributes': ["It looks like you forgot to include the 'return_format' attribute. This attribute specifies how the result will be formatted. "]}))

      ## Calls the calculator module and retrieves the results                    
      output = c.calculate(df)
      result = output.to_json(orient="records",lines=True)
      parsed = json.loads(result)

      ## Applies the specified return_format and notifies the client if they
      ##    supplied an incorrect return_format
      if ret_form == 'literal':
          return json.dumps(parsed, indent=4, separators=(',',':'))
      elif ret_form == 'pretty':
          return parsed
      else:
          return self.error(pd.DataFrame({"Request Failed":  ["It looks like you entered '{}' as the return_type. This field can only accept 'literal' or 'pretty' as it's value".format(ret_form)]}))
                
   ## self.error(err) - Handles errors by formatting exception information and returning it to the client
   ##       to notify them of why the request/operation failed.      
   def error(self, err):
       result = err.to_json(orient="records",lines=True)
       return json.loads(result)  

##  Top-level code that starts the webservice
if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0', 'server.socket_port':4102}
   cherrypy.config.update(config)
   cherrypy.quickstart(CalculatorWebService())

   
