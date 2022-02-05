from flask import Blueprint, request, jsonify
from app import db
from app.models.business import Business
from .helper_functions import *

businnes_bp = Blueprint("businesses", __name__, url_prefix="/businesses")

####---------------------------------------------------####
####----------------- BUSINESS ENDPOINTS -----------------####
####---------------------------------------------------####
@businnes_bp.route("", methods=["POST"])
def create_business():
    request_body = request.get_json()
    valid_input(request_body, Business)
    new_business = Business(name = request_body["name"],
                            street = request_body["street"],
                            city = request_body["city"],
                            zipcode = request_body["zipcode"],
                            state = request_body["state"],
                            website = request_body["website"],
                            category = request_body["category"],
                            like_count = 0)
    db.session.add(new_business)
    db.session.commit()
    return jsonify(new_business.to_dic()), 200

@businnes_bp.route("", methods=["GET"])
def get_busineses():
    """
    Getting all businesses
    """
    businesses = Business.query.all()
    businesses_response = [business.to_dic() for business in businesses]
    return jsonify(businesses_response), 200

@businnes_bp.route("/<business_id>", methods=["GET"])
def get_a_busines(business_id):
    """
    Getting a businesses with the given id
    """
    business = valid_id(Business, business_id)
    return jsonify(business.to_dic()), 200

@businnes_bp.route("/filters", methods=["GET"])
def get_business_for_selected_category_zipcode():
    """
    Getting all businesses locatted in a given zipcode and for a given category
    """
    requested_category = request.args.get('category')
    
    requested_zipcode = request.args.get('zipcode')
    
    if (requested_category and requested_zipcode):
        requested_category=requested_category.capitalize()
        businesses = Business.query.filter_by(category = requested_category).filter_by(zipcode=requested_zipcode)
    elif (requested_category ): 
        requested_category=requested_category.capitalize()
        businesses = Business.query.filter_by(category = requested_category) 
    elif (requested_zipcode ): 
        businesses = Business.query.filter_by(zipcode = requested_zipcode) 
    
    business_response = [business.to_dic() for business in businesses]
    
    return jsonify(business_response), 200

@businnes_bp.route("/<business_id>", methods=["DELETE"])
def delete_selected_business(business_id):
    """
    delete a businesses  with a given id
    """
    business = valid_id(Business, business_id)
    db.session.delete(business)
    db.session.commit()
    return {"id": business.id},200

@businnes_bp.route("/<business_id>", methods=["PATCH"])
def update_selected_business(business_id):
    """
    update a businesses  with a given id
    """
    business = valid_id(Business, business_id)
    request_body = request.get_json()
    valid_input(request_body, Business)
    if "name" in request_body:
        business.name = request_body["name"]
    if "street" in request_body:
        business.street = request_body["street"]
    if "city"  in request_body:  
        business.city = request_body["city"]
    if "state" in request_body:
        business.state = request_body["state"]
    if "zipcode" in request_body:
        business.zipcode = request_body["zipcode"]
    if "website" in request_body:
        business.website = request_body["website"]
    if "category" in request_body:
        business.category = request_body["category"]
    if "like_count" in request_body:
        business.like_count = business.like_count
    db.session.commit()
    return jsonify(business.to_dic()),200

@businnes_bp.route("/<business_id>/like", methods=["PATCH"])
def update_selected_business_like_count(business_id):
    """
    update  businesses like_count  with a given id
    """
    business = valid_id(Business, business_id)
    business.like_count += 1
    db.session.commit()
    return jsonify(business.to_dic()),200
    
@businnes_bp.route("/<business_id>/dislike", methods=["PATCH"])
def decrease_selected_business_like_count(business_id):
    """
    update  businesses like_count  with a given id
    """
    business = valid_id(Business, business_id)
    business.like_count = 0
    db.session.commit()
    return jsonify(business.to_dic()),200

    
