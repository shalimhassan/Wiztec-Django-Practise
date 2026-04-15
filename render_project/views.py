from django.shortcuts import render

def home_page(request):
  
  info ={
    "name": "Rohim",
    "address": "Korimnagar",
  }

  return render(request,"home.html", info)
