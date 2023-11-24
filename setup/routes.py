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
    

@api.route('/api/education')
def education(): #returns information based on education
    ...


@api.route('/api/experience')
def experience(): #returns related work experience/ all work experience
    ...


@api.route('/api/projects')
def projects(): #returns information for projects 
    """
    reason you did them  
    
    description for project
    
    technologioes used
    """
    
  
@api.route('/api/docs') #can also be /documentation
def documentation(): #returns documentation for this project as well as its github repo
    ...



    