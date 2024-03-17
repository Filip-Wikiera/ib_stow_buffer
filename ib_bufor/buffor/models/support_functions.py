from django.db.models.functions import Abs


def closest_count(model, datetime_point):
    return model.objects.filter(time_stamp__lt=datetime_point).order_by('-time_stamp').first()