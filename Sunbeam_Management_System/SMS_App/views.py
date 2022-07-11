from datetime import date
from glob import glob
from imaplib import _Authenticator
from mmap import PAGESIZE
from multiprocessing import context
from os import stat
from pickle import TRUE
from re import A
from tabnanny import check
from telnetlib import AUTHENTICATION
from turtle import update
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import admin_signup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

import os
import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle, colors


def homepage(request):
    if request.method == 'POST':
        feed = request.POST.get('comment')
        newfeed = feedbacks.objects.create(feed=feed)
        newfeed.save()

    stats = customers.objects.filter(status='TENTATIVE').count()
    if stats == 0:
        return render(request, 'html/1_SMS_Homepage.html')
    else:
        record = customers.objects.filter(status='TENTATIVE')
        record.delete()
        return render(request, 'html/1_SMS_Homepage.html')


def c_reservation(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        cellnum = request.POST.get('cellnum')
        email = request.POST.get('email')
        room_name = request.POST.get('Room Name')
        numguest = request.POST.get('numguest')
        cid = request.POST.get('cid')
        cod = request.POST.get('cod')
        total_days = request.POST.get('total_days')
        acts = request.POST.get('activity')
        status = request.POST.get('status')
        price = request.POST.get('price')
        code = request.POST.get('random_code')

        ########################################################
        check_in = cid

        if check_in[5] == 0 and check_in[8] == 0:
            ci_date = date(int(check_in[0:4]), int(
                check_in[6]), int(check_in[9]))

        elif check_in[5] != 0 and check_in[8] == 0:
            ci_date = date(int(check_in[0:4]), int(
                check_in[5:7]), int(check_in[9]))

        elif check_in[5] == '0' and check_in[8] != '0':
            ci_date = date(int(check_in[0:4]), int(
                check_in[6]), int(check_in[8:]))

        elif check_in[5] != '0' and check_in[8] != '0':
            ci_date = date(int(check_in[0:4]), int(
                check_in[5:7]), int(check_in[8:]))

        #########################################################################
        check_out = cod

        if check_out[5] == 0 and check_out[8] == 0:
            co_date = date(int(check_out[0:4]), int(
                check_out[6]), int(check_out[9]))

        elif check_out[5] != 0 and check_out[8] == 0:
            co_date = date(int(check_out[0:4]), int(
                check_out[5:7]), int(check_out[9]))

        elif check_out[5] == '0' and check_out[8] != '0':
            co_date = date(int(check_out[0:4]), int(
                check_out[6]), int(check_out[8:]))

        elif check_out[5] != '0' and check_out[8] != '0':
            co_date = date(int(check_out[0:4]), int(
                check_out[5:7]), int(check_out[8:]))

        #######################################################################################

        customer = customers.objects.filter(room_name_id=room_name)

        for i in customer:

            if i.checkout_date[5] == 0 and i.checkout_date[8] == 0:
                rco_date = date(int(i.checkout_date[0:4]), int(
                    i.checkout_date[6]), int(i.checkout_date[9]))

            elif i.checkout_date[5] != 0 and i.checkout_date[8] == 0:
                rco_date = date(int(i.checkout_date[0:4]), int(
                    i.checkout_date[5:7]), int(i.checkout_date[9]))

            elif i.checkout_date[5] == '0' and i.checkout_date[8] != '0':
                rco_date = date(int(i.checkout_date[0:4]), int(
                    i.checkout_date[6]), int(i.checkout_date[8:]))

            elif i.checkout_date[5] != '0' and i.checkout_date[8] != '0':
                rco_date = date(int(i.checkout_date[0:4]), int(
                    i.checkout_date[5:7]), int(i.checkout_date[8:]))

            #############################################################################################
            if i.checkin_date[5] == 0 and i.checkin_date[8] == 0:
                rci_date = date(int(i.checkin_date[0:4]), int(
                    i.checkin_date[6]), int(i.checkin_date[9]))

            elif i.checkin_date[5] != 0 and i.checkin_date[8] == 0:
                rci_date = date(int(i.checkin_date[0:4]), int(
                    i.checkin_date[5:7]), int(i.checkin_date[9]))

            elif i.checkin_date[5] == '0' and i.checkin_date[8] != '0':
                rci_date = date(int(i.checkin_date[0:4]), int(
                    i.checkin_date[6]), int(i.checkin_date[8:]))

            elif i.checkin_date[5] != '0' and i.checkin_date[8] != '0':
                rci_date = date(int(i.checkin_date[0:4]), int(
                    i.checkin_date[5:7]), int(i.checkin_date[8:]))

            # checkin date > registered check out dates
            test1 = ci_date - rco_date  # possitive number

            # checkin date < registered check in dates
            test2 = rci_date - ci_date  # possitive number

            # checkout date > registered check out dates
            test3 = co_date - rco_date  # possitive number

            # checkout date < registered check in dates
            test4 = rci_date - co_date  # possitive number

            if str(i.checkin_date) == str(cid):
                messages.error(
                    request, 'Your Check In date is currently chosen. Please Choose a different check in date. 1')
                return render(request, 'html/2_SMS_Reservation.html')

            elif test1.days <= 0 and test2.days <= 1:
                messages.error(
                    request, 'Your Check In date is currently chosen. Please Choose a different check in date. 2')
                return render(request, 'html/2_SMS_Reservation.html')

            elif test3.days <= 1 and test4.days <= 0:
                messages.error(
                    request, 'Your Check Out date is currently chosen. Please Choose a different check out date.  4')
                return render(request, 'html/2_SMS_Reservation.html')

            elif test2.days > 1 and test3.days > 1:
                messages.error(
                    request, 'Date already selected. Please Choose another date')
                return render(request, 'html/2_SMS_Reservation.html')

        new_customer = customers.objects.create(first_name=fname, last_name=lname, contact_num=cellnum, email=email,
                                                room_name_id=room_name, guest=numguest, checkin_date=cid, checkout_date=cod,
                                                num_of_days=total_days, activity=acts, status=status, price=price, code=code)

        new_customer.save()
        return redirect('billing')

    return render(request, 'html/2_SMS_Reservation.html')


def billing(request):
    last_customer = customers.objects.all()
    if len(last_customer) == 0:
        return redirect('Reservation')
    else:
        stats = customers.objects.filter(status='TENTATIVE').count()
        if stats == 0:
            return redirect('Reservation')
        context = {}
        context["customer"] = customers.objects.get(status='TENTATIVE')
        return render(request, 'html/3_SMS_Billing.html', context)


def confirmation(request):
    if request.method == 'POST':
        c_code = request.POST.get('c_code')
        email = request.POST.get('email')
        send_mail(
            'Confirmation',
            'Good Day! Your confirmation code is ' + str(c_code) + ".",
            'tropaniaubrey@gmail.com',
            [email],
        )
        return redirect('Reservation')

    else:
        last_customer = customers.objects.all()
        if len(last_customer) == 0:
            return redirect('Reservation')
        else:
            stats = customers.objects.filter(status='TENTATIVE').count()
            if stats == 0:
                return redirect('Reservation')
            context = customers.objects.get(status='TENTATIVE')
            context.status = "RESERVED"
            context.save()
            context_2 = {}
            context_2["customer"] = customers.objects.last()
            return render(request, 'html/4_SMS_Confirmation.html', context_2)


@login_required(login_url='login')
def signup(request):
    form = admin_signup()
    if request.method == "POST":
        form = admin_signup(request.POST)
        if form.is_valid():
            form.instance.is_superuser = True
            form.instance.is_staff = True
            form.save()
            return redirect('logout')

    context = {'form': form}
    return render(request, 'html/6_SMS_Signup.html', context)


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("reservation")

    return render(request, 'html/5_SMS_Login.html')


@login_required(login_url='login')
def reservation(request):
    global update_customer
    if request.method == 'POST':
        type = request.POST.get('type')
        customer_id = request.POST.get('customer_num')
        if type == 'DELETE':
            delete_customer = customers.objects.get(customer_num=customer_id)
            delete_customer.delete()
        else:
            update_customer = customers.objects.get(customer_num=customer_id)
            update_customer.status = "BOOKED"
            update_customer.save()
            update_room = rooms.objects.get(
                room_name=update_customer.room_name_id)
            update_room.room_status = "BOOKED"
            update_room.save()

            if update_customer.activity == "Activity Set 1":
                checkin_bankero()
                checkin_boat()
                checkin_diving_suit()
                checkin_diving_gear()
                checkin_life_vest()
                checkin_flashlights()
                checkin_regulators()
                checkin_oxygen_tanks()
                checkin_ropes()
                checkin_diving_instructor()

            elif update_customer.activity == "Activity Set 2":
                checkin_bankero()
                checkin_boat()
                checkin_life_vest()
                checkin_snorkels()
                checkin_ropes()

            elif update_customer.activity == "Activity Set 3" or update_customer.activity == "Activity Set 7" or update_customer.activity == "Activity Set 9" or update_customer.activity == "Activity Set 11" or update_customer.activity == "Activity Set 13" or update_customer.activity == "Activity Set 14" or update_customer.activity == "Activity Set 15":
                checkin_bankero()
                checkin_boat()
                checkin_diving_suit()
                checkin_diving_gear()
                checkin_life_vest()
                checkin_flashlights()
                checkin_regulators()
                checkin_oxygen_tanks()
                checkin_ropes()
                checkin_diving_instructor()
                checkin_snorkels()

            elif update_customer.activity == "Activity Set 4":
                checkin_bankero()
                checkin_boat()
                checkin_diving_suit()
                checkin_diving_gear()
                checkin_life_vest()
                checkin_regulators()
                checkin_oxygen_tanks()
                checkin_ropes()
                checkin_diving_instructor()

            elif update_customer.activity == "Activity Set 5":
                checkin_bankero()
                checkin_boat()
                checkin_diving_suit()
                checkin_diving_gear()
                checkin_life_vest()
                checkin_flashlights()
                checkin_regulators()
                checkin_oxygen_tanks()
                checkin_ropes()
                checkin_diving_instructor()

            elif update_customer.activity == "Activity Set 6":
                checkin_bankero()
                checkin_boat()
                checkin_diving_suit()
                checkin_diving_gear()
                checkin_life_vest()
                checkin_regulators()
                checkin_oxygen_tanks()
                checkin_ropes()
                checkin_diving_instructor()
                checkin_snorkels()

            elif update_customer.activity == "Activity Set 8":
                checkin_boat()
                checkin_life_vest()
                checkin_snorkels()

            elif update_customer.activity == "Activity Set 10":
                checkin_boat()
                checkin_life_vest()
                checkin_snorkels()
                checkin_bankero()
                checkin_ropes()

            elif update_customer.activity == "Activity Set 12":
                checkin_bankero()
                checkin_boat()
                checkin_diving_suit()
                checkin_diving_gear()
                checkin_life_vest()
                checkin_regulators()
                checkin_oxygen_tanks()
                checkin_ropes()
                checkin_diving_instructor()
                checkin_snorkels()

    reserved_customers = customers.objects.filter(status="RESERVED")
    context = {'reserved_customers': reserved_customers}
    return render(request, 'html/7_SMS_Managerial_Module_Reservations.html', context)


# def reservation_update(request):
#     type = request.POST.get('type')
#     if request.method == 'POST' and type == 'DELETE':
#         customer_id = request.POST.get('customer_num')
#         update_customer = customers.objects.get(customer_num=customer_id)
#         update_customer.status = "RESERVED"
#         update_customer.save()

#     reserved_customers = customers.objects.filter(status="RESERVED")
#     context = {'reserved_customers': reserved_customers}
#     return render(request, 'html/7_SMS_Managerial_Module_Reservations.html', context)

@login_required(login_url='login')
def booking(request):
    global update_customers
    if request.method == 'POST':
        customer_id = request.POST.get('customer_num')
        update_customers = customers.objects.get(customer_num=customer_id)
        update_customers.status = "CHECKED OUT"
        update_customers.save()

        update_room = rooms.objects.get(
            room_name=update_customers.room_name_id)
        update_room.room_status = "AVAILABLE"
        update_room.save()

        if update_customers.activity == "Activity Set 1":
            booking_bankero()
            booking_boat()
            booking_diving_suit()
            booking_diving_gear()
            booking_life_vest()
            booking_flashlights()
            booking_regulators()
            booking_oxygen_tanks()
            booking_ropes()
            booking_diving_instructor()

        elif update_customers.activity == "Activity Set 2":
            booking_bankero()
            booking_boat()
            booking_life_vest()
            booking_snorkels()
            booking_ropes()

        elif update_customers.activity == "Activity Set 3" or update_customers.activity == "Activity Set 7" or update_customers.activity == "Activity Set 9" or update_customers.activity == "Activity Set 11" or update_customers.activity == "Activity Set 13" or update_customers.activity == "Activity Set 14" or update_customers.activity == "Activity Set 15":
            booking_bankero()
            booking_boat()
            booking_diving_suit()
            booking_diving_gear()
            booking_life_vest()
            booking_flashlights()
            booking_regulators()
            booking_oxygen_tanks()
            booking_ropes()
            booking_diving_instructor()
            booking_snorkels()

        elif update_customers.activity == "Activity Set 4":
            booking_bankero()
            booking_boat()
            booking_diving_suit()
            booking_diving_gear()
            booking_life_vest()
            booking_regulators()
            booking_oxygen_tanks()
            booking_ropes()
            booking_diving_instructor()

        elif update_customers.activity == "Activity Set 5":
            booking_bankero()
            booking_boat()
            booking_diving_suit()
            booking_diving_gear()
            booking_life_vest()
            booking_flashlights()
            booking_regulators()
            booking_oxygen_tanks()
            booking_ropes()
            booking_diving_instructor()

        elif update_customers.activity == "Activity Set 6":
            booking_bankero()
            booking_boat()
            booking_diving_suit()
            booking_diving_gear()
            booking_life_vest()
            booking_regulators()
            booking_oxygen_tanks()
            booking_ropes()
            booking_diving_instructor()
            booking_snorkels()

        elif update_customers.activity == "Activity Set 8":
            booking_boat()
            booking_life_vest()
            booking_snorkels()

        elif update_customers.activity == "Activity Set 10":
            booking_boat()
            booking_life_vest()
            booking_snorkels()
            booking_bankero()
            booking_ropes()

        elif update_customers.activity == "Activity Set 12":
            booking_bankero()
            booking_boat()
            booking_diving_suit()
            booking_diving_gear()
            booking_life_vest()
            booking_regulators()
            booking_oxygen_tanks()
            booking_ropes()
            booking_diving_instructor()
            booking_snorkels()

    booked_customers = customers.objects.filter(status="BOOKED")
    context = {'booked_customers': booked_customers}
    return render(request, 'html/8_SMS_Managerial_Module_Bookings.html', context)


@login_required(login_url='login')
def walk_ins(request):
    global numguest
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        cellnum = request.POST.get('cellnum')
        email = request.POST.get('email')
        room_name = request.POST.get('Room Name')
        numguest = request.POST.get('numguest')
        cid = request.POST.get('cid')
        cod = request.POST.get('cod')
        total_days = request.POST.get('total_days')
        acts = request.POST.get('activity')
        status = request.POST.get('status')
        price = request.POST.get('price')

        new_customer = customers.objects.create(first_name=fname, last_name=lname, contact_num=cellnum, email=email,
                                                room_name_id=room_name, guest=numguest, checkin_date=cid, checkout_date=cod,
                                                num_of_days=total_days, activity=acts, status=status, price=price, code=000000)

        new_customer.save()
        update_room = rooms.objects.get(room_name=room_name)
        update_room.room_status = "BOOKED"
        # return redirect('walk_ins')

        if acts == "Activity Set 1":
            walkin_bankero()
            walkin_boat()
            walkin_diving_suit()
            walkin_diving_gear()
            walkin_life_vest()
            walkin_flashlights()
            walkin_regulators()
            walkin_oxygen_tanks()
            walkin_ropes()
            walkin_diving_instructor()

        elif acts == "Activity Set 2":
            walkin_bankero()
            walkin_boat()
            walkin_life_vest()
            walkin_snorkels()
            walkin_ropes()

        elif acts == "Activity Set 3" or acts == "Activity Set 7" or acts == "Activity Set 9" or acts == "Activity Set 11" or acts == "Activity Set 13" or acts == "Activity Set 14" or acts == "Activity Set 15":
            walkin_bankero()
            walkin_boat()
            walkin_diving_suit()
            walkin_diving_gear()
            walkin_life_vest()
            walkin_flashlights()
            walkin_regulators()
            walkin_oxygen_tanks()
            walkin_ropes()
            walkin_diving_instructor()
            walkin_snorkels()

        elif acts == "Activity Set 4":
            walkin_bankero()
            walkin_boat()
            walkin_diving_suit()
            walkin_diving_gear()
            walkin_life_vest()
            walkin_regulators()
            walkin_oxygen_tanks()
            walkin_ropes()
            walkin_diving_instructor()

        elif acts == "Activity Set 5":
            walkin_bankero()
            walkin_boat()
            walkin_diving_suit()
            walkin_diving_gear()
            walkin_life_vest()
            walkin_flashlights()
            walkin_regulators()
            walkin_oxygen_tanks()
            walkin_ropes()
            walkin_diving_instructor()

        elif acts == "Activity Set 6":
            walkin_bankero()
            walkin_boat()
            walkin_diving_suit()
            walkin_diving_gear()
            walkin_life_vest()
            walkin_regulators()
            walkin_oxygen_tanks()
            walkin_ropes()
            walkin_diving_instructor()
            walkin_snorkels()

        elif acts == "Activity Set 8":
            walkin_boat()
            walkin_life_vest()
            walkin_snorkels()

        elif acts == "Activity Set 10":
            walkin_boat()
            walkin_life_vest()
            walkin_snorkels()
            walkin_bankero()
            walkin_ropes()

        elif acts == "Activity Set 12":
            walkin_bankero()
            walkin_boat()
            walkin_diving_suit()
            walkin_diving_gear()
            walkin_life_vest()
            walkin_regulators()
            walkin_oxygen_tanks()
            walkin_ropes()
            walkin_diving_instructor()
            walkin_snorkels()

    roomses = rooms.objects.filter(
        room_status='AVAILABLE').order_by('room_price')
    context = {'roomses': roomses}
    return render(request, 'html/13_SMS_Managerial_Managerial_Walk_Ins.html', context)


@login_required(login_url='login')
def inventory(request):
    if request.method == 'POST':
        items_name = request.POST.get('items')
        item_quantity = request.POST.get('Item_Quantity')
        update_item = items.objects.get(item_name=items_name)
        update_item.item_quantity = int(item_quantity)
        update_item.save()

    itemses = items.objects.all()
    context = {'itemses': itemses}
    return render(request, 'html/9_SMS_Managerial_Module_Inventory.html', context)


@login_required(login_url='login')
def room(request):
    if request.method == 'POST':
        rooms_name = request.POST.get('room_name')
        room_price = request.POST.get('Room_Price')

        update_room = rooms.objects.get(room_name=rooms_name)
        update_room.room_price = int(room_price)
        update_room.save()

    roomses = rooms.objects.all().order_by('room_price')
    context = {'roomses': roomses}
    return render(request, 'html/12_SMS_Managerial_Managerial_Rooms.html', context)


@login_required(login_url='login')
def sales(request):
    checked_out_customers = customers.objects.filter(status="CHECKED OUT")
    if request.method == 'POST':
        my_path = 'C:\\Users\\A\\Desktop\\WebApp\\Sunbeam_Management_System\\SMS_App\\pdf\\sales.pdf'
        my_data = [['NAME', 'CI Date', 'CO Date', 'CP#', 'Email',
                    'Room', 'Guest', 'days', 'Act', 'Code', 'Total']]
        for i in checked_out_customers:
            i = (i.first_name + ' ' + i.last_name, i.checkin_date, i.checkout_date, i.contact_num,
                 i.email, i.room_name, i.guest, i.num_of_days, i.activity, i.code, i.price)
            my_data.append(i)
            print(i)
        print(my_data)
        my_doc = SimpleDocTemplate(my_path, pagesize=landscape(A4))
        t = Table(my_data, rowHeights=20, repeatRows=1)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                               ('FONTSIZE', (0, 0), (-1, -1), 10)]))
        elements = []
        elements.append(t)
        my_doc.build(elements)

    checked_out_customers = customers.objects.filter(status="CHECKED OUT")
    context = {'checked_out_customers': checked_out_customers}
    return render(request, 'html/10_SMS_Managerial_Module_Sales.html', context)


