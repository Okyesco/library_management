from django.shortcuts import render, get_object_or_404, redirect
from .models import StudentRecord, Issuer, StudentReturn, LibraryShelve, SchoolLogo, BorrowerImage, TeachersRecord, \
                    TeachersReturn, TeacherImage
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        stage = request.POST['stage']
        sex = request.POST['sex']
        book_name = request.POST['book_name']
        issuer = request.POST['issuer']
        return_date = request.POST['return_date']
        comment = request.POST['comment']
        author = request.POST['author']
        edition = request.POST['edition']

        StudentRecord.objects.create(student_name=student_name, stage=stage, sex=sex, book_name=book_name,
                                     issuer_id=issuer, return_date=return_date, comment=comment, edition=edition,
                                     author=author)

        return HttpResponse(
            f"<h3> <span style='color:red;'>{student_name}'s</span> Records Added Successfully</h3><a href='/'>Home</a>")
    else:
        issuer_list = Issuer.objects.all()
        shelves = LibraryShelve.objects.all()
        logo = SchoolLogo.objects.all()
        return render(request, 'index.html', {'issuers': issuer_list, 'shelves': shelves, 'logo': logo})


# show borrowed records
def records(request):
    borrowed = StudentRecord.objects.all()
    total_records = StudentRecord.objects.count()
    return render(request, 'table.html', {'records': borrowed, 'total_records': total_records})


# show student detail
def details(request, ad):
    detail = get_object_or_404(StudentRecord, pk=ad)
    image = BorrowerImage.objects.all()
    return render(request, 'list.html', {'detail': detail, 'images': image})


# delete student record
def delete(request, pk):
    detail = get_object_or_404(StudentRecord, pk=pk)

    deleted = StudentReturn(id=detail.id, student_name=detail.student_name, book_name=detail.book_name,
                            date_borrowed=detail.date_borrowed, comment=detail.comment, issuer=detail.issuer,
                            sex=detail.sex, stage=detail.stage, edition=detail.edition,author=detail.author)

    deleted.save()

    detail.delete()
    return redirect('records')


def teachers(request):
    if request.method == 'POST':
        teacher_name = request.POST['teacher_name']
        phone_number = request.POST['phone_number']
        sex = request.POST['sex']
        book_name = request.POST['book_name']
        issuer = request.POST['issuer']
        return_date = request.POST['return_date']
        comment = request.POST['comment']
        author = request.POST['author']
        edition = request.POST['edition']

        TeachersRecord.objects.create(teacher_name=teacher_name, phone_number=phone_number, sex=sex, book_name=book_name,
                                      issuer_id=issuer, return_date=return_date, comment=comment, edition=edition,
                                      author=author)

        return HttpResponse(
            f"<h3> <span style='color:red;'>{teacher_name}'s</span> Records Added Successfully</h3><a href=''>Home</a>")
    else:
        issuer_list = Issuer.objects.all()
        logo = SchoolLogo.objects.all()
        return render(request, 'teachers.html', {'issuers': issuer_list, 'logo': logo})


def teachers_records(request):
    borrowed = TeachersRecord.objects.all()
    total_records = TeachersRecord.objects.count()
    return render(request, 'teachers_table.html', {'records': borrowed, 'total_records': total_records})


def teachers_details(request, ac):
    detail = get_object_or_404(TeachersRecord, pk=ac)
    image = TeacherImage.objects.all()
    return render(request, 'teachers_list.html', {'detail': detail, 'images': image})


def teacher_delete(request, ax):
    detail = get_object_or_404(TeachersRecord, pk=ax)

    deleted = TeachersReturn(id=detail.id, teacher_name=detail.teacher_name, book_name=detail.book_name,
                             date_borrowed=detail.date_borrowed, comment=detail.comment, issuer=detail.issuer,
                             sex=detail.sex, phone_number=detail.phone_number, edition=detail.edition,
                             author=detail.author)

    deleted.save()

    detail.delete()
    return redirect('teachers_records')