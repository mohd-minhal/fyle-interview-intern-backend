from flask import Blueprint, jsonify, request
from core.apis.decorators import AuthPrincipal
from core.models.assignments import Assignment
from core.models.teachers import Teacher

principal_api = Blueprint('principal_api', __name__)


@principal_api.route('/principal/assignments', methods=['GET'])
def list_submitted_and_graded_assignments():
    assignments = Assignment.get_submitted_and_graded()
    return jsonify({"data": [assignment.to_dict() for assignment in assignments]})


@principal_api.route('/principal/teachers', methods=['GET'])
def list_all_teachers():
    teachers = Teacher.get_all_teachers()
    return jsonify({"data": [teacher.to_dict() for teacher in teachers]})


@principal_api.route('/principal/assignments/grade', methods=['POST'])
def grade_assignment():
    data = request.get_json()
    assignment_id = data.get('id')
    grade = data.get('grade')
    auth_principal = AuthPrincipal.from_request()
    assignment = Assignment.mark_grade(assignment_id, grade, auth_principal)
    return jsonify({"data": assignment.to_dict()})