@login_required(login_url='login')
def feedback(request):
    feedback = feedbacks.objects.all()
    context = {'feedback': feedback}
    return render(request, 'html/11_SMS_Managerial_Module_Feedback.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
# Create your views here.


######################################

def checkin_boat():
    update_boat = items.objects.get(item_name="Boat")
    boat = update_boat.item_quantity - update_customer.guest
    update_boat.item_inuse = (
        update_boat.item_quantity - boat) + update_boat.item_inuse
    update_boat.save()


def checkin_bankero():
    update_bankero = items.objects.get(item_name="Bankero")
    bankero = update_bankero.item_quantity - update_customer.guest
    update_bankero.item_inuse = (
        update_bankero.item_quantity - bankero) + update_bankero.item_inuse
    update_bankero.save()


def checkin_diving_suit():
    update_diving_suit = items.objects.get(item_name="Diving Suit")
    diving_suit = update_diving_suit.item_quantity - update_customer.guest
    update_diving_suit.item_inuse = (
        update_diving_suit.item_quantity - diving_suit) + update_diving_suit.item_inuse
    update_diving_suit.save()


def checkin_diving_gear():
    update_diving_gear = items.objects.get(item_name="Diving Gear")
    diving_gear = update_diving_gear.item_quantity - update_customer.guest
    update_diving_gear.item_inuse = (
        update_diving_gear.item_quantity - diving_gear) + update_diving_gear.item_inuse
    update_diving_gear.save()


def checkin_life_vest():
    update_life_vest = items.objects.get(item_name="Life Vest")
    life_vest = update_life_vest.item_quantity - update_customer.guest
    update_life_vest.item_inuse = (
        update_life_vest.item_quantity - life_vest) + update_life_vest.item_inuse
    update_life_vest.save()


def checkin_flashlights():
    update_flashlights = items.objects.get(item_name="Flashlights")
    flashlights = update_flashlights.item_quantity - update_customer.guest
    update_flashlights.item_inuse = (
        update_flashlights.item_quantity - flashlights) + update_flashlights.item_inuse
    update_flashlights.save()


def checkin_snorkels():
    update_snorkels = items.objects.get(item_name="Snorkels")
    snorkels = update_snorkels.item_quantity - update_customer.guest
    update_snorkels.item_inuse = (
        update_snorkels.item_quantity - snorkels) + update_snorkels.item_inuse
    update_snorkels.save()


def checkin_regulators():
    update_regulators = items.objects.get(item_name="Regulators")
    regulators = update_regulators.item_quantity - update_customer.guest
    update_regulators.item_inuse = (
        update_regulators.item_quantity - regulators) + update_regulators.item_inuse
    update_regulators.save()


def checkin_oxygen_tanks():
    update_oxygen_tanks = items.objects.get(item_name="Oxygen Tanks")
    oxygen_tanks = update_oxygen_tanks.item_quantity - update_customer.guest
    update_oxygen_tanks.item_inuse = (
        update_oxygen_tanks.item_quantity - oxygen_tanks) + update_oxygen_tanks.item_inuse
    update_oxygen_tanks.save()


def checkin_ropes():
    update_ropes = items.objects.get(item_name="Ropes")
    ropes = update_ropes.item_quantity - update_customer.guest
    update_ropes.item_inuse = (
        update_ropes.item_quantity - ropes) + update_ropes.item_inuse
    update_ropes.save()


def checkin_diving_instructor():
    update_diving_instructor = items.objects.get(item_name="Diving Instructor")
    diving_instructor = update_diving_instructor.item_quantity - update_customer.guest
    update_diving_instructor.item_inuse = (
        update_diving_instructor.item_quantity - diving_instructor) + update_diving_instructor.item_inuse
    update_diving_instructor.save()

#############################################################


def booking_boat():
    update_boat = items.objects.get(item_name="Boat")
    boat = update_boat.item_quantity - update_customers.guest
    update_boat.item_inuse = update_boat.item_inuse - (
        update_boat.item_quantity - boat)
    update_boat.save()


def booking_bankero():
    update_bankero = items.objects.get(item_name="Bankero")
    bankero = update_bankero.item_quantity - update_customers.guest
    update_bankero.item_inuse = update_bankero.item_inuse - (
        update_bankero.item_quantity - bankero)
    update_bankero.save()


def booking_diving_suit():
    update_diving_suit = items.objects.get(item_name="Diving Suit")
    diving_suit = update_diving_suit.item_quantity - update_customers.guest
    update_diving_suit.item_inuse = update_diving_suit.item_inuse(
        update_diving_suit.item_quantity - diving_suit)
    update_diving_suit.save()


def booking_diving_gear():
    update_diving_gear = items.objects.get(item_name="Diving Gear")
    diving_gear = update_diving_gear.item_quantity - update_customers.guest
    update_diving_gear.item_inuse = update_diving_gear.item_inuse(
        update_diving_gear.item_quantity - diving_gear)
    update_diving_gear.save()


def booking_life_vest():
    update_life_vest = items.objects.get(item_name="Life Vest")
    life_vest = update_life_vest.item_quantity - update_customers.guest
    update_life_vest.item_inuse = update_life_vest.item_inuse - (
        update_life_vest.item_quantity - life_vest)
    update_life_vest.save()


def booking_flashlights():
    update_flashlights = items.objects.get(item_name="Flashlights")
    flashlights = update_flashlights.item_quantity - update_customers.guest
    update_flashlights.item_inuse = update_flashlights.item_inuse - (
        update_flashlights.item_quantity - flashlights)
    update_flashlights.save()


def booking_snorkels():
    update_snorkels = items.objects.get(item_name="Snorkels")
    snorkels = update_snorkels.item_quantity - update_customers.guest
    update_snorkels.item_inuse = update_snorkels.item_inuse - (
        update_snorkels.item_quantity - snorkels)
    update_snorkels.save()


def booking_regulators():
    update_regulators = items.objects.get(item_name="Regulators")
    regulators = update_regulators.item_quantity - update_customers.guest
    update_regulators.item_inuse = update_regulators.item_inuse - (
        update_regulators.item_quantity - regulators)
    update_regulators.save()


def booking_oxygen_tanks():
    update_oxygen_tanks = items.objects.get(item_name="Oxygen Tanks")
    oxygen_tanks = update_oxygen_tanks.item_quantity - update_customers.guest
    update_oxygen_tanks.item_inuse = update_oxygen_tanks.item_inuse - (
        update_oxygen_tanks.item_quantity - oxygen_tanks)
    update_oxygen_tanks.save()


def booking_ropes():
    update_ropes = items.objects.get(item_name="Ropes")
    ropes = update_ropes.item_quantity - update_customers.guest
    update_ropes.item_inuse = update_ropes.item_inuse - (
        update_ropes.item_quantity - ropes)
    update_ropes.save()


def booking_diving_instructor():
    update_diving_instructor = items.objects.get(item_name="Diving Instructor")
    diving_instructor = update_diving_instructor.item_quantity - update_customers.guest
    update_diving_instructor.item_inuse = update_diving_instructor.item_inuse - (
        update_diving_instructor.item_quantity - diving_instructor)
    update_diving_instructor.save()


########################################################################

def walkin_boat():
    update_boat = items.objects.get(item_name="Boat")
    boat = update_boat.item_quantity - int(numguest)
    update_boat.item_inuse = (
        update_boat.item_quantity - boat) + update_boat.item_inuse
    update_boat.save()


def walkin_bankero():
    update_bankero = items.objects.get(item_name="Bankero")
    bankero = update_bankero.item_quantity - int(numguest)
    update_bankero.item_inuse = (
        update_bankero.item_quantity - bankero) + update_bankero.item_inuse
    update_bankero.save()


def walkin_diving_suit():
    update_diving_suit = items.objects.get(item_name="Diving Suit")
    diving_suit = update_diving_suit.item_quantity - int(numguest)
    update_diving_suit.item_inuse = (
        update_diving_suit.item_quantity - diving_suit) + update_diving_suit.item_inuse
    update_diving_suit.save()


def walkin_diving_gear():
    update_diving_gear = items.objects.get(item_name="Diving Gear")
    diving_gear = update_diving_gear.item_quantity - int(numguest)
    update_diving_gear.item_inuse = (
        update_diving_gear.item_quantity - diving_gear) + update_diving_gear.item_inuse
    update_diving_gear.save()


def walkin_life_vest():
    update_life_vest = items.objects.get(item_name="Life Vest")
    life_vest = update_life_vest.item_quantity - int(numguest)
    update_life_vest.item_inuse = (
        update_life_vest.item_quantity - life_vest) + update_life_vest.item_inuse
    update_life_vest.save()


def walkin_flashlights():
    update_flashlights = items.objects.get(item_name="Flashlights")
    flashlights = update_flashlights.item_quantity - int(numguest)
    update_flashlights.item_inuse = (
        update_flashlights.item_quantity - flashlights) + update_flashlights.item_inuse
    update_flashlights.save()


def walkin_snorkels():
    update_snorkels = items.objects.get(item_name="Snorkels")
    snorkels = update_snorkels.item_quantity - int(numguest)
    update_snorkels.item_inuse = (
        update_snorkels.item_quantity - snorkels) + update_snorkels.item_inuse
    update_snorkels.save()


def walkin_regulators():
    update_regulators = items.objects.get(item_name="Regulators")
    regulators = update_regulators.item_quantity - int(numguest)
    update_regulators.item_inuse = (
        update_regulators.item_quantity - regulators) + update_regulators.item_inuse
    update_regulators.save()


def walkin_oxygen_tanks():
    update_oxygen_tanks = items.objects.get(item_name="Oxygen Tanks")
    oxygen_tanks = update_oxygen_tanks.item_quantity - int(numguest)
    update_oxygen_tanks.item_inuse = (
        update_oxygen_tanks.item_quantity - oxygen_tanks) + update_oxygen_tanks.item_inuse
    update_oxygen_tanks.save()


def walkin_ropes():
    update_ropes = items.objects.get(item_name="Ropes")
    ropes = update_ropes.item_quantity - int(numguest)
    update_ropes.item_inuse = (
        update_ropes.item_quantity - ropes) + update_ropes.item_inuse
    update_ropes.save()


def walkin_diving_instructor():
    update_diving_instructor = items.objects.get(item_name="Diving Instructor")
    diving_instructor = update_diving_instructor.item_quantity - int(numguest)
    update_diving_instructor.item_inuse = (
        update_diving_instructor.item_quantity - diving_instructor) + update_diving_instructor.item_inuse
    update_diving_instructor.save()
