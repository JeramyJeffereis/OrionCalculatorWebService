from python:3.6.4-slim-jessie
RUN pip install pandas
RUN pip install CherryPy
COPY calculator.py .
COPY calculator_ws.py .
EXPOSE 4102
ENTRYPOINT ["python", "calculator_ws.py"]