from flask import request
from flask import Blueprint
from flask import jsonify
from core.apis.decorators import AuthPrincipal
from core.models.assignments import Assignment
from core.models.teachers import Teacher

principal_api = Blueprint('principal_api', __name__)

@principal_api.route('/principal/assignments', methods=['GET'])
def list_submitted_and_graded_assignments():
    assignments = Assignment.get_submitted_and_graded()
    assignment_data = []
    
    for assignment in assignments:
        assignment_dict = assignment.to_dict()
        assignment_data.append(assignment_dict)
    
    return jsonify({"data": assignment_data})

@principal_api.route('/principal/teachers', methods=['GET'])
def list_all_teachers():
    teachers = Teacher.get_all_teachers()
    teacher_data = []
    
    for teacher in teachers:
        teacher_dict = teacher.to_dict()
        teacher_data.append(teacher_dict)

    return jsonify({"data": teacher_data})

@principal_api.route('/principal/assignments/grade', methods=['POST'])
def grade_assignment():
    data = request.get_json()
    assignment_id = data.get('id')
    grade = data.get('grade')
    
    auth_principal = AuthPrincipal.from_request()

    assignment = Assignment.mark_grade(assignment_id, grade, auth_principal)
    
    if assignment:
        return jsonify({"data": assignment.to_dict()}), 200
