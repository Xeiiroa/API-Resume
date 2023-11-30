from dotenv import load_dotenv
import os
from fastapi import APIRouter


load_dotenv('.env')
router = APIRouter()

@router.get('/api')
@router.get('/')
def endpoints(): 
    """retrurns all current endpoints and acts as the default and a description of each endpoint"""
    message = [{'message': 'Success'},
    {
        'greeting': 'Welcome to my API resume here are my endpoints that all are tailored to a section of my complete resume',
        'documentationUrl': 'https://github.com/Xeiiroa/API-Resume',
        'endpoints': [
        {'method': "GET", 'path': "/api", 'description': "Describes all available endpoints"},
        {'method': "GET", 'path': "/profile", 'description': "shows social media profiles"},
        {'method': "GET", 'path': "/experience", 'description': "shows present and past work experience"},
        {'method': "GET", 'path': "/education", 'description': "shows education"},
        {'method': "GET", 'path': "/projects", 'description': "shows projects"},
        {'method': "GET", 'path': "/skills", 'description': "shows technical skills"}
        ]
    }]
    return message
    
    
@router.get('/profile')
def profile(): 
    profile = [{'message': 'Success'},
    {
    'name': os.getenv('FULL_NAME'),
    'github_username': 'Xeiiroa',
    'github_link': 'https://github.com/Xeiiroa',
    'linkedIn': os.getenv('LINKEDIN'), 
    }]

    return profile

@router.get('/education')
def education():
    education = [{'message': 'Success'},
    {
        'school': os.getenv('SCHOOL_1_NAME'),
        'degree': 'Associate of Science in Computer Science',
        'year': '2023-2025',
        'location': os.getenv('SCHOOL_1_LOCATION')
    }]


@router.get('/experience')
def experience(): #returns related work experience/ all work experience
    experience = [{'message': 'Success'},
        {
        'company': os.getenv('COMPANY_1_NAME'),
        'title': 'Field Service Technician,',
        'year': 'August 2022 - June 2023',
        'responsibilites': [
            
        ]
    }]
    return experience


@router.get('/projects')
def projects(): #returns information for projects 
    projects = [{'message': 'Success'},
    {
    'personal_projects': [
        {
            'title': 'Peeps',
            'year': 'August 2023',
            'description': 'A security camera software utilizing facial recognition for its captures',
            'technologies': ['Python', 'SQLite', 'Computer Vision', 'Twilio'],
            'github_repo': 'https://github.com/Xeiiroa/Security-Camera'   
        },
        {
            'title': 'API Resume',
            'year': 'November 2023',
            'description': 'A resume converted to API Format',
            'technologies': ['Python', 'FastAPI','Uvicorn', 'HTML', 'CSS'], #can remove html css
            'github_repo': 'https://github.com/Xeiiroa/API-Resume'
        }
        ]
    }]
    return projects

@router.get('/skills')
def technical_skills():
    technical_skills = [{'message': 'Success'},
    {
        'languages': ['Python', 'C', 'Java'],
        'frameworks': ['Flask', 'FastAPI']
    }]


    