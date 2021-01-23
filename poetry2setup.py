from poetry.core.utils._compat import Path
from poetry.core.factory import Factory
from poetry.core.masonry.builders.sdist import SdistBuilder


def build_setup_py():
    return SdistBuilder(Factory().create_poetry(Path(".").resolve())).build_setup()


def main():
    print(build_setup_py().decode("utf8"))


if __name__ == "__main__":
    main()
