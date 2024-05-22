import joblib
import warnings
warnings.filterwarnings('ignore')
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def url_check(request):
    if request.method == "POST":
        url = request.POST.get('url')
        model = joblib.load('pre-trained-model/RandomForestModel.pkl')
        vectorizer = joblib.load('pre-trained-model/TfidfVectorizer.pkl')
        pred = model.predict(vectorizer.transform([url]))
        labels = ["BENIGN", "MALICIOUS"]
        status = labels[pred[0]]
        print("Prediction: ",status)
        request.session['result'] = status
        return redirect(predict)
    return render(request, 'url_check.html')


def predict(request):
    result = request.session.get('result')
    return render(request, 'prediction.html',{'status':result})
