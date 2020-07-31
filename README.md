# IrisPrediction
Trying FastAPI by creating an API for a classification model on the sklearn iris dataset

### run server locally
<code>uvicorn main:app --reload</code>

### Example:

endpoint:

/predictions/

body: 

<code>
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
</code>
<br>

result:
![image](https://user-images.githubusercontent.com/37815834/88993981-f97abd80-d2ac-11ea-9301-b932f79313fd.png)
