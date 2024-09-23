import json
from core.models.assignments import AssignmentStateEnum, GradeEnum
from core.models.principals import Principal
from core import db


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [
            AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B


def test_list_all_teachers(client):
    response = client.get('/principal/teachers')

    assert response.status_code == 200

    data = response.json['data']

    assert isinstance(data, list)

    if data:
        assert 'id' in data[0]
        assert 'user_id' in data[0]


def test_get_non_existent_principal(client):
    response = client.get(
        '/principal/details', headers={'X-Principal': json.dumps({'principal_id': 999})})
    assert response.status_code == 404


def test_query_principal_directly(db_session):
    # Create a principal directly for testing
    principal = Principal(user_id=1)
    db.session.add(principal)
    db.session.commit()

    fetched_principal = Principal.query.filter_by(user_id=1).first()

    assert fetched_principal is not None
    assert fetched_principal.user_id == 1
