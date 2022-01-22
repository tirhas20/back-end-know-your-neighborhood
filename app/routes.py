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
                            category = request_body["category"])
    db.session.add(new_business)
    db.session.commit()
    return {"id":new_business.id}, 201

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
    
@businnes_bp.route("/uniquezipcode", methods=["GET"])
def get_busineses_zipcode():
    """
    Getting all unique zipcodes where the businesses are located 
    """
    businesses = Business.query.all()
    businesses_response= []
    for business in businesses:
        if business.to_dic_zipcode() not in businesses_response:
            businesses_response.append(business.to_dic_zipcode())
    # businesses_response = [business.to_dic_zipcode() for business in businesses]
    return jsonify(businesses_response), 200

@businnes_bp.route("/uniquecategory", methods=["GET"])
def get_busineses_category():
    """
    Getting all unique categorys for the businesses.  
    """
    businesses = Business.query.all()
    businesses_response= []
    for business in businesses:
        if business.to_dic_category() not in businesses_response:
            businesses_response.append(business.to_dic_category())
    # businesses_response = [business.to_dic_category() for business in businesses]
    return jsonify(businesses_response), 200

@businnes_bp.route("/zipcode", methods=["GET"])
def get_business_for_selected_zipcode():
    """
    Getting all businesses locatted in a given zipcode
    """
    requested_zipcode = request.args.get('zipcode')
    print(requested_zipcode)
    if requested_zipcode:
        businesses = Business.query.filter_by(zipcode = requested_zipcode)
    business_response = [business.to_dic() for business in businesses]
    return jsonify(business_response), 200

@businnes_bp.route("/category", methods=["GET"])
def get_business_for_selected_category():
    """
    Getting all businesses locatted for a given category
    """
    requested_category = request.args.get('category')
    print(requested_category)
    if requested_category:
        businesses = Business.query.filter_by(category = requested_category)
    business_response = [business.to_dic() for business in businesses]
    return jsonify(business_response), 200

@businnes_bp.route("/zipcode/category", methods=["GET"])
def get_business_for_selected_category_zipcode():
    """
    Getting all businesses locatted in a given zipcode and for a given category
    """
    requested_category = request.args.get('category')
    requested_zipcode = request.args.get('zipcode')
    print(requested_category)
    if requested_category and requested_zipcode:
        businesses = Business.query.filter_by(category = requested_category).filter_by(zipcode=requested_zipcode)
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

@businnes_bp.route("/<business_id>", methods=["PUT"])
def update_selected_business(business_id):
    """
    update a businesses  with a given id
    """
    business = valid_id(Business, business_id)
    request_body = request.get_json()
    valid_input(request_body, Business)
    business.name = request_body["name"]
    business.street = request_body["street"]
    business.city = request_body["city"]
    business.state = request_body["state"]
    business.website = request_body["website"]
    business.category = request_body["category"]
    db.session.commit()
    return jsonify(business.to_dic()),200