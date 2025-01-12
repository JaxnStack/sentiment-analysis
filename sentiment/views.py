from django.shortcuts import render
from .forms import CSVUploadForm
import pandas as pd
from django.http import HttpResponse

def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the uploaded CSV file into a pandas DataFrame
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)

            # You can now process the data here (e.g., perform sentiment analysis)

            # Just for demonstration, let's return the first few rows
            return HttpResponse(df.head())
    else:
        form = CSVUploadForm()

    return render(request, 'sentiment/upload_csv.html', {'form': form})
