from pathlib import Path

from setuptools import find_packages, setup


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str):
    requirements_path = Path(file_path)
    requirements = []

    for raw_line in requirements_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        requirements.append(line)

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="cnnclassifier",
    version="0.0.0",
    description="CNN classifier package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
    include_package_data=True,
    python_requires=">=3.8",
)
