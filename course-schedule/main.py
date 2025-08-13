from collections import defaultdict


def assess_courses(num_courses: int, prerequisites: list[list[int]]):
    pre_req_dict = defaultdict(list)

    for p, q in prerequisites:
        pre_req_dict[p].append(q)

    taken_courses = set()
    pending_courses = set()

    courses = set([i for i in range(num_courses)])

    def take_course(course):
        if course in taken_courses:
            return True
        if course in pending_courses:
            return False

        pending_courses.add(course)
        for pre_req in pre_req_dict[course]:
            result = take_course(pre_req)
            if not result:
                return False

        pending_courses.remove(course)
        taken_courses.add(course)
        return True

    while len(courses) > 0:
        course = courses.pop()
        result = take_course(course)
        if not result:
            return False

    return True


if __name__ == "__main__":
    assert assess_courses(4, [[2, 1], [3, 1], [4, 2], [3, 4]])
    assert not assess_courses(4, [[2, 1], [3, 1], [4, 2], [3, 4], [1, 4]])
