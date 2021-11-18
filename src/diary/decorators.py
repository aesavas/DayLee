from django.contrib import messages
from functools import wraps
from django.shortcuts import redirect, render
from users.utils import check_master_password

