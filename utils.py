import requests


def load_candidates_from_server_json():
    """
    Получение json данных с сервера
    :return: данные в json формате
    """
    response = requests.get('https://www.jsonkeeper.com/b/AFB3')

    return response.json()


def get_candidate(candidate_id: int):
    """

    :param candidate_id: id кандидата
    :return: словарь с данными о кандидате
    """
    data = load_candidates_from_server_json()

    candidate = ''

    for i in data:
        if i['id'] == candidate_id:
            candidate = i

    return candidate


def get_candidates_by_name(candidate_name):
    """

    :param candidate_name: имя кандидата
    :return: список словарей с подходящеми по именам кандидатами
    """
    data = load_candidates_from_server_json()

    candidates = []

    for i in data:
        if i['name'] == candidate_name:
            candidates.append(i)

    return candidates


def get_candidates_by_skill(skill_name):
    """

    :param skill_name: скилы кандидата
    :return: список словарей с подходящеми по скилам кандидатами
    """
    data = load_candidates_from_server_json()

    candidates = []

    for i in data:
        if skill_name.lower() in i['skills']:

            candidates.append(i)

    return candidates
