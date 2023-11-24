from flask import Flask, jsonify, Blueprint
from dotenv import load_dotenv
import os


load_dotenv('.env')

api = Blueprint("api", __name__)

@api.route('/api/description')
@api.route('/api')
@api.route('/api/endpoints')
def endpoints(): 
    """retrurns all current endpoints and acts as the default and a description of each endpoint"""
    rules = [rule for rule in api.url_map.iter_rules() if rule.endpoint != 'static']
    endpoints = [rule.endpoint for rule in rules]
    return jsonify({'endpoints': endpoints})
    
    
@api.route('/api/profile')
@api.route('/api/socials')
def profile(): #returns social media links
    """
    github
    linkedin
    """
    profile = {name: os.getenv('FULL_NAME'),
    githubUsername: 'Xeiiroa',
    githubLink: 'https://github.com/Xeiiroa',
    githubProfileImage: 'https://github.com/settings/profile',
    linkedIn: os.getenv('LINKEDIN'),
    }

    return jsonify(profile)
@api.route('/api/education')
def education(): #returns information based on education
    education = os.getenv('EDUCATION_INFO')


@api.route('/api/experience')
def experience(): #returns related work experience/ all work experience
    ...


@api.route('/api/projects', methods=['GET', 'POST'])
def projects(): #returns information for projects 
    Personal_Projects = [
        {
            title: 'Peeps',
            year: 'August 2023',
            description: 'A security camera software utilizing facial recognition for its captures',
            technologies: ['Python', 'SQLite', 'Computer Vision', 'Twilio']
            github_repo: 'https://github.com/Xeiiroa/Security-Camera'
            
    }
        {
            title: 'API Resume'
            year: 'November 2023'
            description: 'A resume converted to API Format',
            technologies: ['Python', 'Flask', 'HTML', 'CSS'],
            github_repo: 
        }]
    """
    reason you did them  
    
    description for project
    
    technologioes used
    """
    
  
@api.route('/api/docs') #can also be /documentation
def documentation(): #returns documentation for this project as well as its github repo
    ...



    