# Airflow Django

TBD

## Install

### Poetry
```console
poetry add airflow-django
```

### Pipenv

```console
pipenv install airflow-django
```

### Pip

```
pip install airflow-django
```

## Configuration

### Environment variables

- `AIRFLOW_DJANGO_PATH_TO_SETTINGS_PY`: The directory, where `settings.py` is located (default: `/usr/src/app/project`)

## Quick start

After installing [`airflow-django`](https://pypi.org/project/airflow-django/), set the `AIRFLOW_DJANGO_PATH_TO_SETTINGS_PY` variable.

Then create your custom operator for tasks that aim to communicate with the Django ORM

```py
from datetime import datetime, timedelta

from airflow import DAG
from airflow_django.operators import DjangoOperator

from my_app.models import AmazingModel


dag = DAG(
    'amazing_dag',
    description='This is an amazing Dag',
    schedule_interval=timedelta(days=1),
    default_args={'start_date': datetime(2020, 3, 26)},
)


def create_an_amazing_instance(ds, **kwargs):
    amazing_instance = AmazingModel.objects.create()
    return amazing_instance


run_this = DjangoOperator(
    task_id='create_an_amazing_instance',
    provide_context=True,
    python_callable=create_an_amazing_instance,
    dag=dag,
)
```
