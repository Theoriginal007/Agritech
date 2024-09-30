from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # This is your project's landing page or home view
    return HttpResponse("""
        <h1>Welcome to the Agritech Project!</h1>
        <p>
            Agritech is a revolutionary platform designed to transform the agriculture industry by leveraging cutting-edge 
            technology. Our mission is to empower farmers, agricultural businesses, and stakeholders to optimize 
            production, increase yield, and manage resources more efficiently.
        </p>
        <p>
            From soil analysis and crop monitoring to market price predictions and real-time resource management, 
            Agritech provides a comprehensive suite of tools that drive sustainable farming and enhance productivity 
            across the entire agricultural ecosystem. We aim to connect farmers with modern solutions that make 
            farming smarter, more profitable, and eco-friendly.
        </p>
        <p>
            <b>Explore the platform and join us on our mission to revolutionize the future of agriculture!</b>
        </p>
    """)


def signup_view(request):
    return render(request, 'myapp/signup.html')
