# coding=utf-8

from django.db import transaction


@transaction.commit_manually
def flush_transaction():
    transaction.enter_transaction_management()
    transaction.commit()
