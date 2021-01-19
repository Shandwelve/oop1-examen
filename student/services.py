from .models import Student


def get_students(order, direction):
    if not order:
        order = 'name'

    if direction == 'DESC':
        order = '-{}'.format(order)
    return Student.objects.all().order_by(order)


def add_student(name, discipline, mark):
    print(name)
    print(discipline)
    print(mark)
    student = Student.objects.filter(name=name,
                                     discipline=discipline)
    if student:
        student.update(mark=mark)
    else:
        Student.objects.create(name=name,
                               discipline=discipline,
                               mark=mark)
