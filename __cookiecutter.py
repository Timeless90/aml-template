from cookiecutter.main import cookiecutter
from datetime import datetime
import os


def run():
    template = os.path.dirname(os.path.realpath(__file__))
    print(template)

    cookiecutter(
        template,
        extra_context={
            'timestamp': datetime.utcnow().date()
        }
    )


if __name__ == '__main__':
    run()
