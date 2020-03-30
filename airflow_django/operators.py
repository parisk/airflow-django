import os
import sys

from airflow.operators.python_operator import PythonOperator


DJANGO_ENVIRONMENT_HAS_BEEN_SETUP = False


def setup_django_for_airflow(path_to_settings_py: str):
    if DJANGO_ENVIRONMENT_HAS_BEEN_SETUP:
        return

    base_directory = os.path.dirname(path_to_settings_py)
    project_name = os.path.basename(base_directory)

    # Add Django project root to path
    sys.path.append(base_directory)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")

    import django
    django.setup()

    DJANGO_ENVIRONMENT_HAS_BEEN_SETUP = True


class DjangoOperator(PythonOperator):
    path_to_settings_py: str = os.getenv("AIRFLOW_DJANGO_PATH_TO_SETTINGS_PY", "/usr/src/app/project")

    def pre_execute(self, *args, **kwargs):
        setup_django_for_airflow(self.path_to_settings_py)