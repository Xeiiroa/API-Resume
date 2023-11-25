from dotenv import load_dotenv
import os
from fastapi import APIRouter


load_dotenv('.env')
router = APIRouter()

@router.get('/api')
@router.get('/endpoints')
def endpoints(): 
    """retrurns all current endpoints and acts as the default and a description of each endpoint"""
    return {'endpoints': [{'path': route.path, 'name': route.name} for route in router.routes]}
    
    
@router.get('/profile')
@router.get('/socials')
@router.get('/')
def profile(): #returns social media links #todo make profile act as the homepage
    profile = {
    'name': os.getenv('FULL_NAME'),
    'github_username': 'Xeiiroa',
    'github_link': 'https://github.com/Xeiiroa',
    'linkedIn': os.getenv('LINKEDIN'), 
    }    

    return profile

@router.get('/education')
def education(): #returns information based on education
    return os.getenv('EDUCATION_INFO')


@router.get('/experience')
def experience(): #returns related work experience/ all work experience
    return os.getenv('EXPERIENCE')


@router.get('/projects')
def projects(): #returns information for projects 
    projects = [{
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
@router.get('technical-skills')
def technical_skills():
    technical_skills = [{
        'languages': ['Python', 'C', 'Java'],
        'frameworks': ['Flask', 'FastAPI']
    }]


    