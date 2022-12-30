# 
FROM python:3.9

# 
WORKDIR /

# 
COPY requirements.txt ./

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .

# 
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
